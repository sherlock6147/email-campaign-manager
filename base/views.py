from django.shortcuts import render

# Create your views here.
def home(request):
    email_count = 0
    context = {}
    context['email_count']= email_count
    return render(request,'base/index.html',context)

def about(request):
    return render(request,'base/about.html')

def contact(request):
    return render(request,'base/contact.html')