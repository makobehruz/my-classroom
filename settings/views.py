from django.shortcuts import render
from django.views import View


class SettingsListView(View):
    def get(self, request):
        return render(request,'settings/settings.html')

