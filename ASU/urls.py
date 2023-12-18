from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('as_admin',views.admin_login,name="admin_login"),
    path('as_academic',views.academic_login,name="academic_login"),
    path('admin_user/',include('admin_user.urls')),
    path('academic_user/',include('academic_user.urls')),

    path('enrolmentnumber_check/<str:no>',views.enrolmentnumber_check,name="enrolmentnumber_check"),
    #path('enrolmentnumber_check>',views.enrolmentnumber_check,name="enrolmentnumber_check"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

