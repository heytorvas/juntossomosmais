from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.apps import data

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class UsersAPIView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY, description="number of page", type=openapi.TYPE_INTEGER),
            openapi.Parameter('size', openapi.IN_QUERY, description="size of page", type=openapi.TYPE_INTEGER),
            openapi.Parameter('region', openapi.IN_QUERY, description="region of the user", type=openapi.TYPE_STRING),
            openapi.Parameter('type', openapi.IN_QUERY, description="category of the user", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request):

        # metadata from request
        try:
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('size', 10))
            region = str(request.GET.get('region', '')).lower()
            type = str(request.GET.get('type', '')).lower()

        except:
            return Response({"msg": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

        # manipulating loaded data from memory
        updated_users = data

        # trying filters
        if region != '' and type != '':
            aux = []
            for user in updated_users:
                if user['location']['region'] == region and user['type'] == type:
                    aux.append(user)
            updated_users = aux

        if region != '' and type == '':
            aux = []
            for user in updated_users:
                if user['location']['region'] == region:
                    aux.append(user)
            updated_users = aux

        if region == '' and type != '':
            aux = []
            for user in updated_users:
                if user['type'] == type:
                    aux.append(user)
            updated_users = aux

        # pagination
        total = len(updated_users)
        start = (page - 1) * page_size
        end = page * page_size

        return Response ({
            "pageNumber": page,
            "pageSize": page_size,
            "totalCount": total,
            "users": updated_users[start:end]
        })