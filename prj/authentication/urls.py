from authapp.views import index
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header='issat events'
urlpatterns = [
     path('',index, name='home'),
    path('admin/' ,admin.site.urls),
    path('auth/', include('authapp.urls'))
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

