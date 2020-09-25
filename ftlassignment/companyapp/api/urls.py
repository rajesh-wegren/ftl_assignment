from django.urls import path, include


from companyapp.api.views import MemberListAPIView

urlpatterns = [

   path('list', MemberListAPIView.as_view(), name='member-list'),
]
