from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

router = DefaultRouter(trailing_slash=True)
router.register('seekers', views.SeekerViewSet, base_name='seeker')
router.register('employers', views.EmployerViewSet, base_name='employer')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    # JWT: Signin using email and password
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Signup and profile info
    path('signup/seeker/', views.signup_seeker, name='signup_seeker'),
    path('signup/employer/', views.signup_employer, name='signup_employer'),
    path('me/', views.me, name='me'),
    path(r'^secret$', views.secret_page, name='secret'),
    #0auth accounts path
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('allauth.urls')),

    # view sets
    path('', include(router.urls)),
]
