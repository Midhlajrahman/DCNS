from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Contact,Service,Updates,Faq,
    Enquiryform,Client,Testimonial
    )
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Contact)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("image_preview" ,"title", "is_service")
    exclude = ("creator",)
    prepopulated_fields = {"slug": ("title",)}

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:50px;height:50px;object-fit:contain;">'
            )
        return None
    
    image_preview.short_description = "Image Preview"


@admin.register(Updates)
class UpdatesAdmin(admin.ModelAdmin):
    list_display = ("image_preview" ,"title", "is_updates")
    exclude = ("creator",)
    prepopulated_fields = {"slug": ("title",)}

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:50px;height:50px;object-fit:contain;">'
            )
        return None
       
    image_preview.short_description = "Image Preview"


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("title", )
    exclude = ("creator",)

class EnquiryformAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name" )
    readonly_fields = ['service']

admin.site.register(Enquiryform, EnquiryformAdmin)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("image_preview" ,"title")
    exclude = ("creator",)
    prepopulated_fields = {"slug": ("title",)}

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:50px;height:50px;object-fit:contain;">'
            )
        return None
       
    image_preview.short_description = "Image Preview"

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_position', 'content')
    search_fields = ('author_name', 'author_position', 'content')
