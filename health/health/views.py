from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import subprocess

def git_hash():
   """
       Use git client to obtain latest commit hash for main branch and returns it
   """
   hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
   return hash

def app_name(request):
   """
       Return django app name to caller
   """
   appname = request.resolver_match.app_name
   return appname

@api_view(['GET'])
def git_view(request):
   data = {
      "git hash": git_hash(),
      "app name": app_name(request),
      "app version": "ZZZZ"
   }
   return Response(data)
