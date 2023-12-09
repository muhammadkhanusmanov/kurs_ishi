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

from .models import Category

from .serialzers import CategorySerializer



class LoginView(APIView):
    authentication_classes = [BasicAuthentication]
    def post(self, request):
        user = request.user
        token = Token.objects.get_or_create(user=user)
        token = str(token[0])
        return Response({'detail':True,'token':token},status=status.HTTP_201_CREATED)


class AdminView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    '''Add a new category'''
    def post(self, request):
        data = request.data
        image = request.data.get('img', None)
        try:
            category = Category.objects.create(
                name = data.get('name'),
                img = image
            )
            print(category)
            category.save()
            return Response({'status':True},status=status.HTTP_201_CREATED)
        except:
            return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)


class GetData(APIView):
    def get(self, request,id:str):
        try:
            file = Category.objects.get(id=id)
            img =file.img 
            file = open(img.path, 'rb')
            resp = FileResponse(img)
            return resp
        except:
            return Response({'status':False}, status=status.HTTP_400_BAD_REQUEST)