"""
URL configuration for ModelsOrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework_simplejwt import views as jwt_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('data1.urls')),
    path('social/', include('post_drf.urls')),
    path('auth/', include('BasicAuth.urls')),
    # path('tk/', include('TokenAuth.urls')),
    path('sess/', include('SessionAuth.urls')),
    path('oauth/', include('OAuth.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('jwt/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'), 
    path('jwt/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'), 
    path('jwt/', include('jwtToken.urls')),
]