from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mindtest_id>/', views.detail, name='detail'),
    path('<int:mindtest_id>/results/', views.results, name='results'),
    path('<int:mindtest_id>/vote/', views.vote, name='vote')
]

app_name= 'mindtest'