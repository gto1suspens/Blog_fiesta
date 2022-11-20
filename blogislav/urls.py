
from django.urls import path
from.views import BlogListVIew, BlogDeteilVIew
urlpatterns = [
    path('', BlogListVIew.as_view(), name='home'),
    path("post/<int:pk>/", BlogDeteilVIew.as_view(), name='s'),

]
