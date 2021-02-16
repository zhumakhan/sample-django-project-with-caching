"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls

from .users.views import ObtainAuthToken

api_url_patterns = [
    path(route='users/', view=include('core.users.urls')),
    path(route='stream/', view=include('core.stream.urls')),
    path(route='payment/', view=include('core.payment.urls')),
    path('auth-token/',view=ObtainAuthToken.as_view()),
    path(route='docs/', view=include_docs_urls(title='api documentation')),
]
urlpatterns = [
    path('admin/v1/', admin.site.urls),
    path(route='api/v1/', view=include(api_url_patterns)),
]
