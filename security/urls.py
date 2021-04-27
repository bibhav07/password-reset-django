
from django.contrib import admin
from django.urls import path
from .views import mainpg, loginpg,  logoutUser, signuppg

#
from django.contrib.auth import views as auth_views

# #static
# static files import
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpg, name="mainpg"),
    path('login/', loginpg, name="loginpg"),
    path('logout/', logoutUser, name="logout"),
    path('signup/', signuppg, name="signup"),
    #
    # reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registrations/step1_password_reset.html"),
         name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registrations/step2_password_email_send.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="registrations/step3_password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registrations/step4_password_reset_complete.html"),
         name="password_reset_complete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
