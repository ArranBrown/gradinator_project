"""gradinator_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import reverse
from registration.backends.simple.views import RegistrationView

from gradinator import views


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')


urlpatterns = [
                  url(r'^$', views.home, name='home'),
                  url(r'gradinator/$', views.home, name='home'),
                  # any further urls that start with gradinator/ will be dealt with by the gradinator app
                  url(r'^gradinator/', include('gradinator.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^accounts/', include('registration.backends.simple.urls')),
                  url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
