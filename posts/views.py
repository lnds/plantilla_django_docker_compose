from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from posts.forms import PostCreateForm, PostUpdateForm
from posts.models import Post


class PostMixin(SuccessMessageMixin):
    model = Post


class PostListView(PostMixin, ListView):
    paginate_by = 10


class PostDetailView(PostMixin, DetailView):
    pass


class PostCreateView(PostMixin, LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('home')
    success_message = _("Post creado")
    form_class = PostCreateForm


class PostUpdateView(PostMixin, LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('home')
    success_message = _("Post modificado")
    form_class = PostUpdateForm


class PostDeleteView(PostMixin, LoginRequiredMixin, DeleteView):
    success_message = _("Post eliminado")
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
