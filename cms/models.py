from django.db import models
from django.template.defaultfilters import slugify



class WebsiteSetting(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo")
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        return self.title


class Slider(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.heading} {self.sub_heading}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    author = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog")
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        """ Overriding save method of Super Model """
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs) # save object



class FAQs(models.Model):
    question=models.CharField(max_length=255)
    answer=models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name  = "FAQ"
        verbose_name_plural  = "FAQs"


class Contact(models.Model):
    """model class of contect page"""
    name=models.CharField(max_length=40)
    mobile=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()
    

    def __str__(self):
        return self.name
    
class About(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
    imag=models.ImageField(upload_to='About')
    status = models.BooleanField(default=True)

    


    def __str__(self):
        return self.title

