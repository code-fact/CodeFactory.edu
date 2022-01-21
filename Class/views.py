from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Posts, Categorys
from .forms import posts, Edit, MSG
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector, SearchQuery

def home(request):
    paginator = Paginator(Posts.objects.all(), 12)
    verbose = 'Search'
    if request.method == 'POST':
        verbose = request.POST.get('query')
        query = SearchQuery(verbose)
        POST = Posts.objects.annotate(
            search=SearchVector('title', 'description'),
        ).filter(search=query)
        paginator = Paginator(POST, 12)
    Post = paginator.get_page(request.GET.get('page'))
    return render(request, 'home.html', {'Post':Post, 'verbose':verbose})

class article(generic.DetailView):
    model = Posts
    template_name = 'article.html'
    def post(self, *args, **kwargs):
        form = MSG(self.request.POST)
        if form.is_valid():
            Post = get_object_or_404(Posts, id=self.kwargs['pk'])
            msg = 'user_name:{0};\nmsg:{1};\nmail:{2};'.format(form.cleaned_data['name'],form.cleaned_data['msg'],form.cleaned_data['mail'])
            msg = msg+f'\npost_name:{Post};'
            try:
                send_mail(Post, msg, 'yashasvi.coder@outlook.com', ['yashasvi.coder@outlook.com'])
            except Exception as e:
                return HttpResponse(e)
        return HttpResponseRedirect(reverse('article', args=[str(self.kwargs['pk'])]))
    def get_context_data(self, *args, **kwargs):
        context = super(article, self).get_context_data(*args, **kwargs)
        liked = False
        if get_object_or_404(Posts, id=self.kwargs['pk']).like.filter(id=self.request.user.id).exists():
            liked = True
        like = get_object_or_404(Posts, id=self.kwargs['pk']).likes()
        msg = MSG()
        context['liked'] = liked
        context['like'] = like
        context['msg'] = msg
        return context

class post(generic.CreateView):
    model = Posts
    form_class = posts
    template_name = 'post.html'
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

class edit(generic.UpdateView):
    model = Posts
    form_class = Edit
    template_name = 'edit.html'

class purge(generic.DeleteView):
    model = Posts
    template_name = 'purge.html'
    success_url = reverse_lazy('home')

class tag(generic.CreateView):
    model = Categorys
    fields = '__all__'
    template_name = 'tag.html'
    def form_valid(self, form):
        if form.instance.title == slugify(form.instance.title):
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

def category(request, slug):
    Post = set(Posts.objects.filter(category=slug).order_by('-like'))
    verbose = 'Search'
    if request.method == 'POST':
        verbose = request.POST.get('query')
        query = SearchQuery(verbose)
        Post = Posts.objects.annotate(
            search=SearchVector('title', 'description'),
        ).filter(search=query).order_by('-like')
    return render(request, 'category.html', {'slug':slug, 'Post':set(Post), 'verbose':verbose})

class categories(generic.ListView):
    model = Categorys
    template_name = 'categories.html'
    def get_context_data(self, *args, **kwargs):
        context = super(categories, self).get_context_data(*args, **kwargs)
        categorys = [topic.title for topic in Categorys.objects.all()]
        categorys = sorted(categorys)
        context['categorys'] = categorys
        return context

def like(request, pk):
    like = get_object_or_404(Posts, id=request.POST.get('like'))
    liked = False
    if like.like.filter(id=request.user.id).exists():
        like.like.remove(request.user)
        liked = False
    else:
        like.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))

def user(request, pk):
    Post = set(Posts.objects.filter(author=pk).order_by('-like'))
    verbose = 'Search'
    if request.method == 'POST':
        verbose = request.POST.get('query')
        query = SearchQuery(verbose)
        Post = Posts.objects.annotate(
            search=SearchVector('title', 'description'),
        ).filter(search=query).order_by('-like')
    for slug in Post:
        slug = slug.author.username
    return render(request, 'user.html', {'slug':slug, 'verbose':verbose, 'Post':set(Post)})
