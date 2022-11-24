from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .admin import Timeline,Home_Bio,About_Me,DownloadCV,Portfolio,Blogs,Link_Address,Contact


# Create your views here.

def index(request):

    queryset_Timeline= Timeline.objects.filter(featured=True)
    queryset_HomeBio= Home_Bio.objects.filter(featured=True)
    queryset_AboutMe= About_Me.objects.filter(featured=True)
    queryset_DownloadCV=DownloadCV.objects.filter(featured=True)
    queryset_portfolio=Portfolio.objects.filter(featured=True)
    queryset_Blogs=Blogs.objects.filter(featured=True)
    queryset_Link_Address=Link_Address.objects.all()

    context={
        "timelines":queryset_Timeline,
        "homebio":queryset_HomeBio,
        "aboutme":queryset_AboutMe,
        "cvlink":queryset_DownloadCV,
        "portfolios":queryset_portfolio,
        "blogs":queryset_Blogs,
        "link_address":queryset_Link_Address

    }    

    return render(request, "index.html",context)



def SaveContact(request):

    if request.method=="POST":

        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=Contact(name=name,email=email,subject=subject,message=message)
        data.save()

    return render(request, "success.html")
