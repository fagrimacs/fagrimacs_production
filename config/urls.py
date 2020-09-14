from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('fagrimacs-admin/', admin.site.urls),
    path('', include('mains.urls', namespace='mains')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', include('admins.urls', namespace='admins')),
    path('farmer/', include('farmers.urls',namespace='farmers')),
    path('owner/', include('owners.urls', namespace='owners')),
    path('expert/', include('experts.urls', namespace='experts')),
    path('equipment/', include('equipments.urls', namespace='equipments')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)