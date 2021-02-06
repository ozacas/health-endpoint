from rest_framework.decorators import api_view
from rest_framework.response import Response
import subprocess


def run(cmd, shell=False):
    """
    Wrapper around subprocess to handle exceptions
    """
    try:
        stdout = subprocess.check_output(
            cmd, shell=shell, stderr=subprocess.DEVNULL
        ).strip()
        return stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "n/a"


def git_hash():
    """
    Use git client to obtain latest commit hash for main branch and returns it
    """
    hash = run(["git", "rev-parse", "HEAD"])
    return hash


def app_name():
    """
    Return django app name to caller
    """
    appname = run("basename -s .git `git config --get remote.origin.url`", shell=True)
    return appname


def git_most_recent_tag():
    """
    Return the most recent git release tag associated with the repo and return to caller
    """
    version = run("git describe --exact-match --abbrev=0", shell=True)
    return version


@api_view(["GET"])
def git_view(request):
    """
    Implement a function-based view using Django REST framework. Really simple implementation.
    """
    data = {
        "git hash": git_hash(),
        "app name": app_name(),
        "app version": git_most_recent_tag(),
    }
    return Response(
        data, content_type="application/json"
    )  # explicit content_type rather than negotiated
