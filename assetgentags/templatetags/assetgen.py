import json

from django import template
from settings import ASSETS_JSON

register = template.Library()

def use(p, func):
  with open(p) as f:
    return func(f)

register.simple_tag(lambda x: use(ASSETS_JSON, json.load)[x], name="load_asset")
