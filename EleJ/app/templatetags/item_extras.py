#ページング機能（次のページに引き継ぎ）

#こうやって使うらしい笑

from django import template

register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
