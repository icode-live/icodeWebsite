###
# SETTINGS ::..
##
import os

# You must either define the environment variable DJANGO_SETTINGS_MODULE
# or call settings.configure() before accessing settings.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from settings import *

###
# VIEWS ::..
##
#from django.http import HttpResponse
from django.shortcuts import render

## -- home
def home(request):
    return render(request, 'home/index.html')

def inspiration(request):
    return render(request, 'home/inspiration.html')

## -- concept
def concept(request):
    return render(request, 'concept/index.html')

## -- tools
def tools(request):
    return render(request, 'tools/index.html')

def console(request):
    return render(request, 'tools/console.html')

def vim(request):
    return render(request, 'tools/vim.html')

def git(request):
    return render(request, 'tools/git.html')

## -- learn
def learn(request):
    return render(request, 'learn/index.html')

## -- practice
def practice(request):
    return render(request, 'practice/index.html')

###
# URLS ::..
##
from django.conf.urls import url


urlpatterns = (  # '',
        ## -- home
        url(r'^$', home, name="home"),
        ## -- concept
        url(r'^concept/', concept, name="concept"),
        ## -- tools
        url(r'^tools/', tools, name="tools"),
        ## -- learn
        url(r'^learn/', learn, name="learn"),
        ## -- practice
        url(r'^practice/', practice, name="practice")
)


###
# tests
##
def test_hello_world():
    assert "hello_world" == "hello_world"

###
# WSGI ::..
##

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()

if __name__ == "__main__":
    import sys

    from django.core.management import execute_from_command_line


    execute_from_command_line(sys.argv)
