from django.views.generic import TemplateView

class IdexView(TemplateView):
    template_name = 'index.html'

class AssinarView(TemplateView):
    template_name= 'assinatura.html'
    
