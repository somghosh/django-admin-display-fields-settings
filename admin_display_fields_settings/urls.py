from django.conf.urls import url
from .ajax import changeFormHandler


urlpatterns = [
    url(r'^change_form/$', changeFormHandler, name='changeFormHandler'),
]
