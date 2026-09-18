from django.views.generic import TemplateView

class IdexView(TemplateView):
    template_name = 'index.html'

class AssinarView(TemplateView):
    template_name= 'assinatura.html'
    
class ContatView(TemplateView):
    template_name = 'contato.html'