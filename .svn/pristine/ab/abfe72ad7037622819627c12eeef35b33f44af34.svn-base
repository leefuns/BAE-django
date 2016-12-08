#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class MetaInfo(models.Model):
    web_keywords = models.CharField(max_length=150,verbose_name='网站关键字')
    web_description = models.CharField(max_length=200,verbose_name='网站描述')

    class Meta:
        verbose_name = '网站信息'

    def __unicode__(self):
        return self.web_keywords

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='标题')
    img = models.ImageField(default="uploads/default.jpg",upload_to='uploads/%Y-%m-%d', verbose_name='图片')
    author = models.CharField(max_length=10, verbose_name='作者',default='Lee')
    desc = models.CharField(max_length=255, verbose_name='描述')
    content = models.TextField(verbose_name='文章内容')
    publish_time = models.DateTimeField(verbose_name='发布时间')
    # category = models.ForeignKey(blank=True, null=True, verbose_name='分类')

    class Meta:
        verbose_name = '文章发布'

    def __unicode__(self):
        return self.title