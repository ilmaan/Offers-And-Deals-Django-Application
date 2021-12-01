from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
# from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.views import APIView
from .serializers import RegisterSerializer

import ast
# Create your views here.



class RegisterApiView(APIView):
    def post(self,request,pk=None, format=None):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'SUCCESS', 'data': 'User Created'}, status=200)
            return Response(serializer.errors) 
        except Exception as e:
            return Response({'status':'ERROR','message':str(e)},status=400)    








class RegisterView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            a = request.data['roles']
            lst = ast.literal_eval(a)
            serializer.is_valid(raise_exception=True)
            user = self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"status":'SUCCESS',"message": "Verification e-mail sent."}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)
            

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # complete_signup(self.request._request, user,
        #                 allauth_settings.EMAIL_VERIFICATION,
        #                 None)
        return user
    


