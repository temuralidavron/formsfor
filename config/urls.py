
from django.contrib import admin
from django.urls import path
from app.views import author, author_list, ProfileFamilyMemberCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', author, name='author'),
    path('author/list', author_list, name='profile-list'),
    path('author/create/', ProfileFamilyMemberCreate.as_view(), name='author-list'),

]
