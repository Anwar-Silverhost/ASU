from django.urls import path
from admin_user import views


urlpatterns = [
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('admin_navbar', views.admin_navbar, name='admin_navbar'),
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('admin_academic',views.admin_academic,name="admin_academic"),
    path('admin_create_academic',views.admin_create_academic,name="admin_create_academic"),
    path('save_academic',views.save_academic,name="save_academic"),
    path('admin_academic_view/<int:id>',views.admin_academic_view,name="admin_academic_view"),
    path('admin_user_registrations',views.admin_user_registrations,name="admin_user_registrations"),
    path('admin_user_reg_view/<int:id>',views.admin_user_reg_view,name="admin_user_reg_view"),
    path('admin_Update_status/<int:id>',views.admin_Update_status,name="admin_Update_status"),
    path('admin_academic_add_seat/<int:id>',views.admin_academic_add_seat,name="admin_academic_add_seat"),
    path('update_academic/<int:id>',views.update_academic,name="update_academic"),
    path('shutDown_academi/<int:id>',views.shutDown_academi,name="shutDown_academi"),
    path('restart_academi/<int:id>',views.restart_academi,name="restart_academi"),
]
