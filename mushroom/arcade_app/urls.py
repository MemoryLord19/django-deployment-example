#URLs for arcade_app
from django.conf.urls import url
from arcade_app import views

#For template tagging
app_name = 'arcade_app'

urlpatterns =[
	url(r'^$',views.index,name='index'),
	url(r'^chat/$',views.chat,name='chat'),
	url(r'^games/$',views.games,name='games'),
	url(r'^connect_four/$',views.connect_four,name='connect_four'),
	url(r'^knots_and_crosses/$',views.kac,name='knots_and_crosses'),
]