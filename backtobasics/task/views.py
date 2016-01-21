from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def tasks(request):
	template = 'task/index.html'
	context = {}
	return render(request,template,context)
