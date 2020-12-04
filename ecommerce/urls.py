"""ecommerce URL Configuration

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
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings

from users import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),

    # user
    path('profile/', csrf_exempt(user_view.User_Profile), name="user_profile"),
    path('login/', csrf_exempt(user_view.User_Login), name="login"),
    path('logedout/', csrf_exempt(user_view.User_Logout), name="logout"),
    path('register/', csrf_exempt(user_view.User_Register), name="register")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
