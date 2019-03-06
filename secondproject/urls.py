"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import blog.views
from django.conf import settings
from django.conf.urls.static import static
#아래 두줄은 media사용하려면 필수로 import해줘야할것임

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/<int:blog_id>', blog.views.detail, name='detail'),
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create', blog.views.create, name="create"),
    path('blog/portpolio/', blog.views.portpolio, name="portpolio"),
    path('accounts/', include('accounts.urls')),
    path('blog/newblog/', blog.views.blogpost, name="newblog"),
    path('accounts/', include('allauth.urls')), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# 맨아래줄 media파일 사용하려면 추가해줘하함
