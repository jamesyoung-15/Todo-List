from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLogin, RegisterUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='userlogin'),
    path('logout/', LogoutView.as_view(next_page='userlogin') ,name='logout'),
    path('register/', RegisterUser.as_view() ,name='register'),
    path('', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='taskdetail'),
    path('taskcreate', TaskCreate.as_view(), name='taskcreate'),
    path('taskupdate/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>/', TaskDelete.as_view(), name='taskdelete'),
]