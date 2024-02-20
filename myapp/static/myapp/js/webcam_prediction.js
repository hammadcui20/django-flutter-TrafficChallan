// webcam_prediction.js

// Define a global variable for the model
let model;

// Load the pre-trained YOLO model
async function loadModel() {
    model = await tf.loadLayersModel('path/to/model.json'); // Update with the path to your YOLO model
}

// Start the webcam and perform predictions
async function startWebcam() {
    const video = document.getElementById('webcamFeed');
    
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: {} });
        video.srcObject = stream;

        video.addEventListener('loadeddata', async () => {
            // Load the model once the webcam feed is ready
            await loadModel();

            // Enable the prediction button
            document.getElementById('startPrediction').style.display = 'block';
        });
    } catch (error) {
        console.error('Error accessing webcam:', error);
    }
}

// Perform predictions on each frame
async function startPrediction() {
    const video = document.getElementById('webcamFeed');
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');

    // Set canvas dimensions to match the video
    canvas.width = video.width;
    canvas.height = video.height;

    // Append the canvas to the document
    document.body.appendChild(canvas);

    // Continuously perform predictions
    setInterval(async () => {
        // Capture the current frame
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Preprocess the image and perform predictions
        const predictions = await predictFromImage(canvas);

        // Display the predictions
        displayPredictions(predictions);
    }, 1000 / 2); // Adjust the interval based on your needs
}

// Preprocess the image and perform predictions
async function predictFromImage(image) {
    // Convert the image to a TensorFlow.js tensor
    const tensor = tf.browser.fromPixels(image);
    const resized = tf.image.resizeBilinear(tensor, [416, 416]);
    const expanded = resized.expandDims(0).toFloat();

    // Normalize the input image
    const normalized = expanded.div(255.0);

    // Perform predictions
    const predictions = await model.predict(normalized).array();

    return predictions;
}

// Display the predictions
function displayPredictions(predictions) {
    const predictionResults = document.getElementById('predictionResults');
    predictionResults.innerHTML = '';

    // Process the predictions and display the results
    predictions.forEach((prediction) => {
        const label = prediction.class;
        const confidence = (prediction.confidence * 100).toFixed(2);

        const result = document.createElement('p');
        result.textContent = `${label}: ${confidence}% confidence`;
        predictionResults.appendChild(result);
    });
}

// Other existing code...
