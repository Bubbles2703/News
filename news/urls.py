from django.urls import path
from .views import news_list, news_detail
from .views import user_login
urlpatterns = [
    path('', news_list, name='news_list'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('login/', user_login, name='login'),
]

