from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def testing_api(request):
    if request.method == 'GET':
        return Response({'msg': 'This is inside GET request'})

    if request.method == 'POST':
        return Response({'msg': 'This is inside POST request', 'data': request.data})
