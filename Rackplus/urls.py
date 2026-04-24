
from django.contrib import admin
from django.urls import path,include

handler404 = 'app.views.erro_404_view'
handler500 = 'app.views.erro_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
