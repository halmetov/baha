from django.db import models
from phone_field import PhoneField


# Create your models here.

class Carusel(models.Model):
    title = models.CharField(max_length=300)
    mini_title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class BestService(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title




class Service(models.Model):
    title = models.CharField(max_length=300)
    mini_description = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='upload')
    is_main = models.BooleanField(blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

class Recovery(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.IntegerField(default=0,blank=True)
    rating = models.IntegerField(default=0, blank=True)
    recovery_id = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title



class ServiceProcess(models.Model):
    title = models.CharField(max_length=300)
    is_in_service = models.BooleanField(blank=True)
    description = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title



class About(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class About_action(models.Model):
    title = models.CharField(max_length=300, blank=True)
    action = models.ForeignKey(About, on_delete=models.CASCADE, blank=True)


    def __str__(self):
        return self.title



class About_service(models.Model):
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title




class Staff(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    is_experienced = models.BooleanField(blank=True)
    logo = models.ImageField(upload_to='upload')
    facebook = models.CharField(max_length=300, blank=True)
    gmail = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    old_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    rating = models.IntegerField(default=0.0, blank=True)
    mini_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    is_main = models.BooleanField()
    is_related = models.BooleanField()
    status = models.IntegerField(default=0, blank=True)


    def __str__(self):
        return self.title




class Productcomment(models.Model):
    text = models.TextField(max_length=1000, blank=True)
    name = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, default='', blank=True)
    rating = models.FloatField(default=0.0, blank=True)
    date = models.DateTimeField(blank=True)
    comment_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='upload', blank=True, default='')

    def __str__(self):
        return self.name




class Feedback(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    quantities = models.IntegerField(default=0, blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=300)
    main_description = models.CharField(max_length=300)
    more_description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='upload')
    category = models.CharField(max_length=300, blank=True)
    date = models.DateField()
    is_latest = models.BooleanField(blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    gmail = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title


class BlogQoute(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    description = models.TextField()
    action = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.first_name



class Blogcomment(models.Model):
    text = models.TextField(max_length=1000, blank=True)
    name = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, default='', blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number', max_length=31)
    rating = models.FloatField(default=0.0, blank=True)
    date = models.DateTimeField(blank=True)
    comment_id = models.IntegerField(default=0)
    blog_id = models.IntegerField(default=0, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True, default='')

    def __str__(self):
        return self.name




class Price(models.Model):
    title = models.CharField(max_length=300)
    mini_title = models.CharField(max_length=300, blank=True)
    price = models.IntegerField(default=0)
    quality1 = models.CharField(max_length=300, blank=True)
    quality2 = models.CharField(max_length=300, blank=True)
    quality3 = models.CharField(max_length=300, blank=True)
    quality4 = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title




class Faq(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title





class Contact(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    info = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=300, blank=True)
    country = models.CharField(max_length=300, blank=True)
    bin = models.IntegerField(default=0, blank=True)
    weekday1 = models.CharField(max_length=300, blank=True)
    weekday2 = models.CharField(max_length=300, blank=True)
    time1 = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    time2 = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    email = models.EmailField(max_length=300, blank=True)
    icon = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title





class ContactPost(models.Model):
    first_name = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, default='', blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number', max_length=31)
    message = models.TextField(blank=True)
    rating = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return self.first_name









class ClientSays(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0, blank =True)
    rating = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.first_name


class Brand(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload')


    def __str__(self):
        return self.title



class Information(models.Model):
    need_recovery_title = models.CharField(max_length=300, blank=True)
    need_recovery_text = models.TextField(max_length=300, blank=True)
    request_name = models.CharField(max_length=300, blank=True)
    request_text = models.TextField(max_length=300, blank=True)
    contact_address = models.CharField(max_length=300, blank=True)
    phone = models.IntegerField(default=0, blank=True)
    footer_theme = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    gmail = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    service_right_title = models.CharField(max_length=300, blank=True)
    service_right_description = models.TextField(blank=True)
    blog_right_title = models.CharField(max_length=300, blank=True)
    blog_right_description = models.TextField(blank=True)

    def __str__(self):
        return self.need_recovery_title

