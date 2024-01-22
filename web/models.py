from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    image = models.ImageField(upload_to="services/img/")
    description = RichTextField(blank=True, null=True)
    is_service = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    is_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "service"
        verbose_name_plural = "services"

    def get_absolute_url(self):
        return reverse("web:service_details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Updates(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="web/images/update/")
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=100, blank=True, null=True)
    is_updates = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    is_create = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed.

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "Updates"
        verbose_name_plural = "Updates"

    def save(self, *args, **kwargs):
        # Auto set author if not provided
        if not self.author_id:
            self.author = User.objects.first()
        # Auto generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(Updates, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("web:update_details", kwargs={"slug": self.slug})

    def _str_(self):
        return self.title


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
    )
    message = models.TextField()
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return str(self.full_name())

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Faq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.title


class Enquiryform(models.Model):
    service = models.CharField(max_length=100, editable=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.services}  "


class Client(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="web/images/client/")

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    author_position = models.CharField(max_length=100)
    avatar_image = models.ImageField(upload_to="web/images/testimonial/")

    def __str__(self):
        return f"Testimonial from {self.author_name}"
