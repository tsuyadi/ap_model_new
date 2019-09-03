from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ap_model.agencies.serializers import *
from django.http import Http404, HttpResponse


# Create your views here.
class AgentProfileDisplay(APIView):
    """
    Retrieve Agent Profile data
    """
    def get_object(self, user):
        """Get Agent Profile data from database"""
        try:
            return AgentProfile.objects.get(user=user)
        except AgentProfile.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        """Retrieve Agent Profile data"""
        try:

            try:
                if 'agent' in request.data:
                    agent = request.data['agent']
                    user = User.objects.get(username=agent)
                else:
                    user = request.user
            except Exception as e:
                raise Http404

            agent = self.get_object(user)
            agent_user = agent.user
            agent_serializer = AgentSerializer(agent)
            user_serializer = UserSerializer(agent_user)
            get_response = {"agent_profile": agent_serializer.data, "user": user_serializer.data}
            request_status = "OK"
            http_status = status.HTTP_200_OK
        except Exception as e:
            get_response = None
            request_status = str(e)
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        responses = {"status": request_status, "content": get_response}
        return Response(responses, status=http_status)


class BranchList(APIView):
    def get(self, request, format=None):
        try:
            branchs = Branch.objects.all().order_by('name')
            serializer = BranchSerializer(branchs, many=True)

            return Response({"status": "OK","content": serializer.data }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"status": "NOT OK", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)