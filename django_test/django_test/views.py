from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed


def hello_view(request):
    if request.method == "GET":
        name: str = request.GET.get("name", None)
        message: str = request.GET.get("message", None)
        if not name:
            return HttpResponseBadRequest(f'Name must be set')
        if not message:
            return HttpResponseBadRequest(f"Message must be set")
        return HttpResponse(f"Hello {name}! {message}!")
    else:
        return HttpResponseNotAllowed()