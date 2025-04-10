from django.shortcuts import render
from django.views import View
from student.models import Student
from django.core.paginator import Paginator

# Create your views here.

class StudentListView(View):
  

  def get(self,request):
    student = Student.objects.all()
    paginator = Paginator(student,3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request,'page/page.html',{'page_obj':page_obj})


