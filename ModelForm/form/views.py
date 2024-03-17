from django.shortcuts import render, redirect

from .forms import StudentForm

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def contact(request):

    return render(request, 'contact.html')


def create_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
        
    else:
        form = StudentForm()

    return render(request, 'create_student.html', {'form' : form} )
