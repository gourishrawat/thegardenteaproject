from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('infor/',views.infor),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)