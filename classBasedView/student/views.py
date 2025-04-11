from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,CreateView,UpdateView,TemplateView
from .forms import StudentForm
from .models import Student
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@method_decorator(login_required,name='dispatch')
class Dashboard(TemplateView):
  template_name = 'auth/home.html'


# Create your views here.
@method_decorator(login_required,name='dispatch')
class StudentCreateView(View):

  def get(self,request):
      print(request.user)
      form = StudentForm()
      return render(request,'student/userCreate.html',{'user':form})

  def post(self,request):
    form = StudentForm(request.POST)
    if form.is_valid(): 
      student = form.save(commit=False)  
      student.set_password(form.cleaned_data['password'])
      # print(form.cleaned_data['password'])
      student.user = request.user  
      student.save()
  
      return redirect('student_list',id = request.user.id)

    return render(request,'student/userCreate.html',{'user':form})  
  
@method_decorator(login_required,name='dispatch')
class StudentDetailViews(View):  
    
    def get(self,request,id):
      student = Student.objects.filter(user= id)
      paginator = Paginator(student,3)
      page_num = request.GET.get('page')
      page_obj = paginator.get_page(page_num)
      return render(request,'student/userGet.html',{'user':page_obj})
  

@method_decorator(login_required,name='dispatch')
class StudentDeleteView(View):

  def get(self,request,user_id):
      student = get_object_or_404(Student,id = user_id)
      return render(request,'student/user_confirm_delete.html',{'user':student})

  def post(self,request,user_id):
    student = get_object_or_404(Student,id = user_id)
    id = student.user.id
    student.delete()
    return redirect('student_list',id = id)
  
@method_decorator(login_required,name='dispatch')
class StudentUpdateView(View):

  def get(self,request,user_id):
      student = get_object_or_404(Student,id = user_id)
      form = StudentForm(instance=student)
    
      return render(request,'student/userUpdate.html',{'user':form})

  def post(self,request,user_id):
    student = get_object_or_404(Student,id = user_id)
    form = StudentForm(request.POST,instance=student)
    if form.is_valid():
      student = form.save(commit=False)   
      student.user = request.user  
      student.set_password(form.cleaned_data['password'])
      student.save()
  
      return redirect('student_list',id = request.user.id)


    return render(request,'student/userCreate.html',{'user':form})   

















#----------------------------------------------------------------------

class StudentListGenricView(ListView  ):
  model = Student
  template_name = 'student/userGet.html'
  context_object_name = 'user'

class StudentCreateGenricView(CreateView):
  model = Student
  form_class = StudentForm
  template_name = 'student/userCreate.html'
  # success_url = reverse_lazy('student_list')  
  success_url = reverse_lazy('student_list')
  # context_object_name = 'user'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['user'] = self.get_form()
    return context
  
  # def form_valid(self, form):
  #       # Save the form (new student)
  #       self.object = form.save()

  #       # Redirect to the student list after successful form submission
  #       return redirect('student_list') 


class StudentCreateGenricView(UpdateView):
  model = Student
  form_class = StudentForm
  template_name = 'student/userUpdate.html'
  # success_url = reverse_lazy('student_list')  
  success_url = reverse_lazy('student_list')
  # context_object_name = 'user'  


