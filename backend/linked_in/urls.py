from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes" ),
    path('jobs/', views.getJobs, name="jobs" ),
    path('jobs/<int:pk>', views.getJob, name="job" ),
    
]