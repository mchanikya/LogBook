"""LogBook URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',include('homePage.urls', namespace="Home")),
    path(r'login/',include('login.urls', namespace="login")),
    path('Me/',include('Me.urls', namespace="Me")),
    path('Academic/',include('Academic.urls', namespace="Academic")),
    path('Pics/',include('Pics.urls', namespace="Pics")),
    path('Family/',include('Family.urls', namespace="Family")),
]
