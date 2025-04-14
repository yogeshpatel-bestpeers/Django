from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

def custom_login_required(function=None):
    print("decorator called")
    
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            print(request)
            user = getattr(request, 'user', None)
            if user is None or request.user.is_authenticated:                               
                redirect_to = reverse('custom_login') 
                return HttpResponseRedirect(redirect_to)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    if function:
        return decorator(function)
    return decorator
