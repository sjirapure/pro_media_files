from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.views import View

# Create your views here.
class AddEmployee(View):
    template_name ='app1/addemp.html'
    form  =EmployeeForm
    def get(self,request):
        form = self.form()
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request):
        form = self.form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        context={'form':'form'}
        return render(request,self.template_name,context)
    
class ShowEWmployee(View):
    template_name = 'app1/showemp.html'
    def get(self,request):
        obj = Employee.objects.all()
        context={'obj':obj}
        return render(request,self.template_name,context)
    
class UpdateEmployee(View):
    template_name ='app1/addemp.html'
    form  =EmployeeForm
    def get(self,request,id):
        obj = Employee.objects.get(id=id)
        form = self.form(instance=obj)
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request,id):
        obj = Employee.objects.get(id=id)
        form = self.form(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        context={'form':'form'}
        return render(request,self.template_name,context)
    
class DeleteEmployee(View):
    template_name = 'app1/deleteemp.html'
    def get(self,request,id):
        obj = Employee.objects.get(id=id)
        context ={'obj':obj}
        return render(request,self.template_name,context)
    def post(self,request,id):
        obj = Employee.objects.get(id=id)
        obj.delete()
        return redirect("show_url")
        context ={'obj':obj}
        return render(request,self.template_name,context)
        
        
        
    
    
    
        
        