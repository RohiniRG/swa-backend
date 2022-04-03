from django.urls import path
from content.api.viewsets import GetAllContentView, CreateContentView, UpdateContentView

app_name = "content"

urlpatterns = [
    path("get_all_content/", GetAllContentView.as_view(), name="get_all_content"),
    path("get_all_content/<int:pk>", GetAllContentView.as_view(), name="get_all_content"),
    path("create_content/", CreateContentView.as_view(), name="create_content"),
    path("update_content/<int:pk>", UpdateContentView.as_view(), name="update_content"),
]
