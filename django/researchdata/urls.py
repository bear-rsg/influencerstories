from django.urls import path
from . import views
from .apps import app_name

app_name = app_name

urlpatterns = [
    # Stories
    path('stories/', views.StoryListView.as_view(), name='story-list'),
    path('stories/<pk>/', views.StoryDetailView.as_view(), name='story-detail'),
    # Resources
    path('resources/education/', views.ResourceEducationListView.as_view(), name='resource-education-list'),
    path('resources/policy/', views.ResourcePolicyListView.as_view(), name='resource-policy-list'),
    path('resources/mensmentalhealth/', views.ResourceMensMentalHealthListView.as_view(), name='resource-mensmentalhealth-list'),
    path('resources/feedback/create/', views.resource_feedback_create, name='resource-feedback-create'),
]
