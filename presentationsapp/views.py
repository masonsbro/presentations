import zipfile

from django.shortcuts import render, redirect

from models import *

# Create your views here.

def only_logged_in(func):
	def wrapper(req, *args, **kwargs):
		if 'email' in req.session:
			return func(req, *args, **kwargs)
		else:
			return redirect("/login/")
	return wrapper

def index(req):
	return render(req, "landing.html", {'request': req})

def login(req):
	if req.method == 'POST':
		try:
			user = User.objects.get(email = req.POST['email'])
			if user.check_password(req.POST['password']):
				req.session['email'] = req.POST['email']
				return redirect("/")
		except:
			pass
	return render(req, "login.html", {'request': req})

def register(req):
	if req.method == 'POST':
		try:
			user = User(email = req.POST['email'])
			user.set_password(req.POST['password'])
			user.save()
			req.session['email'] = req.POST['email']
			return redirect("/")
		except:
			# I'm kind of lazy
			pass
	return render(req, "register.html", {'request': req})

def logout(req):
	del req.session['email']
	return redirect("/")

@only_logged_in
def create(req):
	if req.method == 'POST':
		try:
			user = User.objects.get(email = req.session['email'])
			presentation = Presentation(title = req.POST['title'], author = user, description = req.POST['description'])
			# First, unzip the file upload
			file = request.FILES['slides']
			with zipfile.ZipFile(file, 'r') as z:
				# Start with 1 and keep going while there are more files
				fn = 'Slide1.PNG'
				slide = Slide(image = z.open(fn, 'r'))
				slide.save()
				presentation.first_slide = slide
				for i in range(2, 1 + len(z.namelist())):
					# Of course, this assumes that the user did what they were supposed to
					# I should probably change this later to fix that assumption
					fn = 'Slide' + str(i) + '.PNG'
					next = Slide(image = z.open(fn, 'r'))
					next.save()
					slide.next = next
					slide.save()
					slide = next
			presentation.save()
		except:
			pass
	return render(req, "create.html", {'request': req})
