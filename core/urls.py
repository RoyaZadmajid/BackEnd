from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from django.views.generic.base import RedirectView
from happiness.views import TeamHappinessStatics

urlpatterns = [
    url('admin/', admin.site.urls),

    # API Urls
    url(r'^api/logout/', RedirectView.as_view(pattern_name='logout', permanent=False), name='home'),
    url(r'^api/v1/happiness_level/', TeamHappinessStatics.as_view(), name='team_happiness_level_api'),
]
