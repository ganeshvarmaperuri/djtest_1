from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp import forms

# Create your views here.
def EmpModelView(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = forms.EmpForm()
    return render(request, 'welcome.html',{'form':form})

def thanks(request):
    return render(request, 'thanks.html')