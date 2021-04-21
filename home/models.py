from django.db import models
from transliterate import translit
# Create your models here.
from django.utils.text import slugify

from base.models import BaseModel


class HomeImages(BaseModel):
    image = models.ImageField(upload_to="media/home/", blank=True, null=True)




class Post(BaseModel):
    title = models.CharField(max_length=255)
    small_description = models.TextField()
    image = models.ImageField(upload_to="media/post/", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.title, 'uk', reversed=True))
        print(self.slug)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostDescription(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.post}'



class Comments(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email


class AboutMe(BaseModel):
    image = models.ImageField(upload_to="media/about-me/", blank=True, null=True)
    about_me_text = models.TextField()
