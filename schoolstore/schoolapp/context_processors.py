from . models import Stream
def menu_links(request):
    links=Stream.objects.all()
    return dict(links=links)