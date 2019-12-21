"""bookstore_project URL Configuration"""


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # User account management(login, logout, signup etc)
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('users.urls')),

    # local app(html,css,js pages or templates)
    path('',include('pages.urls')),
]
