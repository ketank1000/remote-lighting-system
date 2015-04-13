from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect,HttpResponse
from django.db import connection
from django.contrib import auth
from django.template import RequestContext, loader, Context
from auth.models import leds
from auth.models import ledsgroup
from auth.models import group_name
from django.contrib.auth.decorators import login_required
from socket import *
import threading
import thread

conn = ['',0]

def sender(msg):
		clientsock.send(msg)


def handler(clientsock,addr):
        sender(msg)
    


def connect_user(request):


	if request.session['connectionflag'] == 0:


		timeout = 30


		HOST = '0.0.0.0'
		PORT = 5000
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.settimeout(timeout)
		s.bind((HOST, PORT))
		s.listen(1)

		try:

			global conn
			conn, addr = s.accept()
			username = conn.recv(1024)
			password = conn.recv(1024)
			user = authenticate(username=username, password=password)
			
			if user is not None:
				if username == request.session['user']:
					request.session['connectionflag'] = 1
					conn.sendall('1')
					thread.start_new_thread(handler, (clientsock, addr))

				else:
					conn.sendall('0')
			else:
				conn.sendall('0')
	
		except socket.timeout:
			request.session['connectionflag'] = 0


	return HttpResponseRedirect('/user_home/')



def login_user(request):
	state = "Please login below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

	
		user = authenticate(username=username, password=password)
		
	   	if user is not None:
	   		auth.login(request, user)
	   		response = HttpResponseRedirect("/user_home/")
	   		response.set_cookie("user", request.POST.get('username'))
	   		request.session["user"] = username
			request.session["connectionflag"] = 0
			request.session["conn"]= ['',0]
			return response
	
	   	else:
	   	    state = "Your username and/or password were incorrect."
        
	return render_to_response('auth/login.html',{'state':state, 'username': username})




def register_user(request):
	name = email = url = message = ''
	if request.POST:
		name = request.POST.get('username')
		email = request.POST.get('email')
		url = request.POST.get('url')
		message = request.POST.get('message')

	return render_to_response('auth/register.html')

def logout(request):	
	if request.session['connectionflag'] == 1:
		global conn
		conn.sendall('9')
		request.session['connectionflag'] = 0
		global conn
		conn.close()


	del request.session['user']
	auth.logout(request)

	return HttpResponseRedirect('/index/')


def update(request):
	name = status = ""
	username = ""
	username = request.session['user']
	name = request.POST.get('FirstName')
	status = request.POST.get('ledstatus')
	intensity = request.POST.get('intensity')
	a = leds.objects.filter(username=username)
	for i in a:
		if i.name == name:
			i.status = status
			i.intesity = intensity
			i.save()
		if request.session['connectionflag'] == 1:

			if i.name == '2s':

				if status == '1':

					inter = int(intensity)
					int1 = str(inter)

					global conn
					conn.sendall(int1)

				else:
					global conn
					conn.sendall('0')
	return HttpResponseRedirect('/user_home/')
	

def edit_update(request):
	name = x = y = fill = ""
	username = ""
	flag = 0
	username = request.session['user']
	led_name = request.POST.get('FirstName')
	x = request.POST.get('xposition')
	y = request.POST.get('yposition')
	fill = request.POST.get('fill')
	a = leds.objects.filter(username=username)
	for i in a:
		if i.name == led_name:
			if x == "0":
				i.delete()
				return HttpResponseRedirect('/edit/')
			i.x = int(x)
			i.y = int(y)
			i.color = fill
			flag = 1
			i.save()
	if flag == 0:
		a = leds(username=username,name=led_name,x=x,y=y,status=0,radius=15,color=fill)
		a.save()
	return HttpResponseRedirect('/edit/')


def group_update(request):
	if 'add' in request.POST:
		name = x = ""
		username = groupname = groupcolor = ""
		username = request.session['user']
		led_name = request.POST.get('FirstName')
		groupname = request.POST.get('grname')
		color = group_name.objects.filter(groupname=groupname)
		for i in color:
			x = i.groupcolor
			i.quantity = i.quantity + 1
		i.save()
		a = ledsgroup(username=username,name=led_name,groupcolor=x,groupname=groupname)
		a.save()
	elif 'delete' in request.POST:
		username = request.session['user']
		led_name = request.POST.get('FirstName')
		groupname = request.POST.get('grname')
		a = ledsgroup.objects.filter(username=username)
		x = group_name.objects.filter(groupname=groupname)
		for i in x:
			i.quantity = i.quantity - 1
		i.save()
		for i in a:
			if i.groupname == groupname and i.name == led_name:
				i.delete()

	return HttpResponseRedirect('/group/')

def add_group(request):
	username = ""
	username = request.session['user']
	groupname = request.POST.get('groupname')
	color = request.POST.get('grfill')
	a=group_name(username=username,groupname=groupname,groupcolor=color)
	a.save()
	return HttpResponseRedirect('/group/')

def group_status(request):
	if 'save' in request.POST:
		username = ""
		username = request.session['user']
		groupname = request.POST.get('groupname')
		status = request.POST.get('ledstatus')
		intensity = request.POST.get('intensity')
		a = ledsgroup.objects.filter(groupname=groupname)
		led = leds.objects.filter(username=username)
		for i in a:
			for x in led:
				if x.name == i.name:
					x.status = status
					x.intensity = intensity
					x.save()
		return HttpResponseRedirect('/group/')
	
	elif 'delete' in request.POST:
		username = ""
		username = request.session['user']
		groupname = request.POST.get('groupname')
		a = ledsgroup.objects.filter(groupname=groupname)
		b = group_name.objects.filter(groupname=groupname)
		for i in a:
			i.delete()
		b.delete()
		return HttpResponseRedirect('/group/')
	return HttpResponseRedirect('/group/')


def user_home(request):

	username = ''
	user = ''

	if 'user' in request.session:
		username = request.session['user']
		template = loader.get_template('profile/user_home.html')
		led = leds.objects.filter(username=username)
		x_forwarded_for = request.META.get(' HTTP_X_FORWARDED_FOR')
	
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
	
		context = RequestContext(request, {'username': username, 'led':led,'client':ip,'connection':request.session['connectionflag']})
		return HttpResponse(template.render(context))
		
	else:
		return HttpResponseRedirect('/login/')


