from django.shortcuts import redirect, render
from blogs.models import Category,Blog
from linkMedia.models import About 
from.forms import registrationForm
def home(request):
    featured_post=Blog.objects.filter(is_featured=True,status="Published").order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status="Published")
    try:
        about=About.objects.get()
    except:
        about=None
        
    context={
      'featured_post':featured_post,
      'posts':posts,
      'about':about



    }
    return render (request,'home.html',context)

def register(request):
    if request.method=='POST':
        form=registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
       form=registrationForm()
    context={
        'form':form
    }
    return render(request,'register.html',context)

