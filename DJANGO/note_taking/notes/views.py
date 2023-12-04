from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))
def index2(request):
    template = loader.get_template("index2.html")
    return HttpResponse(template.render({}, request))