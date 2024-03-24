from django import template

from carts import utils
from carts.models import Cart

register=template.Library()

@register.simple_tag()
def user_carts(request):
    return utils.get_user_carts(request)
