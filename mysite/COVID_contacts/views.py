from django.http import HttpResponse


def index(request):
    return HttpResponse("testujemy gita ajeee 222 <p>ssss</p>")