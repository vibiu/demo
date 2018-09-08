from django.http import HttpResponse
from django.shortcuts import render

from .models import IdcInfo
# from django.template import loader

# Create your views here.


def index(request):
    return HttpResponse('hello world')


def section(request):
    is_virtual_list = IdcInfo.objects.all()
    # import pdb
    # pdb.set_trace()
    context = {'is_virtual_list': is_virtual_list}
    context = {'is_virtual_list': [
        choice for choice in IdcInfo.virtual_choice]}
    return render(
        request, "polls/index.html", context)


def section_post(request):
    import pdb
    pdb.set_trace()
    return HttpResponse('hi')


def ajax(request):
    return HttpResponse('hello')


def html(request):
    return render(request, "pools/ajaxttest.html")
