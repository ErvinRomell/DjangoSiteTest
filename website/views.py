from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
	return render(request,'website/index.html')
def about_view(request):
	return HttpResponse('<h1>about us</h1>')
def contact_view(request):
	return HttpResponse('<h1>contact us</h1>')