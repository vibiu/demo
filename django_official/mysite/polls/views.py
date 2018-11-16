from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import IdcInfo
from .forms import UploadFileForm
from .util.upload import handle_uploaded_file
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


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.cleaned_data.get('title', 'test')
            handle_uploaded_file(filename, request.FILES['file'])
            return HttpResponse('success.')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
    return HttpResponse('hello')
