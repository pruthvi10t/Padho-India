from django.urls import path

from . import views

urlpatterns = [
	path('donor/',views.home_page,name="donor_home_page"),
	path('',views.register_donor,name='register_donor'),
]