# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from sblog.models import Blog,Category,Tag,ClientInfo
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def blog_list(request):
    blog_list = Blog.objects.all()

    paginator = Paginator(blog_list,4)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    # 访客数据采集
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip=""
    client_info = ClientInfo()
    client_info.ip_address=regip
    client_info.save()

    return render_to_response("blog_list.html",{"blogs":blogs,"categories":categories,"tags":tags})

def blog_show(request,slug):
    try:
        blog = Blog.objects.get(slug=slug)
        categories = Category.objects.all()
        tags = Tag.objects.all()
    except Blog.DoesNotExit:
        raise Http404
    return render_to_response("blog_show.html",{"blog":blog,'slug':slug,"categories":categories,"tags":tags})

def category(request,slug):
    cut_category = get_object_or_404(Category,slug=slug)
    blogs = cut_category.blog_set.all() #查找符合条件的所有文章  #Blog.objects.filter(category=cut_category)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render_to_response("blog_list.html",{"blogs":blogs,"categories":categories,"tags":tags})

def tag(request,id=''):
    cut_tag = Tag.objects.get(id=id)
    blogs =cut_tag.blog_set.all() #查找符合条件的所有文章
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render_to_response("blog_list.html",{"blogs":blogs,"categories":categories,"tags":tags})

