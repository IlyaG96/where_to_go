from django.http import HttpResponse
from django.template import loader


def index_page(request):
    template = loader.get_template('index_page.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

