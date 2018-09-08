from django.http import HttpResponse

from .model import User


def index(request):
    response = HttpResponse('helloworld')
    user = User.objects.create(username='user', password='password')
    return HttpResponse('user:{}'.format(user.username))
    return response
