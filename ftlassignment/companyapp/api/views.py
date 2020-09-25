
from rest_framework import status, mixins, generics
import datetime
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from companyapp.api.serializers import PeriodSerializer,MemberSerializer
from companyapp.models import Member,Period
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import APIException
import json
# from timezone_field import TimeZoneField


class MemberListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Member.objects.all().order_by('id')
    serializer_class = PeriodSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = request.query_params.get("q")

        paginator = PageNumberPagination()

        paginator.page_size = 10
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = MemberSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)