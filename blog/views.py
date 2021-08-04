from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import BlogAuthor, Blog
# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage
from datetime import date

dummy = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sit amet velit vel massa pellentesque aliquet quis quis urna. Donec efficitur aliquam neque quis luctus. Ut efficitur nisi neque, at condimentum ex efficitur id. Nulla sit amet est et ex iaculis dictum. Quisque vulputate et ipsum eu interdum. Aenean placerat enim et scelerisque porta. Quisque eget ultrices nibh. Nam semper dapibus eleifend. Vestibulum ut eros leo. Nam pellentesque non est at luctus. In ac semper quam.

Nulla quam lacus, blandit iaculis nisi mattis, pretium interdum neque. Donec mollis, tortor at posuere efficitur, justo quam faucibus dui, vitae faucibus urna magna non risus. Fusce eu dictum metus, et sodales velit. Vivamus leo mauris, elementum in lorem eu, iaculis cursus mi. Aliquam ante ipsum, varius ac dapibus quis, accumsan sed nibh. Pellentesque condimentum ligula a tincidunt feugiat. Cras sit amet eros eget nibh varius egestas. Nulla facilisis lorem eget ante sollicitudin pulvinar. Sed blandit nisi eu tellus bibendum, vitae malesuada sapien molestie. Nam id lectus convallis, blandit felis ut, rhoncus felis."""

def index(request):
	'''for i in range(20):
		name = "dummy"+str(i)+str(i*i)
		user = User.objects.create_user(name,name+"@mail.com","dummy"+str(i)+str(i))
		user.save()
		bAuth = BlogAuthor(user=user,bio="This is"+name+"I am a blog author")
		bAuth.save()
		for i in range(4):
			blog = Blog(name=name, author = bAuth,description = "This is"+name+"I am a blog author. Should have entered lorem ipsum")
			blog.save()
	'''
	
	return render(request,'index.html')


def view(request):
	allBlogs = Blog.objects.all().order_by('-post_date')	
	context = {'data':allBlogs}
	return render(request,'view.html',context)

def getBloggers(request):
	allBloggers = BlogAuthor.objects.all().order_by('user__username')
	context = {'data':allBloggers}
	return render(request,'blogger.html',context)

@login_required
def getBlog(request, blog_id):
	blog = Blog.objects.get(id__exact = blog_id)
	context = {'data':blog}
	return render(request,'BlogPage.html',context)

@login_required	
def getBloggerProfile(request,blogger_id):
	blogger = BlogAuthor.objects.get(id__exact = blogger_id)
	blogs = Blog.objects.filter(author__id = blogger_id)
	blogs = blogs.order_by('-post_date')
	context = {'data':blogger,'author':blogs}
	return render(request,'BloggerProfile.html',context)
	
	
def getlogin(request):
	return render(request,'login.html')
	
def trylogin(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		
		password = request.POST.get('password','')
		#user = BlogAuthor.objects.filter(user__username__exact = username)
		user = authenticate(request,username = username,password = password)
		if user is not None:
			login(request,user)
			print(user.is_authenticated)
			return redirect('/blog')
			
	return redirect('/loginpage')
	

@login_required
def loggingout(request):
	auth.logout(request)
	return redirect('/blog')
	
@login_required
def getadmin(request):
	pass
	
	