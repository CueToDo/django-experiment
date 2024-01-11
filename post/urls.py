from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='post-home'),
    path('account', views.account_page, name="post-account"),
    path('about', views.about_page, name='post-about'),
    path('logout-post', views.logout_view, name='logout-post'),
    path('single-postit/<int:post_it_id>/',
         views.single_post_it, name='single_post_it'),
    path('single-postit/<int:post_it_id>/<str:update>/',
         views.single_post_it, name='single_post_it'),  # same name as above
    path('delete-postit/<int:post_it_id>/',
         views.delete_post_it, name='delete_post_it'),

]
