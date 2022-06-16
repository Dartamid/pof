from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Guide



def GuidesListView(request):
    guides = Guide.objects.all()
    return render(
        request,
        'GuidesListPage.html',
        context={
            'guides': guides,
        }
    )


def GuideDetailView(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    return render(
        request,
        'GuideDetailPage.html',
        context={
            'guide': guide,
        }
    )