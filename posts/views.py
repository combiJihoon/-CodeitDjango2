from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


class PostListView(ListView):
    model = Post
    # 글을 최신 순으로 정렬 -> '-' 기호를 붙이면 가장 최신 순으로 정렬됨
    # '-' 기호를 붙이지 않으면 오름차순으로 정렬됨
    ordering = ['-dt_created']
    # 몇 개 단위로 페이지를 나눌 것인지 결정
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post  # 우리가 사용할 모델 할당
    form_class = PostForm  # 우리가 사용할 폼

    def get_success_url(self):
        # 이동할 url
        # kwargs = keyword argument의 약자로, 사전형으로 키워드를 이용해서 값을 전달시 사용
        # self.objects.id를 통해 새로 생성된 post 데이터 객체에 접근할 수 있다.
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm()

    # postform의 유효성 검증 통과시 이동할 url
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post-list')


def index(request):
    return redirect('post-list')


class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'
