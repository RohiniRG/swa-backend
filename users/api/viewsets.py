from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from users.api.serializers import registerSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer

@api_view(["POST"])
def register_user(request):
    """
    Response object for the api is created if the data obtained serializers is successfully validated
    """
    serializer = registerSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data["response"] = "User registered successfully!"
        data["email"] = user.email
        data["username"] = user.username
        data["mobile_no"] = str(user.mobile_no)
        token = Token.objects.get(user=user).key
        data["token"] = token
        response = {
            "success": True, 
            "data": data
        }
    else:
        data = serializer.errors
        response = {
            "success": "False", 
            "data": data
        }

    return Response(
        response, 
        status=status.HTTP_200_OK
    )


@api_view(["POST"])
def login_user(request):
    """
    Modifying the obtain_auth_token method present in rest_framework.authtoken.views to create a custom response
    """
    serializer_class = AuthTokenSerializer
    serializer = serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    token, created = Token.objects.get_or_create(user=user)
    response = {
        "success": True, 
        "token": token.key
    }
    return Response(
        response, 
        status=status.HTTP_200_OK
    )


@api_view(["POST"])
def logout_user(request):
    request.user.token.delete()
    return Response(
        "User Logged out successfully"
    )


@api_view(["POST"])
def period_data(request):
    """
    This method is used to store the period data of the user
    """
    data = request.data
    user = request.user
    user.cycleDays = data["cycleDays"]
    user.cycleLength = data["cycleLength"]
    user.lastCycleStart = data["lastCycleStart"]
    user.save()
    return Response(
        "Period data saved successfully"
    )


@api_view(["GET"])
def get_period_data(request):
    """
    This method is used to get the period data of the user
    """
    user = request.user
    response = {
        "cycleDays": user.cycleDays,
        "cycleLength": user.cycleLength,
        "lastCycleStart": user.lastCycleStart
    }
    return Response(
        response, 
        status=status.HTTP_200_OK
    )

@api_view(['PATCH'])
def update_period_data(request):
    """
    This method is used to update the period data of the user
    """
    data = request.data
    user = request.user
    user.cycleDays = data["cycleDays"]
    user.cycleLength = data["cycleLength"]
    user.lastCycleStart = data["lastCycleStart"]
    user.save()
    return Response(
        "Period data updated successfully"
    )

@api_view(['POST'])
def add_user_interest(request):
    """
    This method is used to add the interest of the user
    """
    data = request.data
    user = request.user
    user.interests.add(data["interest"])
    user.save()
    return Response(
        "Interest added successfully"
    )

@api_view(['GET'])
def get_user_interest(request):
    """
    This method is used to get the interest of the user
    """
    user = request.user
    response = {
        "interests": user.interests.all()
    }
    return Response(
        response, 
        status=status.HTTP_200_OK
    )

