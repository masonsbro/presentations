from django.shortcuts import render, redirect

from models import *

# Create your views here.

def index(req):
	return render(req, "landing.html", {'request': req})

def login(req):
	return render(req, "login.html", {'request': req})

def register(req):
	if req.method == 'POST':
		try:
			user = User(email = req.POST['email'])
			user.set_password(req.POST['password'])
			req.session['email'] = req.POST['email']
			return redirect("/")
		except:
			# I'm kind of lazy
			pass
	return render(req, "register.html", {'request': req})
