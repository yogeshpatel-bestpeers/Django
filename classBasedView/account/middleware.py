class CustomAuthMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        from .models import User
        user_id = request.session.get('user_id')
        print('middleWare : ', user_id)
        if user_id:
            try:
                request.user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                request.user = None
        else:
            request.user = None
        return self.get_response(request)
