# from django.views.generic.base import View
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from api.scraper import get_updated_users

class UsersAPIView(APIView):
    def get(self, request):
        return Response({"users": get_updated_users()})