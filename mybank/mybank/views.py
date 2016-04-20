#-*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django import template
from django.http import HttpResponse
from django.contrib import auth
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	return render_to_response('home.html', RequestContext(request, locals()))  #不能直接進入home.html 要透過登入
def main(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	return render_to_response('main.html', RequestContext(request, locals()))  #不能直接進入main.html 要透過登入
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	username = request.POST.get('username', '')
	password = request.POST.get('password' '')
	
	user = auth.authenticate(username=username, password=password)
	
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/home/')
	else:
		return render_to_response('login.html', RequestContext(request, locals()))
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/accounts/login/')
	
	
	return render_to_response('home.html', locals())
	
def register(request):  #註冊
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/accounts/login/')
	else:
		form = UserCreationForm()
	return render_to_response('login.html', RequestContext(request, locals()))
