# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from sblog.views import blog_list

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.blog_show', name='blog_article'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'sblog.views.blog_list',name='blog_list'), # 首页
    url(r'^bloglist/$','sblog.views.blog_list',name='blog_list'),
    url(r'^article/(?P<slug>[-\w]+)/$','sblog.views.blog_show',name='blog_article'), # 博文
    url(r'^category/(?P<slug>[-\w]+)/$','sblog.views.category',name='blog_category'), # 分类
    url(r'^tag/(?P<id>\d+)/$','sblog.views.tag',name='blog_tag'), # 标签

)


