from django.shortcuts import render
from .models import TeamMember

# Create your views here.
def TitlePageView(request):
    return render(
        request,
        'TitlePage.html'
    )

def AboutUsPageView(request):
    teammembers = TeamMember.objects.all()
    return render(
        request,
        'AboutUsPage.html',
        context={
            'teammembers': teammembers,
        }
    )