from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask_mongoengine.wtf import model_form

from tumblelog.models import Comment
from tumblelog.models import BlogPost_Main
from tumblelog.models import BlogPost_About
from tumblelog.models import BlogPost_Napr
from tumblelog.models import BlogPost_Exams
from tumblelog.models import Video_Video
from tumblelog.models import BlogPost_Telegram
from tumblelog.models import BlogPost_Advices
from tumblelog.models import BlogPost_Events
from tumblelog.models import BlogPost_Day
from tumblelog.models import BlogPost_Properties
posts = Blueprint('posts', __name__, template_folder='../templates')


class ListView_Main(MethodView):

    def get(self):
        posts = BlogPost_Main.objects.all()
        return render_template('posts/list.html', posts=posts)


class ListView_About(MethodView):

    def get(self):
        posts = BlogPost_About.objects.all()
        return render_template('posts/list1.html', posts=posts)


class ListView_Napr(MethodView):

    def get(self):
        posts = BlogPost_Napr.objects.all()
        return render_template('posts/list2.html', posts=posts)


class ListView_Exams(MethodView):

    def get(self):
        posts = BlogPost_Exams.objects.all()
        return render_template('posts/list3.html', posts=posts)


class ListView_Video(MethodView):

    def get(self):
        posts = Video_Video.objects.all()
        return render_template('posts/list4.html', posts=posts)


class ListView_Telegram(MethodView):

    def get(self):
        posts = BlogPost_Telegram.objects.all()
        return render_template('posts/list5.html', posts=posts)


class ListView_Advices(MethodView):

    def get(self):
        posts = BlogPost_Advices.objects.all()
        return render_template('posts/list6.html', posts=posts)


class ListView_Events(MethodView):

    def get(self):
        posts = BlogPost_Events.objects.all()
        return render_template('posts/list7.html', posts=posts)


class ListView_Day(MethodView):

    def get(self):
        posts = BlogPost_Day.objects.all()
        return render_template('posts/list8.html', posts=posts)


class ListView_Properties(MethodView):

    def get(self):
        posts = BlogPost_Properties.objects.all()
        return render_template('posts/list9.html', posts=posts)


class DetailView(MethodView):

    form = model_form(Comment, exclude=['created_at'])

    def get_context(self, slug):
        post = BlogPost_Main.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('posts/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            post.save()

            return redirect(url_for('posts.detail', slug=slug))

        return render_template('posts/detail.html', **context)


class DetailView1(DetailView):

    def get_context(self, slug):
        post = BlogPost_About.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView2(DetailView):

    def get_context(self, slug):
        post = BlogPost_Napr.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView3(DetailView):

    def get_context(self, slug):
        post = BlogPost_Exams.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView4(DetailView):

    def get_context(self, slug):
        post = Video_Video.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView5(DetailView):

    def get_context(self, slug):
        post = BlogPost_Telegram.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView6(DetailView):

    def get_context(self, slug):
        post = BlogPost_Advices.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView7(DetailView):

    def get_context(self, slug):
        post = BlogPost_Events.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView8(DetailView):

    def get_context(self, slug):
        post = BlogPost_Day.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


class DetailView9(DetailView):

    def get_context(self, slug):
        post = BlogPost_Properties.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


# Register the urls

posts.add_url_rule('/', view_func=ListView_Main.as_view('list'))
posts.add_url_rule('/about/', view_func=ListView_About.as_view('list1'))
posts.add_url_rule('/napr/', view_func=ListView_Napr.as_view('list2'))
posts.add_url_rule('/exams/', view_func=ListView_Exams.as_view('list3'))
posts.add_url_rule('/video/', view_func=ListView_Video.as_view('list4'))
posts.add_url_rule('/telegram/', view_func=ListView_Telegram.as_view('list5'))
posts.add_url_rule('/advices/', view_func=ListView_Advices.as_view('list6'))
posts.add_url_rule('/events/', view_func=ListView_Events.as_view('list7'))
posts.add_url_rule('/day/', view_func=ListView_Day.as_view('list8'))
posts.add_url_rule('/properties/', view_func=ListView_Properties.as_view('list9'))

posts.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
posts.add_url_rule('/about/<slug>/', view_func=DetailView1.as_view('detail1'))
posts.add_url_rule('/napr/<slug>/', view_func=DetailView2.as_view('detail2'))
posts.add_url_rule('/exams/<slug>/', view_func=DetailView3.as_view('detail3'))
posts.add_url_rule('/video/<slug>/', view_func=DetailView4.as_view('detail4'))
posts.add_url_rule('/telegram/<slug>/', view_func=DetailView5.as_view('detail5'))
posts.add_url_rule('/advices/<slug>/', view_func=DetailView6.as_view('detail6'))
posts.add_url_rule('/events/<slug>/', view_func=DetailView7.as_view('detail7'))
posts.add_url_rule('/day/<slug>/', view_func=DetailView8.as_view('detail8'))
posts.add_url_rule('/properties/<slug>/', view_func=DetailView9.as_view('detail9'))