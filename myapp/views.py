
from http.client import HTTPResponse
from multiprocessing import context
from django.contrib import messages
from urllib import response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import User
from rest_framework.views import APIView
import jwt ,datetime

from .serializers import UserSerializer


# Create your views here.
def homePage(request):
    return render(request,'welcomePage.html')

class RegisterView(APIView):
     def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = User.objects.filter(email=email).first()
        if user is None:
            messages.error(request,'user not found')
            return redirect('/')
        
        if not user.check_password(password):

            messages.error(request,'Incorrect password')
            return redirect('/')
        else:
            payload={
            'id': user.id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
            }
            messages.success(request,f'hi {user}, you sucessfully authenticated by your email id')
            token = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='jwt',value=token,httponly=True)
            response.data={
                'jwt':token
            }
            return redirect('home')
        
    return render(request,'login.html')


def loginUser(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unanthenticated')
    try:
        payload= jwt.decode(token,'secret',algorithms=['HS256'])
    except:
        raise AuthenticationFailed('Unanthenticated')
    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)

        
    return render(request,'home.html')

    
    
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success'
        }
        return response
    

def homePage2(request):
    return render(request, 'home.html')