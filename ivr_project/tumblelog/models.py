# -*- coding: utf-8 -*-
import datetime
from flask import url_for
from tumblelog import db


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name=u"Комментарий", required=True)
    author = db.StringField(verbose_name=u"Имя, Абитуриент (Лицеист)", max_length=255, required=True)


class Post(db.DynamicDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    slug = db.StringField(max_length=255, required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    @property
    def post_type(self):
        return self.__class__.__name__

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class Title_Main(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст", required=True)


class BlogPost_Main(Post):
    body = db.StringField(verbose_name=u"Текст",required=True)
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    image_url = db.StringField(verbose_name=u"URL картинки")


class BlogPost_About(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)
    image_url = db.StringField(verbose_name=u"URL картинки", max_length=255)


class BlogPost_Napr(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)
    image_url = db.StringField(verbose_name=u"URL картинки", max_length=255)


class BlogPost_Exams(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)
    image_url = db.StringField(verbose_name=u"URL картинки", max_length=255)


class Video_Video(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    embed_code = db.StringField(verbose_name=u"URL видео", required=True)


class BlogPost_Telegram(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)


class BlogPost_Advices(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)
    body1 = db.StringField(verbose_name=u"Текст", required=True)
    body2 = db.StringField(verbose_name=u"Текст", required=True)
    body3 = db.StringField(verbose_name=u"Текст", required=True)
    image_url = db.StringField(verbose_name=u"URL картинки", max_length=255)


class BlogPost_Events(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)
    image_url = db.StringField(verbose_name=u"URL картинки", max_length=255)


class BlogPost_Day(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)
    image_url = db.StringField(verbose_name=u"URL картинки", max_length=255)


class BlogPost_Properties(Post):
    title = db.StringField(verbose_name=u"Заголовок", max_length=255, required=True)
    body = db.StringField(verbose_name=u"Текст",required=True)
    body1 = db.StringField(verbose_name=u"Текст", required=True)
    body2 = db.StringField(verbose_name=u"Текст", required=True)
    body3 = db.StringField(verbose_name=u"Текст", required=True)
    body4 = db.StringField(verbose_name=u"Текст", required=True)
    image_url = db.StringField(verbose_name=u"URL картинки", max_length=255)









