from django.shortcuts import render,redirect    
from django.views import View
from django.views.generic import TemplateView
from .forms import UserForm
from .models import User

# Create your views here.

class Registration(View):

    def get(self,request):
        form = UserForm()
        return render(request,'auth/signup.html',{'form':form})
    
    def post(self,request):
        form = UserForm(request.POST)

        if form.is_valid():
            
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])
            user.save()
            print('hii')
            return redirect('/account/login/')
            

        return render(request,'auth/signup.html',{'form':form})
    
class Login(View):

    def get(self,request):
        print('login')
        form = UserForm()
        return render(request,'auth/login.html',{'form':form})    
    
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
            return redirect('auth/login.html')

class LogoutView(View):
    def get(self, request):
        print(request.session['user_id'])
        if 'user_id' in request.session:
            print('logout Sucess')
            del request.session['user_id']
        return redirect('/account/login/')        
            
    
class Profile(View):

    def get(self,request):
        print("is user valid  : ",request.user)
        if request.user and request.user.is_authenticated:
            template_name = 'custom/profile.html' 
            return render(request,template_name,{'user':request.user})   
        else:
            return redirect('/account/login/') 