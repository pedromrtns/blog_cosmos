#from django.contrib import admin
#from django.urls import path
#from galeria.views import index

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', index),
#]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
