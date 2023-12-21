from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from pages.views import contact_page_view, home_page_view

app_name = 'pages'

urlpatterns = [
    path('contact/', contact_page_view, name='contact'),
    path('', home_page_view, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
