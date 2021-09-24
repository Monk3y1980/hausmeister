from django.core.validators import RegexValidator
from django.db import models


class ContactPrice(models.Model):
    """
    Create repair request
    """
    # steckdose = 'Steckdose installieren'
    # kabel_verlegen = 'Kabel verlegen'
    # select = 'Wählen Sie aus...'
    # Repairs = [(steckdose, 'Steckdose installieren'), (kabel_verlegen, 'Kabel verlegen'), ('select', 'Wählen Sie aus...')]
    # to_repair = models.CharField(max_length=30, choices=Repairs, default='select', verbose_name='Тема')
    name = models.CharField('name', max_length=120)
    email = models.EmailField('email', max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=16, blank=True)  # Validator soll eine Liste sein
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField('nachricht', help_text='max. 500 Zeichen')

    class Meta:
        verbose_name = 'reparaturanfrage'
        verbose_name_plural = 'reparaturanfragen'
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}: {self.message} {self.created}'


class Slider(models.Model):
    """
    Slider
    """
    name = models.CharField('name', max_length=32, help_text='maximal 32 Zeichen')
    title = models.CharField('überschrift', max_length=64, help_text='maximal 64 Zeichen')
    text = models.CharField('beschreibung', max_length=254, help_text='maximal 254 Zeichen')
    image = models.ImageField('bild', upload_to='images/slider', help_text='maximale Bildauflösung 1920x600px')

    class Meta:
        verbose_name = 'slider'

    def __str__(self):
        return self.name


class TestimonialsCarousel(models.Model):
    first_name = models.CharField('vorname', max_length=254, help_text='maximal 254 Zeichen')
    last_name = models.CharField('nachname', max_length=254, help_text='maximal 254 Zeichen')
    image = models.ImageField('avatar', upload_to='images/carousel', help_text='maximale Bildauflösung 47x47px')
    testimonial = models.TextField('referenz', max_length=500, help_text='maximal 500 Zeichnen')

    def __str__(self):
        return f'Referenz von: {self.image} {self.last_name} {self.first_name} {self.testimonial}  '


class Team(models.Model):
    """
    Team
    """
    avatar = models.ImageField('foto', upload_to='images/team', help_text='maximale Bildgröße 370x370px')
    first_name = models.CharField('vorname', max_length=200)
    last_name = models.CharField('nachname', max_length=200)
    job = models.CharField('beruf', max_length=64)

    class Meta:
        verbose_name = 'mitarbeiter'
        verbose_name_plural = 'mitarbeiter'


class Social(models.Model):
    """ Social accounts"""
    icon = models.FileField('icon', upload_to='icons/', help_text='maximale Bildgröße 18x18')
    name = models.CharField('social netzwerk', max_length=200)
    link = models.URLField('social url')

    class Meta:
        verbose_name = 'social account'
#        verbose_name_plural = 'social accounts'

    def __str__(self):
        return f'Account: {self.name}'
