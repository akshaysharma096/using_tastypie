from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from tastypie.authentication import ApiKeyAuthentication
from django.contrib.auth import authenticate
# Create your views here.


class LoginView(View):
	http_method_names=['get']
	content_type='application/json'
	charset='utf-8'

	def get(self,request):
		obj=ApiKeyAuthentication()
		try:
			username_from_request=request.META['HTTP_USERNAME']
			password=request.META['HTTP_PASSWORD']
			if username_from_request is not None and password is not None:
				user=authenticate(username=username_from_request,password=password)
				if user is not None:
					is_auth=obj.is_authenticated(request)
					if is_auth:
						return HttpResponse(status=200,content_type='application/json')
					else:
						return HttpResponse(status=200,content_type='application/json')
				else:
					return HttpResponse(status=401,content_type='application/json')
			else:
				return HttpResponse(status=401,content_type='application/json')
		except(KeyError):
			return HttpResponse(status=400,content_type='application/json')


