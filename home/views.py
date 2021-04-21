from django.shortcuts import render

# Create your views here.
from django.views import View
from home.models import Post, PostDescription, AboutMe, HomeImages


class Home(View):
    def get(self, request):
        home_images = HomeImages.objects.filter().order_by('-created_at')
        print(home_images)
        posts = Post.objects.filter().order_by('-created_at')[:10]
        context = {
            'home_images': home_images,
            'posts': posts
        }
        return render(request=request, template_name='home.html', context=context)


class PostDescriptionView(View):
    def get(self, request, slug):
        post = Post.objects.filter(slug=slug).first
        post_description = PostDescription.objects.get(post=post)
        return render(request=request, template_name='post-description.html',
                      context={'post': post, 'post_description': post_description})


class Contact(View):
    def get(self, request):
        return render(request=request, template_name='contact.html')


class About(View):
    def get(self, request):
        about_me = AboutMe.objects.filter().last()
        return render(request=request, template_name='about-me.html', context={"about":about_me})
