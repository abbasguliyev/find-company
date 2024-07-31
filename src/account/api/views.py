from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.api.serializers import UserOutSerializer
from account.api.selectors import user_list


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs) -> Response:
        data = super().post(request, *args, **kwargs)

        data = data.data

        user = user_list().last()

        user_details = UserOutSerializer(user)
        print(f"{user_details.data=}")


        user_details = UserOutSerializer(user)
        data['user_details'] = user_details.data
        return Response(data)
