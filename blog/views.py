from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')

def situation(request):
	return render(request, 'blog/situation.html')

def gender(request):
	return render(request, 'blog/gender.html')

def relation(request):
	return render(request, 'blog/relation.html')

def age(request):
	return render(request, 'blog/age.html')

def price(request):
	return render(request, 'blog/price.html')

def content(request):
	return render(request, 'blog/content.html')

def contact(request):
	return render(request, 'blog/contact.html')

def name(request):
	return render(request, 'blog/name.html')
