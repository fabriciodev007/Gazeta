from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.http import HttpRequest, HttpResponse


def requer_premium(view_func):
    @wraps(view_func)
    def _wrapped_view(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())

        if getattr(request.user, 'plano_atual', None) != 'PREMIUM':
            from django.shortcuts import render
            return render(request, 'assinatura.html', {
                'mensagem': 'Este conteúdo é exclusivo para usuários Premium.'
            })

        return view_func(request, *args, **kwargs)

    return _wrapped_view
