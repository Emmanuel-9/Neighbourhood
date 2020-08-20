from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('business/', views.business, name='business'),
    path('posts/', views.post, name='posts'),
    path('reg_business/', views.BusinessCreateView.as_view(), name='register-business'),
    path('reg_hood/', views.HoodCreateView.as_view(), name='register-hood'),
    path('neighbourhood/<int:pk>/', views.HoodDetailView.as_view(), name='neighbourhood-detail'),
    path('neighbourhood/<int:pk>/delete/', views.HoodDeleteView.as_view(), name='delete-neighbourhood'),
    path('neighbourhood/<int:pk>/update/', views.HoodUpdateView.as_view(), name='update-neighbourhood'),
    path('business/<int:pk>/', views.BusinessDetailView.as_view(), name='business-detail'),
    path('business/<int:pk>/update/', views.BusinessUpdateView.as_view(), name='update-business'),
    path('business/<int:pk>/delete/', views.BusinessDeleteView.as_view(), name='delete-business'),
    path('create_post/', views.PostCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('admin_pr/', views.admin_profile, name='admin-profile')

]