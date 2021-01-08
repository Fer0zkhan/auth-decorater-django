from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# Only for Html or simple views
from AuthDecorator.decorators import is_driver
from auth_decorators.utils import success_response


@user_passes_test(is_driver)
def driver_authenticated_view(request):
    return JsonResponse(success_response())
