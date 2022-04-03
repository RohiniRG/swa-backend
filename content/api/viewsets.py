from functools import partial
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Content
from .serializers import ContentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.permissions import IsAuthenticatedAndIsStaff

class GetAllContentView(APIView):
    """
    Viewset for CRUD APIS of Content Model
    """
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        """
        Get all the contents of the user
        """
        if pk:
            try:
                content = Content.objects.get(id=pk, is_archived=False)
                serializer = self.serializer_class(content)
                response = {"success": True, "data": serializer.data}
            except:
                response = {
                    "success": "False",
                    "message": "Data invalid. Operation unsuccesful",
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            contents = Content.objects.filter(is_archived=False)
            serializer = ContentSerializer(contents, many=True)
            response = {
                "success": "True",
                "data": serializer.data
            }

        return Response(response, status=status.HTTP_200_OK)

    
class CreateContentView(APIView):
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedAndIsStaff]

    def post(self, request):
        """
        Create a new content
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            response = {"success": True, "data": serializer.data}
        else:
            response = {"success": "False", "message": serializer.errors}

        return Response(response, status=status.HTTP_200_OK)


class UpdateContentView(APIView):
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedAndIsStaff]

    def patch(self, request, pk):
        """
        Update a content
        """
        try:
            content = Content.objects.get(id=pk, is_archived=False)
            serializer = self.serializer_class(content, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {"success": True, "data": serializer.data}
            else:
                response = {"success": "False", "message": serializer.errors}
        except:
            response = {
                "success": "False",
                "message": "Data invalid. Operation unsuccesful",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)

