from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, OrganisationSerializer
from .models import User, Organisation
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # This triggers the CustomUserManager.create_user method
        refresh = RefreshToken.for_user(user)  # Generate JWT token for the user
        user_data = UserSerializer(user).data  # Serialize user data for response
        return Response({
            "status": "success",
            "message": "Registration successful",
            "data": {
                "accessToken": str(refresh.access_token),  # Access token for authentication
                "user": user_data  # Serialized user data
            }
        }, status=status.HTTP_201_CREATED)
    return Response({
        "status": "Bad request",
        "message": "Registration unsuccessful",
        "errors": serializer.errors,
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
    try:
        print(f"Attempting to find user with userId: {user_id}")
        user = get_object_or_404(User, userId=user_id)
        print(f"User found: {user}")
    except User.DoesNotExist:
        print("User not found")
        return Response({
            "detail": "User not found",
            "code": "user_not_found"
        }, status=status.HTTP_404_NOT_FOUND)

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
        print("Permission denied")
        return Response({
            "status": "failure",
            "message": "You do not have permission to view this user."
        }, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_organisations(request):
    user = request.user
    organisations = user.organisations.all()
    serializer = OrganisationSerializer(organisations, many=True)

    return Response({
        "status": "success",
        "message": "Organisations retrieved successfully",
        "data": {
            "organisations": serializer.data
        }
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_organisation_record(request, org_id):
    organisation = get_object_or_404(Organisation, orgId=org_id)
    if request.user.organisations.filter(orgId=org_id).exists():
        serializer = OrganisationSerializer(organisation)
        return Response({
            'status': 'success',
            'message': 'Organisation details retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "status": "error",
            "message": "You do not have permission to view this organisation",
        }, status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_organisation(request):
    serializer = OrganisationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'message': 'Organisation created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'status': 'Bad Request',
            'message': 'client error',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_to_organisation(request, org_id):
    # Retrieve organisation by orgId
    organisation = get_object_or_404(Organisation, orgId=org_id)
    # Retrieve the user by userId from the request body
    user_id = request.data.get('userId')
    user = get_object_or_404(User, userId=user_id)

    # Add the user to the organisation's users
    organisation.users.add(user)
    # Save the organisation to update the database
    organisation.save()
    # Return a success response
    return Response({
        'status': 'success',
        'message': 'user added to organisation successfully',
    }, status=status.HTTP_200_OK)
