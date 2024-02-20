$(document).ready(function () {
    let webcamStream;
    const webcamFeed = document.getElementById('webcamFeed');
    const predictionResults = document.getElementById('predictionResults');
    const startWebcamBtn = document.getElementById('startWebcam');
    const stopWebcamBtn = document.getElementById('stopWebcam');
    const startPredictionBtn = document.getElementById('startPrediction');

    startWebcamBtn.addEventListener('click', startWebcam);
    stopWebcamBtn.addEventListener('click', stopWebcam);
    startPredictionBtn.addEventListener('click', startPrediction);

    async function startWebcam() {
        try {
            webcamStream = await navigator.mediaDevices.getUserMedia({ video: true });
            webcamFeed.srcObject = webcamStream;
            startWebcamBtn.style.display = 'none';
            stopWebcamBtn.style.display = 'block';
            startPredictionBtn.style.display = 'block';
        } catch (error) {
            console.error('Error starting webcam:', error);
        }
    }

    function stopWebcam() {
        if (webcamStream) {
            webcamStream.getTracks().forEach(track => track.stop());
            webcamFeed.srcObject = null;
            startWebcamBtn.style.display = 'block';
            stopWebcamBtn.style.display = 'none';
            startPredictionBtn.style.display = 'none';
        }
    }

    function startPrediction() {
        // Load the YOLO model
        const net = new darknet.Net({
            weights: 'C:/Users/user/Desktop/suspiciousdetector/files/yolov2-tiny.weights',
            config: 'C:/Users/user/Desktop/suspiciousdetector/files/yolov2-tiny.cfg',
            names: 'C:/Users/user/Desktop/suspiciousdetector/files/coco.names', // File containing class names
        });
        
        const video = document.getElementById('webcamFeed');
        navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
            video.srcObject = stream;

            // Start YOLO prediction on each frame
            video.addEventListener('loadeddata', function () {
                setInterval(() => {
                    const predictions = net.forward(video);
                    console.log('Predictions:', predictions); // Log predictions for debugging
                    displayPredictions(predictions);
                }, 1000 / 30); // Adjust the interval based on your needs
            });
        });
    }

    function displayPredictions(predictions) {
        const predictionResults = document.getElementById('predictionResults');
        predictionResults.innerHTML = '';

        predictions.forEach((prediction) => {
            const label = prediction.class;
            const confidence = (prediction.confidence * 100).toFixed(2);

            const result = document.createElement('p');
            result.textContent = `${label}: ${confidence}% confidence`;
            predictionResults.appendChild(result);
            predictionResults.innerHTML = 'Prediction in progress...'; // Placeholder message

        });
    }
});
