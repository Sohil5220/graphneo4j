"""graphGG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from graphapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("see_nodes/", views.see_nodes, name="see_nodes"),
    path("", include("graphapp.urls")),  # include() already handles routing, so no need for a regex here
    path("", views.index, name="index"),
]
