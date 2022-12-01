
from django.urls import path
from.views import (BlogListVIew,
    BlogDeteilVIew,
    BLogDeleteme,
    AddBlogView,
    BlogEditVIew,
    SignUpViEW,
                   )

urlpatterns = [
    path('', BlogListVIew.as_view(), name='home'),
    path("<int:pk>", BlogDeteilVIew.as_view(), name='post_detail'),
    path('add/', AddBlogView.as_view(), name='post_new'),
    path('<int:pk>/edit', BlogEditVIew.as_view(), name='edit_me'),
    path('<int:pk>/delete', BLogDeleteme.as_view(), name='delete_me'),
    path('signup/',SignUpViEW.as_view(),name='signup')



]
