from django.urls import path
from . import views

#Allow for the user to pass in parameter for get by beer type
#Also include commented out path for get all function
urlpatterns=[
        # path('beer',views.getAllBeer),
        path('beer/<str:pk>',views.getBeer,name='beer'),
    ]