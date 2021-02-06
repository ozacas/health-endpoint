from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def git_view(request):
   data = {
      "git hash": "XXX",
      "app name": "XXX",
      "app version": "ZZZZ"
   }
   return Response(data)
