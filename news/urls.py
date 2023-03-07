from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *
urlpatterns = [
    path('contact/', contact, name='contact'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/',user_logout, name='logout'),
    # path('', index, name='home'),
    # path('',cache_page(60) (HoneNews.as_view()), name='home'),
    path('', HoneNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add_news/', add_news, name='add_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),

]
