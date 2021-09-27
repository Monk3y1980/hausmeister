from django import template
from ..models import Social, Team, Slider, TestimonialsCarousel


register = template.Library()


#     @register.simple_tag()
# def get_social_links():
#     """
#     Display of social links networks
#     """
#     return Social.objects.all()


@register.simple_tag()
def get_team():
    """
    Display Team
    """
    return Team.objects.all()


@register.simple_tag()
def get_slider_images():
    """
    Header Slider
    """
    return Slider.objects.all()


@register.simple_tag()
def get_testimonials_items():
    """
    Display Testimonials
    """
    return TestimonialsCarousel.objects.all()