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

def app_name():
   """
       Return django app name to caller
   """
   appname = subprocess.check_output("basename -s .git `git config --get remote.origin.url`", shell=True).strip()
   return appname

def git_most_recent_tag():
   """
       Return the most recent git release tag associated with the repo and return to caller
   """
   version = subprocess.check_output(["git", "describe", "--exact-match", "--abbrev=0"])
   return version

@api_view(['GET'])
def git_view(request):
   """
      Implement a function-based view using Django REST framework. Really simple implementation.
   """
   data = {
      "git hash": git_hash(),
      "app name": app_name(),
      "app version": git_most_recent_tag(),
   }
   return Response(data)
