from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Custom account routes (register, profile)
    path('accounts/', include('accounts.urls')),

    # Built-in auth routes (login, logout, password reset)
    path('accounts/', include('django.contrib.auth.urls')),

    # Blog pages
    path('blog/', include('blog.urls')),

    # Root URL also loads blog
    path('', include('blog.urls')),
]

# Serve uploaded media files in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)