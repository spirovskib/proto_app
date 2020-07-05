from application.forms import Post_Submission_Form
from application.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from settings.constants import MAX_RESIZE_WIDTH

from PIL import Image
import io



# Create your views here.

def home_view(request, *args, **kwargs):  
    #return HttpResponse("<h1>Home Page</h1>") 
    posts = Post.objects.filter(post_active=True).order_by('-post_published_date')
    context = {
        'posts' : posts,
    }
    return render(request, "home.html", context)

def post_detail_view(request, slug):  
    post = Post.objects.get(post_url = slug)
    #return HttpResponse("<h1>Home Page</h1>") 
    context = {
        'post':post,
    }
    return render(request, "view.html", context)

def new_post_view(request, *args, **kwargs):  
    if request.method == 'POST' : 
        submission_form = Post_Submission_Form(request.POST,request.FILES)
        if submission_form.is_valid():
            instance = submission_form.save(commit=False) #this seems to work for saving the user... 
            #resizing of input image
            if instance.post_image_1:
                image = Image.open(instance.post_image_1)
                w,h=image.size
                if w > MAX_RESIZE_WIDTH or h > MAX_RESIZE_HEIGHT:
                    ratio = w/h
                    if ratio > 1:
                        resize_height = int(MAX_RESIZE_WIDTH/ratio)
                        resize_width = MAX_RESIZE_WIDTH
                    else:
                        resize_width = int(ratio/MAX_RESIZE_HEIGHT)
                        resize_height = MAX_RESIZE_HEIGHT
                    image = image.resize((resize_width, resize_height), Image.ANTIALIAS)
                    image_file = io.BytesIO()
                    image.save(image_file, 'JPEG', quality=95)
                    instance.post_image_1.file=image_file
            #resizing of input image
            instance.save()
            url_link = instance.post_url
            return redirect('post_detail', url_link) 
    else:   
        submission_form = Post_Submission_Form()
    context = {
        'submission_form' : submission_form,
    }
    return render(request, "new.html", context)

