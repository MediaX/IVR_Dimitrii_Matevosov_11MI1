from flask.views import MethodView
from flask_mongoengine.wtf import model_form


from flask import Blueprint, request, redirect, render_template, url_for

from tumblelog.auth import requires_auth

from tumblelog.models import BlogPost_Main, Title_Main
from tumblelog.models import BlogPost_About
from tumblelog.models import BlogPost_Napr
from tumblelog.models import BlogPost_Exams
from tumblelog.models import Video_Video
from tumblelog.models import BlogPost_Telegram
from tumblelog.models import BlogPost_Advices
from tumblelog.models import BlogPost_Events
from tumblelog.models import BlogPost_Day
from tumblelog.models import BlogPost_Properties


admin = Blueprint('admin', __name__, template_folder='templates')


class Del(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Main, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Main.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Main()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index'))


class Del1(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_About, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_About.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_About()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index1'))


class Del2(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Napr, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Napr.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Napr()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index2'))


class Del3(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Exams, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Exams.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Exams()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index3'))


class Del4(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(Video_Video, exclude=('created_at', 'comments'))

        if slug:
            post = Video_Video.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = Video_Video()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index4'))


class Del5(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Telegram, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Telegram.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Telegram()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index5'))


class Del6(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Advices, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Advices.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Advices()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index6'))


class Del7(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Events, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Events.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Events()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index7'))


class Del8(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Day, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Day.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Day()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index8'))


class Del9(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(BlogPost_Properties, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Properties.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Properties()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index9'))


class Del_title(MethodView):
    decorators = [requires_auth]

    def d_p(self, slug=None):
        form_cls = model_form(Title_Main, exclude=('created_at', 'comments'))

        if slug:
            post = Title_Main.objects.get_or_404(slug=slug)
            post.delete()
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = Title_Main()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        self.d_p(slug)
        return redirect(url_for('admin.index'))


class List(MethodView):
    decorators = [requires_auth]
    cls = BlogPost_Main
    cls1 = Title_Main

    def get(self):
        posts = self.cls.objects.all()
        post = self.cls1.objects.all()
        return render_template('admin/list.html', posts=posts, title=post)


class List1(List):
    cls = BlogPost_About

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list1.html', posts=posts)


class List2(List):
    cls = BlogPost_Napr

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list2.html', posts=posts)


class List3(List):
    cls = BlogPost_Exams

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list3.html', posts=posts)


class List4(List):
    cls = Video_Video

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list4.html', posts=posts)


class List5(List):
    cls = BlogPost_Telegram

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list5.html', posts=posts)


class List6(List):
    cls = BlogPost_Advices

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list6.html', posts=posts)


class List7(List):
    cls = BlogPost_Events

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list7.html', posts=posts)


class List8(List):
    cls = BlogPost_Day

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list8.html', posts=posts)


class List9(List):
    cls = BlogPost_Properties

    def get(self):
        posts = self.cls.objects.all()
        return render_template('admin/list9.html', posts=posts)


class Detail_title(MethodView):
    decorators = [requires_auth]

    def get_context(self, slug=None):
        form_cls = model_form(Title_Main, exclude=('created_at', 'comments'))

        if slug:
            post = Title_Main.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = Title_Main()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('admin/detail_title.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index'))
        return render_template('admin/detail_title.html', **context)


class Detail(MethodView):
    decorators = [requires_auth]

    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Main, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Main.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Main()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('admin/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index'))
        return render_template('admin/detail.html', **context)


class Detail1(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_About, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_About.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_About()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index1'))
        return render_template('admin/detail.html', **context)


class Detail2(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Napr, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Napr.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Napr()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index2'))
        return render_template('admin/detail.html', **context)


class Detail3(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Exams, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Exams.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Exams()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index3'))
        return render_template('admin/detail.html', **context)


class Detail4(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(Video_Video, exclude=('created_at', 'comments'))

        if slug:
            post = Video_Video.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = Video_Video()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index4'))
        return render_template('admin/detail.html', **context)


class Detail5(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Telegram, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Telegram.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Telegram()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index5'))
        return render_template('admin/detail.html', **context)


class Detail6(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Advices, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Advices.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Advices()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index6'))
        return render_template('admin/detail.html', **context)


class Detail7(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Events, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Events.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Events()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index7'))
        return render_template('admin/detail.html', **context)


class Detail8(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Day, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Day.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Day()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index8'))
        return render_template('admin/detail.html', **context)


class Detail9(Detail):
    def get_context(self, slug=None):
        form_cls = model_form(BlogPost_Properties, exclude=('created_at', 'comments'))

        if slug:
            post = BlogPost_Properties.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = BlogPost_Properties()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index9'))
        return render_template('admin/detail.html', **context)


# Register the urls
admin.add_url_rule('/admin/', view_func=List.as_view('index'))
admin.add_url_rule('/admin/about/', view_func=List1.as_view('index1'))
admin.add_url_rule('/admin/napr/', view_func=List2.as_view('index2'))
admin.add_url_rule('/admin/exams/', view_func=List3.as_view('index3'))
admin.add_url_rule('/admin/video/', view_func=List4.as_view('index4'))
admin.add_url_rule('/admin/telegram/', view_func=List5.as_view('index5'))
admin.add_url_rule('/admin/advices/', view_func=List6.as_view('index6'))
admin.add_url_rule('/admin/events/', view_func=List7.as_view('index7'))
admin.add_url_rule('/admin/day/', view_func=List8.as_view('index8'))
admin.add_url_rule('/admin/properties/', view_func=List9.as_view('index9'))

admin.add_url_rule('/admin/create/', defaults={'slug': None}, view_func=Detail.as_view('create'))
admin.add_url_rule('/admin/create/title/', defaults={'slug': None}, view_func=Detail_title.as_view('create_title'))
admin.add_url_rule('/admin/create/about', defaults={'slug': None}, view_func=Detail1.as_view('create1'))
admin.add_url_rule('/admin/create/napr', defaults={'slug': None}, view_func=Detail2.as_view('create2'))
admin.add_url_rule('/admin/create/exams', defaults={'slug': None}, view_func=Detail3.as_view('create3'))
admin.add_url_rule('/admin/create/video', defaults={'slug': None}, view_func=Detail4.as_view('create4'))
admin.add_url_rule('/admin/create/telegram', defaults={'slug': None}, view_func=Detail5.as_view('create5'))
admin.add_url_rule('/admin/create/advices', defaults={'slug': None}, view_func=Detail6.as_view('create6'))
admin.add_url_rule('/admin/create/events', defaults={'slug': None}, view_func=Detail7.as_view('create7'))
admin.add_url_rule('/admin/create/day', defaults={'slug': None}, view_func=Detail8.as_view('create8'))
admin.add_url_rule('/admin/create/properties', defaults={'slug': None}, view_func=Detail9.as_view('create9'))


admin.add_url_rule('/admin/<slug>/', view_func=Detail.as_view('edit'))
admin.add_url_rule('/admin/about/<slug>/', view_func=Detail1.as_view('edit1'))
admin.add_url_rule('/admin/napr/<slug>/', view_func=Detail2.as_view('edit2'))
admin.add_url_rule('/admin/exams/<slug>/', view_func=Detail3.as_view('edit3'))
admin.add_url_rule('/admin/video/<slug>/', view_func=Detail4.as_view('edit4'))
admin.add_url_rule('/admin/telegram/<slug>/', view_func=Detail5.as_view('edit5'))
admin.add_url_rule('/admin/advices/<slug>/', view_func=Detail6.as_view('edit6'))
admin.add_url_rule('/admin/events/<slug>/', view_func=Detail7.as_view('edit7'))
admin.add_url_rule('/admin/day/<slug>/', view_func=Detail8.as_view('edit8'))
admin.add_url_rule('/admin/properties/<slug>/', view_func=Detail9.as_view('edit9'))
admin.add_url_rule('/admin/title/<slug>', view_func=Detail_title.as_view('edit10'))

admin.add_url_rule('/admin/delete/<slug>/', view_func=Del.as_view('del'))
admin.add_url_rule('/admin/about/delete/<slug>/', view_func=Del1.as_view('del1'))
admin.add_url_rule('/admin/napr/delete/<slug>/', view_func=Del2.as_view('del2'))
admin.add_url_rule('/admin/exams/delete/<slug>/', view_func=Del3.as_view('del3'))
admin.add_url_rule('/admin/video/delete/<slug>/', view_func=Del4.as_view('del4'))
admin.add_url_rule('/admin/telegram/delete/<slug>/', view_func=Del5.as_view('del5'))
admin.add_url_rule('/admin/advices/delete/<slug>/', view_func=Del6.as_view('del6'))
admin.add_url_rule('/admin/events/delete/<slug>/', view_func=Del7.as_view('del7'))
admin.add_url_rule('/admin/day/delete/<slug>/', view_func=Del8.as_view('del8'))
admin.add_url_rule('/admin/properties/delete/<slug>/', view_func=Del9.as_view('del9'))
admin.add_url_rule('/admin/delete/title/<slug>/', view_func=Del_title.as_view('del_title'))
