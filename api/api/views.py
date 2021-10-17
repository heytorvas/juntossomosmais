from rest_framework.views import APIView
from rest_framework.response import Response

from api.apps import data

class UsersAPIView(APIView):

    def get(self, request):

        # metadata from request
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('size', 10))
        region = str(request.GET.get('region', '')).lower()
        type = str(request.GET.get('type', '')).lower()

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