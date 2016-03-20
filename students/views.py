from django.shortcuts import render
from django.http import HttpResponse


def my_first_page(request):
	return HttpResponse('this is my first page')