from django.shortcuts import render,redirect
from .forms import imageupload
from .models import image
from django.contrib import messages
# Create your views here.

def image_upload(request): 
    if request.method =='POST':
        form= imageupload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your! Image was Upload')
            return redirect('gallery')
    else:
        form = imageupload()
        img = image.objects.all()
    return render(request,'image_upload.html' ,{'img': img, 'form': form})


def gallery(request): 
    img = image.objects.all()
    return render(request, 'gallery.html' ,{'img': img})


def deleteItem(request, pk):
    form = image.objects.get(id = pk)
    form.delete()
    return redirect('gallery')



from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import HttpResponse
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def image_crousel(request):
    return render(request, 'image_crousel.html')

def navbar(request):
    return render(request, 'navbar.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password')
        password2=request.POST.get('password1')
        user = User.objects.create_user(username,email,password1)
        if not User.objects.filter(username=username,email=email):
            messages.success(request, 'You Already Have Account! Login Now')
            return redirect('signup')

        elif not User.objects.filter(username=username):
            messages.success(request, 'Name is Already Taken!')
            return redirect('signup')
        else:
            user.save()
            return redirect('login')
    return render(request , 'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        
        if User.objects.filter(email=username,password = password):
            return render(request,'index.html', {'username':username, 'password': password})
       
        user=authenticate(username=username,password=password)
        if user is not None:
            username=user.username
            password =user.password
            return render(request,'index.html', {'username':username, 'password': password})
        else:
            messages.success(request, 'Please Login Your Username User Not Found!')
        
        
    return render(request , 'login.html')

