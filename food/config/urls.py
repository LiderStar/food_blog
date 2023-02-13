from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('contact.urls')),
    path('', include('blog.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)