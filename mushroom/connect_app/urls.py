#URLs for connect_app
from django.conf.urls import url
from connect_app import views

#For template tagging
app_name = 'connect_app'

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^find/$',views.find,name='find'),
	url(r'^messages/$',views.messages,name='messages'),
	url(r'^public/$',views.public,name='public'),
]