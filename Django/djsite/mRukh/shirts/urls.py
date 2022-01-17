from django.urls import path, re_path

from .views import *

urlpatterns = {
    path('', index, name='home'),
    path('t-shirts/<int:tshirtsID>/', categories),  # http://127.0.0.1:8000/t-shirts/11
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
}
