from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

CONDITION = (
    ('bn', "Brand-new"),
    ('sh', "Second-hand")
)

SCHOOL = (
    ('RSU', "Rivers State University"),
)

TYPE = (
    ("room", 'RM'),
    ("hostel", "HOS"),
    ("self-contain", "CON"),
    ("flat", "FLA",),
)

STATUS = (
    ("For rent", "For rent"),
    ("Female roommate needed", 'Female roommate needed'),
    ("Male roommate needed", 'Male roommate needed'),  
    
)


class House(models.Model):
    address = models.CharField(max_length=60, default='', null=True, blank=True)
    status = models.CharField(max_length=60, choices=STATUS)
    typ = models.CharField(max_length=20, choices=TYPE)
    price = models.CharField(max_length=20,)
    school = models.CharField(max_length=20, choices=SCHOOL) 
    pic1 = models.ImageField(upload_to='house_pics')
    pic2 = models.ImageField(upload_to='house_pics', null=True, blank=True)
    pic3 = models.ImageField(upload_to='house_pics', null=True, blank=True)
    pic4 = models.ImageField(upload_to='house_pics', null=True, blank=True)

    def __str__(self):
        return self.status


class School(models.Model):
    name = models.CharField(max_length=20, choices=SCHOOL, default='bn')
    street = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.name


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    school = models.ManyToManyField(School)
    name = models.CharField(max_length=60, )
    phone = models.IntegerField(default=234,)
    whatsapp = models.IntegerField(default=234)
    site = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to='shop_pics')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Shop(user=user)
        profile.save()


class Product(models.Model):
    name = models.CharField(max_length=60)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    description = models.TextField(null=True)
    condition = models.CharField(max_length=20, choices=CONDITION, default='bn')
    quantity = models.IntegerField(default=0)
    pic1 = models.ImageField(upload_to='product_pics')
    pic2 = models.ImageField(upload_to='product_pics', null=True, blank=True)
    pic3 = models.ImageField(upload_to='product_pics', null=True, blank=True)
    pic4 = models.ImageField(upload_to='product_pics', null=True, blank=True)
    pic5 = models.ImageField(upload_to='product_pics', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.description)
        super(Product, self).save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=60)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    charge = models.TextField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='service_pics', null=True, blank=True)
    pic1 = models.ImageField(upload_to='service_pics', null=True, blank=True)
    pic2 = models.ImageField(upload_to='service_pics', null=True, blank=True)
    pic3 = models.ImageField(upload_to='service_pics', null=True, blank=True)
    pic4 = models.ImageField(upload_to='service_pics', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    customer = models.CharField(max_length=18)
    title = models.CharField(max_length=20)
    content = models.TextField()
    dp = models.ImageField(upload_to="review_dp", null=True)
    photo = models.ImageField(upload_to='review_pics', null=True, blank=True)
    photo1 = models.ImageField(upload_to='review_pics', null=True, blank=True)
    photo2 = models.ImageField(upload_to='review_pics', null=True, blank=True)
    photo3 = models.ImageField(upload_to='review_pics', null=True, blank=True)
    photo4 = models.ImageField(upload_to='review_pics', null=True, blank=True)
    photo5 = models.ImageField(upload_to='review_pics', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review_detail', args=[self.slug])


class Request(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField()
    ref_pic = models.ImageField(upload_to='request_pics', null=True, blank=True)
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

