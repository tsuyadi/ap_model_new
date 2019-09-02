from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ap_model.agencies.models import *
from ap_model.agencies.serializers import *


# Create your views here.
class BranchList(APIView):
    def get(self, request, format=None):
        try:
            branchs = Branch.objects.all().order_by('name')
            serializer = BranchSerializer(branchs, many=True)

            return Response({"status": "OK","content": serializer.data }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"status": "NOT OK", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)