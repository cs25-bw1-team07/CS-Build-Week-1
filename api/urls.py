from django.urls import include, path
# from django.conf.urls import url
from .views import RoomView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path("room/", RoomView.as_view(), name="rooms"),
]
