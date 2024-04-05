from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'app1', views.YourViewSet)  # Replace YourViewSet with your actual viewset

urlpatterns = [
    path('', views.index, name='index'),
    path('tech-category-01', views.techcategory01, name='tech-category-01'),
    path('tech-category-02', views.techcategory02, name='tech-category-02'),
    path('tech-category-03', views.techcategory03, name='tech-category-03'),
    path('tech-contact', views.techcontact, name='tech-contact'),
    path('tech-single', views.techsingle, name='tech-single'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('api/', include(router.urls)),
]
