from django.urls import path
from myapp import views

app_name='myapp'

urlpatterns = [
	# path('',views.index,name='index'),
	path('',views.user_login,name='user_login'),
	path('block/',views.block,name='block'),
	# path('lecture/',views.lecture,name='lecture'),
	# path('labs/',views.labs,name='labs')
	path('lecture/booking/',views.booking,name='booking')
]
