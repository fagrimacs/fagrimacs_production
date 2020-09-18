from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('admin/', include('admins.urls', namespace='admins')),
    path('farmer/', include('farmers.urls',namespace='farmers')),
    path('owner/', include('owners.urls', namespace='owners')),
    path('equipment/', include('equipments.urls', namespace='equipments')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
