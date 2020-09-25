from django.urls import path, include
app_name = 'companyapp'
urlpatterns = [
    path('', include('companyapp.api.urls')),
]
