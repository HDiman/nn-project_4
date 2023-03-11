from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('task', views.task, name="task"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
]
