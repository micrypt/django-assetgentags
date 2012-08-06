import json

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    from settings import ASSETS_JSON
except:
    raise ImproperlyConfigured("Please specify an ASSETS_JSON path in your settings")

register = template.Library()

def use(p, func):
  with open(p) as f:
    return func(f)

register.simple_tag(lambda x: use(ASSETS_JSON, json.load)[x], name="load_asset")
