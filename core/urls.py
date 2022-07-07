from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from basics import views
from rest_framework import routers
from basics.views import T1ViewSet, T2ViewSet, T3ViewSet


router = routers.DefaultRouter()
router.register(r't1', T1ViewSet)
router.register(r't2', T2ViewSet)
router.register(r't3', T3ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]
