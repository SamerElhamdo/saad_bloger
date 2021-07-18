from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

from django.dispatch import receiver


from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField





from django.utils.translation import gettext_lazy as _




STATUS = (
    (0,_("Draft")),
    (1,_("Publish"))
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name= _("title"))
    slug = models.SlugField(max_length=200, allow_unicode=True, null=True, blank=True, verbose_name= _("slug"))
    img = models.ImageField(upload_to='images/',  verbose_name= _("img"))
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', verbose_name= _("author"), default=1)
    updated_on = models.DateTimeField(auto_now= True, verbose_name= _("updated_on"))
    content = RichTextUploadingField(verbose_name= _("content"))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name= _("created_on"))
    status = models.IntegerField(choices=STATUS, default=0, verbose_name= _("status"))

    class Meta:
        ordering = ['-created_on']
        verbose_name = _('Post')
        verbose_name_plural = _('posts')

        

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

@receiver(models.signals.post_delete, sender=Post)
def remove_file_from_s3(sender, instance, using, **kwargs):
	instance.img.delete(save=False)


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name= _("title"))
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name= _("slug"))
    img = models.ImageField(upload_to='images/',  verbose_name= _("img"))
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_books', verbose_name= _("author"), default=1)
    writer = models.CharField(max_length=200, unique=True, verbose_name= _("writer"))
    updated_on = models.DateTimeField(auto_now= True, verbose_name= _("updated_on"))
    descrption = models.TextField(verbose_name= _("descrption"))
    file_pdf = models.FileField(upload_to='books/',  verbose_name= _("file_pdf"))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name= _("created_on"))

    class Meta:
        ordering = ['-created_on']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

        

    def __str__(self):
        return self.title


class Telawa(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name= _("title"))
    img = models.ImageField(upload_to='images/',  verbose_name= _("img"))
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name= _("slug"))
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_Telawa', verbose_name= _("author"), default=1)
    updated_on = models.DateTimeField(auto_now= True, verbose_name= _("updated_on"))
    youtube_url = models.TextField(verbose_name= _("youtube_url"))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name= _("created_on"))
    status = models.IntegerField(choices=STATUS, default=0, verbose_name= _("status"))

    class Meta:
        ordering = ['-created_on']
        verbose_name = _('Telawa')
        verbose_name_plural = _('Telawas')

        

    def __str__(self):
        return self.title