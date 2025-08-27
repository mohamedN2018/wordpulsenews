from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import gettext
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path
from django.views.i18n import set_language

urlpatterns = [
    # هذا خارج i18n_patterns، لتفعيل تبديل اللغة
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    re_path('accounts/', include('accounts.urls'), name='accounts'),
    path('i18n/setlang/', set_language, name='set_language'),

    path("", include("main_core.urls")),
    path("contact/", include("contact.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
