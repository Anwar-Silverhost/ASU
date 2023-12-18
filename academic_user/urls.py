from django.urls import path
from academic_user import views


urlpatterns = [
    path('academic_logout',views.academic_logout,name="academic_logout"),
    path('academic_navbar', views.academic_navbar, name='academic_navbar'),
    path('academic_dashboard',views.academic_dashboard,name="academic_dashboard"),  
    path('academic_registrations',views.academic_registrations,name="academic_registrations"),
    path('academic_register',views.academic_register,name="academic_register"),
    path('save_user/<int:id>',views.save_user,name="save_user"), 
    path('academic_profile',views.academic_profile,name="academic_profile"),
    path('academic_user/Profile/<int:id>',views.academic_userProfile,name="academic_userProfile"),
    path('update_user/<int:id>',views.update_user,name="update_user")
]
