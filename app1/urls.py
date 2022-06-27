from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'app1'
urlpatterns = [
    
    path('', views.home, name='home'),

    path('index', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('enter_book/', views.enter_book, name='enter_book'),

    # path('book_details/<int:pk>', views.book_details, name='book_details'),
    path('get_all_books/', views.get_all_books, name='get_all_books'),
    path('list/', views.list, name='list'),
    path('save_update_book/<str:pk>/', views.save_update_book, name='save_update_book'),

    path('update_book/<str:pk>/', views.update_book, name='update_book'),
    path('create_user/', views.create_user, name='create_user'),
    path('login_view/', views.login_view, name="login_view"),
    path('logout_view/', views.logout_view, name="logout_view"),
    path('gettoken/',obtain_auth_token),
    path('delete_book/<str:pk>/', views.delete_book, name="delete_book"),

    





]