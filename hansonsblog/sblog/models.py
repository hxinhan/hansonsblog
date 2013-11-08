# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import permalink
#from markdown import markdown
from django.template.defaultfilters import  slugify


# Create your models here.

class Category(models.Model): # 分类表

    name = models.CharField(max_length=10,verbose_name=u'名称')
    slug = models.CharField(max_length=50,unique=True,verbose_name=u'Slug')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('blog_category',None,{'slug':self.slug})


    class Meta:
        ordering = ['id']
        verbose_name_plural = verbose_name = u'分类'




class Tag(models.Model): # 标签

    tag_name = models.CharField(max_length=20,blank=True,verbose_name=u'名称')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'建立时间')

    def __unicode__(self):
        return self.tag_name

    class Meta:
        verbose_name_plural = verbose_name = u'标签'





class Blog(models.Model): # 文章

    caption = models.CharField(max_length=50,verbose_name=u'标题')
    slug = models.SlugField(max_length=50,unique=True,verbose_name=u'Slug')
    tags = models.ManyToManyField(Tag,blank=True,verbose_name=u'标签名称')
    content = models.TextField(verbose_name=u'内容')
    #content_html = models.TextField(blank=True,null=True)
    publish_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发表时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name=u'更新时间')
    counts = models.IntegerField(default=0,verbose_name=u'阅读数')
    category = models.ForeignKey(Category,verbose_name=u'分类')

    def __unicode__(self):
        return u'%s %s' % (self.caption,self.publish_time)

    @permalink
    def get_absolute_url(self):
        return ('blog_article',None,{'slug':self.slug})

    #def save(self):
    #    self.content_html = markdown(self.content,['codehilite','fenced_code'])
    #    super(Blog,self).save()

    class Meta:
        get_latest_by = 'publish_time'
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'文章'

class ClientInfo(models.Model):

    ip_address = models.CharField(max_length=20,verbose_name=u'IP地址')
    time = models.DateTimeField(auto_now=True,verbose_name=u'访问时间')

    def __unicode__(self):
        return u'%s %s' % (self.ip_address,self.time)

    class Meta:
        get_latest_by = 'time'
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'访问记录'