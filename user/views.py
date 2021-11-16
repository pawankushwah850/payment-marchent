from rest_framework import parsers, renderers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from user.serializers import CustomAuthTokenSerializer, UserSingupSerializer, UserProfileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from .models import User


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class UserSignup(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSingupSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)


class UserProfile(ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user_id = self.request.user.pk
        if user_id:
            return User.objects.filter(pk=user_id)
        return User.objects.all()

    @action(methods=['POST', 'GET', "PUT", 'DELETE'], detail=False)
    def updateKycDocument(self):
        pass
