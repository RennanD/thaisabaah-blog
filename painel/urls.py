from django.urls import path
from .views import add, dashboard, update, delete, logout_view, index
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('dashboard/', dashboard, name = "dashboard"),
	path('add/', add, name = "add"),
	path('', index, name = "index"),
	path('update/<int:id>', update, name = "update"),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('delete/<int:id>', delete, name = "delete"),
	path('logout/', logout_view, name = "logout"),

]