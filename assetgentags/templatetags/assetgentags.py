import json

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

register = template.Library()

def use(p, func):
  with open(p) as f:
    return func(f)

register.simple_tag(lambda x: use(settings.ASSETS_JSON, json.load)[x], name="load_asset")