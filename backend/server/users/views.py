from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from adventures.models import Adventure, Collection
from .serializers import CustomUserDetailsSerializer
from users.models import CustomUser
from .serializers import ChangeEmailSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.conf import settings
from adventures.serializers import AdventureSerializer, CollectionSerializer

class ChangeEmailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ChangeEmailSerializer,
        responses={
            200: openapi.Response('Email successfully changed'),
            400: 'Bad Request'
        },
        operation_description="Change the email address for the authenticated user."
    )
    def post(self, request):
        serializer = ChangeEmailSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            new_email = serializer.validated_data['new_email']
            user.email = new_email
            # remove all other email addresses for the user
            user.emailaddress_set.exclude(email=new_email).delete()
            user.emailaddress_set.create(email=new_email, primary=True, verified=False)
            user.save()
            return Response({"detail": "Email successfully changed."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IsRegistrationDisabled(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response('Registration is disabled'),
            400: 'Bad Request'
        },
        operation_description="Check if registration is disabled."
    )
    def get(self, request):
        return Response({"is_disabled": settings.DISABLE_REGISTRATION, "message": settings.DISABLE_REGISTRATION_MESSAGE}, status=status.HTTP_200_OK)
    
class PublicUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: openapi.Response('List of public profiles'),
            400: 'Bad Request'
        },
        operation_description="List all users with public profiles."
    )
    def get(self, request, pk=None):
        if pk:
            try:
                user = CustomUser.objects.get(pk=pk, public_profile=True)
                serializer = CustomUserDetailsSerializer(user)
                data = serializer.data
                if 'email' in data:
                    del data['email']

                # get all public adventures for the user
                adventures = Adventure.objects.filter(user_id=user, is_public=True)
                serializer = AdventureSerializer(adventures, many=True)
                data['adventures'] = serializer.data

                # get all public collections for the user
                collections = Collection.objects.filter(user_id=user, is_public=True)
                serializer = CollectionSerializer(collections, many=True)
                data['collections'] = serializer.data

                return Response(data, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response({"error": "User not found or profile is not public."}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = CustomUser.objects.filter(public_profile=True)
            serializer = CustomUserDetailsSerializer(users, many=True)
            for user in serializer.data:
                if 'email' in user:
                    del user['email']
            return Response(serializer.data, status=status.HTTP_200_OK)