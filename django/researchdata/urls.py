from django.urls import path
from . import views
from .apps import app_name

app_name = app_name

urlpatterns = [
    # Stories
    path('stories/', views.StoryListView.as_view(), name='story-list'),
    path('stories/<pk>/', views.StoryDetailView.as_view(), name='story-detail'),
    # Resources
    path('resources/<slug:slug>/', views.ResourceStrandDetailView.as_view(), name='resourcestrand-detail'),
    path('resources/feedback/create/', views.resource_feedback_create, name='resource-feedback-create'),
]
