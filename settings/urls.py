from django.urls import path

from . import views


app_name = 'settings'

urlpatterns = [
    path('list/', views.SettingsListView.as_view(), name='list'),
]