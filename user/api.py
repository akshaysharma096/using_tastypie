from tastypie.resources import ModelResource
from user.models import Entry
from tastypie import fields
from tastypie.authentication import BasicAuthentication,ApiKeyAuthentication,SessionAuthentication,DigestAuthentication,OAuthAuthentication
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class UserResource(ModelResource):
	entries=fields.ToManyField('user.api.EntryResource','entries')
	class Meta:
		queryset=User.objects.all()
		resource_name='user'
		#excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser'] 	#specify which fields to exclude
		fields = ['username', 'first_name', 'last_name', 'last_login']  			#or use this
		allowed_methods = ['get']   #allowed http methods
		authentication=ApiKeyAuthentication()
		filtering = {
            'username': ['exact'],
        }

class EntryResource(ModelResource):
	# Maps `Entry.user` to a Tastypie `ForeignKey` field named `user`,
    # which gets serialized using `UserResource`. The first appearance of
    # 'user' on the next line of code is the Tastypie field name, the 2nd
    # appearance tells the `ForeignKey` it maps to the `user` attribute of
    # `Entry`. Field names and model attributes don't have to be the same.
    user=fields.ForeignKey(UserResource,'user',full=True) #Foreign Key is not added in serialiation adding it explicitly.
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authorization=Authorization() 			#	prevents PUT,DELETE and POST requests on the url.
        allowed_methods = ['get','post']   			#	allowed http methods
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
            'slug':['exact'],
            'title':['exact']
        }
