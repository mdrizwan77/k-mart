from django.shortcuts import render


# Create your views here.



def About(request):
     about_us= About.objects.all()
 
     return render(request,'about.html',{'about_us':about_us})



         
