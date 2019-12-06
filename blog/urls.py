from django.urls import path
from  .views import PostList, PostDetail, UserDetail, UserList

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('PostList', PostList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]