from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(ContactPrice)
class ContactPriceAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['name', 'phone', 'email', 'message', 'created']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 1920px; height: 600px;"/>'.format(obj.image.url))

    image_tag.short_description = 'bild'
    list_display = ['image_tag', 'name', 'title', 'text']


@admin.register(TestimonialsCarousel)
class TestimonialsCarouselAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 47px; height: 47px;"/>'.format(obj.avatar.url))

    image_tag.short_description = 'bild'
    list_display = ['image_tag', 'first_name', 'last_name', 'testimonial']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 370px; height: 370px;"/>'.format(obj.avatar.url))

    image_tag.short_description = 'avatar'
    list_display = ['image_tag', 'first_name', 'last_name', 'job']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 18px; height: 18px;"/>'.format(obj.icon.url))

    list_display = ['name', 'image_tag', 'link']

