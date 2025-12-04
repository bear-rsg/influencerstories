from django.urls import path
from . import views

app_name = 'general'

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('insights/', views.InsightsTemplateView.as_view(), name='insights'),
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies')
]
