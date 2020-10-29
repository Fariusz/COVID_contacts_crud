from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('COVID/', include('COVID_contacts.urls')),
    path('admin/', admin.site.urls),
]