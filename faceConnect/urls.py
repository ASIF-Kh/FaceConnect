from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'faceConnect'


urlpatterns = [
    path('', views.upload_individuals, name='upload_individuals'),
    path('detection/', views.detect_individuals, name='detect_individuals'),
    path('send_email/', views.send_email, name='send_email')
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path('share/', views.share_image, name='share_image'),
# path('check_status/', views.check_processing_status, name='check_processing_status'),

