from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/blog', views.index, name='index'),
    path('admin', views.index, name='getadmin'),
	path('blogs',views.view, name='view'),
	path('blogs/?page=<int:page_no>',views.view, name='view'),
	path('blogger',views.getBloggers, name='getBloggers'),
	path('blogger/',views.getBloggers, name='getBloggers'),
	path('blogger/blogs/<int:blog_id>',views.getBlog, name='getBlog'),
	path('blogs/<int:blog_id>',views.getBlog,name='getBlog'),
	path('blogger/<int:blogger_id>',views.getBloggerProfile,name='getBloggerProfile'),
	path('loginpage',views.getlogin,name='getlogin'),
	path('try-login',views.trylogin,name='trylogin'),
	path('loggingout',views.loggingout,name='loggingout')
	
	
]
