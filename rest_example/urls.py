"""rest_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

#from django.urls import path, include
from restapp import views
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

admin.autodiscover()

schema_view = get_swagger_view(title='My RefApp API')

urlpatterns = [
    # Examples:
    # url(r'^$', 'rest_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^user/', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^awx/', views.AWXTest.as_view()),
    #url(r'^$', schema_view),
    url(r'^api/', schema_view),
]
