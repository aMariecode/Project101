from django.shortcuts import render, redirect
from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the registration
            messages.success(request, "Registration successful!")
            # return redirect('login')  # Redirect to login page (you can adjust this)
        else:
            messages.error(request, "There was an error in the registration form.")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# def home(request):
#     return render(request, 'home.html')

@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)