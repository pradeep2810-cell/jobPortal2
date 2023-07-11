from django.urls import path

urlpatterns = [
    # 127.0.0.1/organizations/
    path('', ''),

    # 127.0.0.1/organizations/type
    path('type', ''),

    # 127.0.0.1/organizations/searched
    path('searched', ''),
]
