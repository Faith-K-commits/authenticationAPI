from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import User, Organisation
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user_data = UserSerializer(user).data
        return Response({
            "status": "success",
            "message": "Registration successful",
            "data": {
                "accessToken": str(refresh.access_token),
                "user": user_data
            }
        }, status=status.HTTP_201_CREATED)
    return Response({
        "status": "Bad request",
        "message": "Registration unsuccessful",
        "statusCode": 400,
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise ValueError("Invalid password")
        refresh = RefreshToken.for_user(user)
        return Response({
            "status": "success",
            "message": "Login successful",
            "data": {
                "accessToken": str(refresh.access_token),
                "user": {
                    "userId": user.userId,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "email": user.email,
                    "phone": user.phone
                }
            }
        }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({
            "status": "Bad request",
            "message": "Authentication failed",
            "statusCode": 401
        }, status=status.HTTP_401_UNAUTHORIZED)
    except ValueError:
        return Response({
            "status": "Bad request",
            "message": "Authentication failed",
            "statusCode": 401
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_record(request, user_id):
    # Get the user
    user = get_object_or_404(User, userId=user_id)

    """
    Check if the requesting user is either the user themselves
    or belongs to the organizations the user is part of
    """
    if user == request.user or Organisation.objects.filter(users=request.user).exists():
        serializer = UserSerializer(user)
        return Response({
            "status": "success",
            "message": "User record retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "status": "failure",
            "message": "You do not have permission to view this user."
        }, status=status.HTTP_403_FORBIDDEN)
