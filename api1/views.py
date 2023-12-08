from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpRequest,JsonResponse,FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication, BasicAuthentication



class Login(APIView):
    authentication_classes = [BasicAuthentication]
    def post(self, request):
        user = request.user
        token = Token.objects.get_or_create(user=user)
        token = str(token[0])
        return Response({'detail':True,'token':token},status=status.HTTP_201_CREATED)

