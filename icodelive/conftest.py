import os
import sys


sys.path.append(os.path.dirname(__file__))

# You must either define the environment variable DJANGO_SETTINGS_MODULE
# or call settings.configure() before accessing settings.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_settings")
