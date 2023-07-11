from django.urls import path
from information import views


urlpatterns = [
    # http://127.0.0.1:8000/info/about
    path('about', views.show_about, name='about'),

    # http://127.0.0.1:8000/info/contacts
    path('contacts', views.show_contacts, name='contacts'),

    # http://127.0.0.1:8000/info/policy
    path('policy', views.show_policy)
]
