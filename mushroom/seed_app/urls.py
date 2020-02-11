#URLs for seed_app
from django.conf.urls import url
from seed_app import views

#For template tagging

app_name='seed_app'

urlpatterns = [
	url(r'^user_login/$',views.user_login,name='user_login'),
	url(r'^register/$',views.register,name='register'),
]
