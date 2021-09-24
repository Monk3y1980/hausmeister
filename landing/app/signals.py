from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives
# from django.http import HttpResponse
# from django.shortcuts import redirect
from django.template.loader import render_to_string
# from django.core.mail import mail_admins

from .models import ContactPrice


@receiver(post_save, sender=ContactPrice)
def contact(instance, created, **kwargs):
    if created:
        admin_msg = EmailMultiAlternatives(
            subject='Eine neue Reparaturanfrage über Homepage',
            from_email=settings.SERVER_EMAIL,
            to=settings.ADMINS[0],
        )
        body = render_to_string('app/admin_repair_mail.html', {
            'name': instance.name,
            'email': instance.email,
            'message': instance.message,
            'to_repair': instance.to_repair,
            'phone': instance.phone,
        }
                            )

        admin_msg.attach_alternative(body, 'text/html')
        admin_msg.send()

        client_msg = EmailMultiAlternatives(
            subject=f'Hallo {instance.name}!',
            from_email=settings.SERVER_EMAIL,
            to=[instance.email],
        )
        body = render_to_string('app/client_mail.html', {
            'msg': 'Vielen Dank für Ihre Anfrage. Wir werden uns schnellstmöglich darum kümmern.'
        }
                            )

        client_msg.attach_alternative(body, 'text/html')
        client_msg.send()


