from django.urls import path,include
from . import views
urlpatterns = [
    path('openaccount/', views.OpenAccount.as_view(), name='openaccount'),
    path('is_activeate/<uid64>/<token>/', views.is_activeate, name='is_activeate'),
    path('useraccount/<int:id>/', views.UserAccount.as_view(), name='useraccount'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]