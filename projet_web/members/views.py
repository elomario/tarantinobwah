from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django import forms

def member_login(request):
    # Like before, obtain the context for the user's request.
	context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
		if user:
            # Is the account active? It could have been disabled.
			if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/home/')
				#return HttpResponse("GG")
			else:
                # An inactive account was used - no logging in!
				return HttpResponse("Your PIC account is disabled.")
		else:
            # Bad login details were provided. So we can't log the user in.
			#print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
	else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
		return render_to_response('members/login.html', {}, context)
	
	
def member_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def	home(request):
	return render(request,'members/home_member.html')

def	presentation(request):
	return render(request,'members/presentation.html')
	
def	shell(request):
	return render(request,'members/shell.html')