from django.shortcuts import render,redirect    
from django.views import View
from django.views.generic import TemplateView
from .forms import UserForm
from .models import User
from django.contrib import messages
from .utils import custom_login_required
from django.utils.decorators import method_decorator

# Create your views here.


class Registration(View):
    template_name = None
    @method_decorator(custom_login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get(self,request):
        form = UserForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = UserForm(request.POST)

        if form.is_valid():
            
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/account/login/')
            

        return render(request,'/auth/signup.html',{'form':form})
    
class Login(View):
    template_name = None
    

    def get(self,request):
        
        if request.user and request.user.is_authenticated:
            return redirect('/account/profile/')
            
        else:
            form = UserForm()

            return render(request,self.template_name,{'form':form})
        # 'custom/login.html'

    
    def post(self,request):


        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        user = User.objects.get(email = email)
        print('login : ',user.check_password(password))
        if user.check_password(password):
            request.session['user_id'] = user.user_id
            return redirect('/account/profile/')
            

        else :
            form = UserForm()
            messages.error(request, 'Invalid email or password')
            return render(request, self.template_name,{'form':form})

class LogoutView(View):
    def get(self, request):
        print(request.session['user_id'])
        if 'user_id' in request.session:
            print('logout Sucess')
            del request.session['user_id']
        return redirect('/account/login/')        
            
    
class Profile(View):
    template_name =None
    def get(self,request):
        print("is user valid  : ",request.user)
        if request.user and request.user.is_authenticated:
            
            return render(request,self.template_name,{'user':request.user})   
        else:
            return redirect('/account/login/') 
        


# class Singleton():
    # _instance ={}
    # def __call__(cls, *args, **kwargs):
    #     if cls not in cls._instances:
    #         instance = super().__call__(*args, **kwargs)
    #         cls._instances[cls] = instance
    #     return cls._instances[cls]

    