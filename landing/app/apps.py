from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = 'Adminpanel'

    # нам надо переопределить метод ready,
    # чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import app.signals
