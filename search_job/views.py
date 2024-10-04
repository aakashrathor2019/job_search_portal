from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
import re
import requests


# SignUp Form
class SignUp(View):
    def post(self, request):
      try:
        print("Inside post method")
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["conf_password"]

        errors = {}
        # Hunter api key for email verification
        api_key = "d9f88867b0a997ef8e5b91a44b55b8ba2476e00f"

        if any(char.isdigit() for char in username):
            errors["username"] = "username contains character only"

        # Hunter API endpoint
        url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"

        # Make a request to Hunter API
        response = requests.get(url)

        # Parse the JSON response
        data = response.json()

        # Check if the status is 'valid'
        if data["data"]["status"] != "valid":
            errors["email"] = "email does not exists"

        if User.objects.filter(email=email).exists():
            errors["email"] = "already registered"

        if "@" not in email:
            errors["email"] = "enter valid email address"

        if not len(password) >= 8:
            errors["password"] = "password must be 8 characters"

        if not re.search(r"[!@#$%^&*|<>,(),{}]", password):
            errors["password"] = "password contanis atleast one special character"

        if password != confirm_password:
            errors["conf_password"] = "passwords do not match"

        if errors:
            return render(request, "signup.html", {"errors": errors})
        else:
            User.objects.create_user(username=username, password=password, email=email)

        return redirect("login")
      except:
          return render(request , 'signup.html' ,{'error':'Enter valid data'})

    def get(self, request):
        print("inside get method")
        return render(request, "signup.html")


# Login Class
class Login(View):
    def post(self, request):
      try:
        username = request.POST["username"]
        password = request.POST["password"]
    
        user = User.objects.get(username=username)
        print("value of username and password is:", user.username, user.password)
        if user.check_password(password):
            return render(request, "home.html")
        elif not user:
            return render(request, "login.html", {'error':'user does not exists,please register first'})
        else:
            return render(request, "login.html", {"error": "enter valid username or password"})
      except:
          return render(request ,'login.html',{'error':'Enter valid data'})

    def get(self, request):
        print("inside login class")
        return render(request, "login.html")


class Home(View):
    def get(self ,request):
        return render(request, "home.html")
