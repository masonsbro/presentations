from django.shortcuts import render

from models import *

# Create your views here.

def index(req):
	return render(req, "landing.html", {})

def login(req):
	return render(req, "login.html", {})

def register(req):
	return render(req, "register.html", {})
