# from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.response import Response

from api.scraper import get_updated_users

class UsersAPIView(APIView):

    def get(self, request):
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('size', 10))
        region = str(request.GET.get('region', '')).lower()
        type = str(request.GET.get('type', '')).lower()

        data = get_updated_users()

        if region != '' and type != '':
            aux = []
            for user in data:
                if user['location']['region'] == region and user['type'] == type:
                    aux.append(user)
            data = aux

        if region != '' and type == '':
            aux = []
            for user in data:
                if user['location']['region'] == region:
                    aux.append(user)
            data = aux

        if region == '' and type != '':
            aux = []
            for user in data:
                if user['type'] == type:
                    aux.append(user)
            data = aux

        total = len(data)
        start = (page - 1) * page_size
        end = page * page_size

        return Response ({
            "pageNumber": page,
            "pageSize": page_size,
            "totalCount": total,
            "users": data[start:end]
        })