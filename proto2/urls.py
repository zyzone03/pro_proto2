"""proto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'blog.views.index'),
    url(r'^situation/$', 'blog.views.situation'),
    url(r'^gender/$', 'blog.views.gender'),
    url(r'^relation/$', 'blog.views.relation'),
    url(r'^age/$', 'blog.views.age'),
    url(r'^price/$', 'blog.views.price'),
    url(r'^content/$', 'blog.views.content'),
    url(r'^contact/$', 'blog.views.contact'),
    url(r'^name/$', 'blog.views.name'),
]
