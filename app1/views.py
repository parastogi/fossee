from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import answer
def home(request):
	return render(request,'app1/home.html')
def afcsti(request):
	return render(request,'app1/afcsti.html')
def quiz(request):
	return render(request,'app1/quiz.html')
def check(request):
	
	anss=request.POST.get('ans')
	print(anss)
	x=0
	tot=0;
	a="";
	for i in range(1,11):
		ans=answer.objects.get(pk=i)
		if ans==anss[x]:
			tot+=1
			a=a+str(x)
			x+=1		
	return JsonResponse({stri:a,cor:tot})

# Create your views here.
