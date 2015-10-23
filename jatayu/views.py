from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import RequestContext, loader
# Create your views here.

def HomePage(request):
	context = {}
	#return HttpResponse("Helle there, welocme to eAll I Need!!")
	return render(request, 'jatayu/homepage.html', context)
