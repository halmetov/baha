"""it_site URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from it_site import settings
from main.views import indexHandler, aboutHandler, serviceHandler, service_listHandler, service_detailHandler, \
    blogHandler, blog_detailHandler, priceHandler, faqHandler, shopHandler, shop_detailHandler, contactHandler, \
    Handler404, applicationHandler, cartHandler, chekHandler

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),

    path('', indexHandler),
    path('about/', aboutHandler),
    path('service/', serviceHandler),
    path('service-list/', service_listHandler),
    path('service-detail/<int:detail_id>/', service_detailHandler),
    path('blog/', blogHandler),
    path('blog/<int:blog_detail_id>/', blog_detailHandler),
    path('price/', priceHandler),
    path('faq/', faqHandler),
    path('error/', Handler404),
    path('shop/', shopHandler),
    path('shop/<int:product_id>/', shop_detailHandler),
    path('contact/', contactHandler),
    path('application/', applicationHandler),
    path('cart/', cartHandler),
    path('chek/', chekHandler),
]
