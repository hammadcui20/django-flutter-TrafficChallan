# myapp/views.py
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm, UserCreationForm, LoginForm
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout 



# server = 'computervision.database.windows.net'
# database = 'mydb_2'
# username = 'manager'
# password = "7QaG4'/jlJ]6"
# driver = '{ODBC Driver 17 for SQL Server}'
# connection = pyodbc.connect(
#     f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# )

    
def your_view_function(request):
    admin_url = reverse('admin:index')  # 'admin:index' is the URL name for the admin index page
    return HttpResponseRedirect(admin_url)

def index(request):
    return render(request, 'myapp/index.html')
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)    
#                 return redirect('index')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# logout page
# def user_logout(request):
#     logout(request)
#     return redirect('index')
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .serializers import LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return 

class UserLoginAPIView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    @permission_classes([AllowAny])
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
                return redirect('index')
            else:
               return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
                # form = LoginForm()
                # return render(request, 'login.html', {'form': form})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserLogoutAPIView(APIView):
    # @csrf_exempt
    authentication_classes = (CsrfExemptSessionAuthentication,)
    @permission_classes([AllowAny])
    def post(self, request, *args, **kwargs):
        # user_id = request.user.id  # Get the user ID instead of using the LazyObject directly
        # print(user_id)
        logout(request)
        # return Response(status=status.HTTP_200_OK)
        return redirect('index')
    
def about_us(request):
    return render(request, 'myapp/about.html')

def contact_us(request):
    return render(request, 'myapp/contact.html')

def by_video(request):
    return render(request, 'myapp/byvideo.html')

def by_webcam(request):
    return render(request, 'myapp/bywebcam.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a thank you page or homepage
    else:
        form = ContactForm()

    return render(request, 'myapp/contact.html', {'form': form})


def webcam_prediction(request):
    return render(request, 'myapp/webcam_prediction.html')


    