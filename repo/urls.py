from django.urls import path
from . import views

app_name = 'repo'


urlpatterns = [
    path('', views.welcome, name='home'),
    path('results', views.getRepos, name='get_result'),
    path('result', views.postRepos, name='post_result')
        
]
