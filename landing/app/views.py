from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import FormContactPrice


class IndexView(TemplateView, FormView):
    template_name = 'app/index.html'
    success_url = reverse_lazy('home')
    form_class = FormContactPrice

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


