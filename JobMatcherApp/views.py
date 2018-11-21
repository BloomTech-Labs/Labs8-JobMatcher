from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from JobMatcherApp.models import Employer, Seeker
from . import serializers


@swagger_auto_schema(methods=['get'],
                     responses={200: openapi.Response('Seeker or Employer profile', serializers.ProfileSerializer)})
@api_view(http_method_names=['GET'])
def me(request):
    """Returns representation of the authenticated user profile (Seeker or Employer) making the request."""

    if request.user.is_seeker:
        serializer = serializers.SeekerSerializer(instance=request.user.seeker)
    else:
        serializer = serializers.EmployerSerializer(instance=request.user.employer)

    return Response(data=serializer.data)


@swagger_auto_schema(methods=['post'], request_body=serializers.SignupSeekerSerializer)
@api_view(http_method_names=['POST'])
@permission_classes([])
def signup_seeker(request):
    """Signs up a Seeker and returns an access and refresh JSON web token pair"""

    serializer = serializers.SignupSeekerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)


@swagger_auto_schema(methods=['post'], request_body=serializers.SignupEmployerSerializer)
@api_view(http_method_names=['POST'])
@permission_classes([])
def signup_employer(request):
    """Signs up a Employer and returns an access and refresh JSON web token pair"""

    serializer = serializers.SignupEmployerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)


class SeekerViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.SeekerSerializer
    queryset = Seeker.objects.all()


class EmployerViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = serializers.EmployerSerializer
    queryset = Employer.objects.all()


from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)
