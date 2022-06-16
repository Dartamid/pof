from django.shortcuts import get_object_or_404, render
from .models import ItemType, Item


def ItemsListView(request):
    itemtypes = ItemType.objects.all()
    return render(
        request,
        'ItemsListPage.html',
        {
            'itemtypes': itemtypes,
        }
    )


def ItemDetailView(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(
        request,
        'ItemDetailPage.html',
        {
            'item': item,
        }
    )
