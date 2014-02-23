from blog.models import Blog
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        """Return the last five published blogs."""
        return Blog.objects.order_by('-id')[:5]

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'

class EditView(generic.DetailView):
    model = Blog
    template_name = 'blog/edit.html'

def blog_save(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
    except (KeyError, Blog.DoesNotExist):
        return render(request, 'blog/edit.html', {
            'blog': blog,
            'error_message': "Blog with such id doesn't exist.",
        })
    else:
        blog.save()
        return HttpResponseRedirect(reverse('blog:index'))