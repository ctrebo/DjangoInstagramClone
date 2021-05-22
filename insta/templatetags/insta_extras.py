import itertools
from django import template
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.template.defaultfilters import stringfilter


register = template.Library()


class CycleNode(template.Node):
    def __init__(self, cyclevars):
        self.cyclevars = template.Variable(cyclevars)

    def render(self, context):
        names = self.cyclevars.resolve(context)
        if self not in context.render_context:
            context.render_context[self] = itertools.cycle(names)
        cycle_iter = context.render_context[self]
        return next(cycle_iter)

@register.tag
def cycle_list(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires an argument" % token.contents.split()[0]
        )
    node = CycleNode(arg)
    return node

@register.simple_tag
@stringfilter
def get_tagged_user(tagged_user):
    user_model = get_user_model()
    if user_model.objects.filter(username=tagged_user[1:]).count() != 0:
        user = get_object_or_404(user_model, username=tagged_user[1:])
        return reverse('user-detail', args=[str(user.id)])
    else:
        #return to custom page
        return reverse('user-dont-exist', args=[str(tagged_user[1:])])
