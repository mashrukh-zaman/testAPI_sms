from django.urls import re_path, include, path
from api import views 
 
urlpatterns = [ 
    # path('api/tutorials/', views.tutorial_list),
    # path('api/tutorials/<int:pk>', views.tutorial_detail),
    # path('api/tutorials/published', views.tutorial_list_published),
    path('sms', views.send_sms)
]