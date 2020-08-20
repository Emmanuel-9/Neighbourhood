from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Neighbourhood,  Business, Post
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import BusinessCreateForm, HoodCreateForm



# Create your views here.
def welcome(request):
    groups = Group.objects.all()
    neigh = Neighbourhood.get_all_neighbourhoods()
    context = {
        'group': groups,
        'neighs': neigh,
    }
    return render(request, 'hood/welcome.html', context)

def business(request):
    business = Business.get_all_businesses()
    context = {
        'business': business
    }

    return render(request, 'hood/business.html', context)

def post(request):
    posts = Post.get_all_posts()
    context = {
        'posts': posts
    }
    return render(request, 'hood/posts.html', context)

# @user_passes_test(lambda u: u.is_superuser)
def admin_profile(request):
    if not request.user.username == 'admin':
        return redirect('/login/?next=%s' % request.path)
    else:
        users = User.objects.all().order_by('id')
        print(type(users))
        business = Business.objects.all()
        neigh = Neighbourhood.objects.all()
        context = {
            'users': users,
            'business': business,
            'hoods': neigh
        }
        return render(request, 'hood/admin_profile.html', context)

@method_decorator(login_required, name='dispatch')
class BusinessCreateView(UserPassesTestMixin, CreateView):
    model = Business
    fields = ['name', 'email', 'desc', 'neighbourhood']

    def test_func(self):
        groups = self.request.user.groups.all()
        groups_refined = []
        for group in groups:
            groups_refined.append(group.name)
        
        if 'normal users' and 'neighbourhood admin' in groups_refined:
            return True
        return False    

    def form_valid(self, form):
        print('great')
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class BusinessUpdateView(UserPassesTestMixin, UpdateView):
    model = Business
    fields = ['name', 'email', 'desc', 'neighbourhood']

    def test_func(self):
        groups = self.request.user.groups.all()
        groups_refined = []
        for group in groups:
            groups_refined.append(group.name)
        
        if 'normal users' and 'neighbourhood admin' in groups_refined:
            return True
        return False    

    def form_valid(self, form):
        print('great')
        form.instance.user = self.request.user
        return super().form_valid(form)

class BusinessDetailView(DetailView):
    model = Business

@method_decorator(login_required, name='dispatch')
class BusinessDeleteView(UserPassesTestMixin, DeleteView):
    model = Business
    fields = ['name', 'email', 'desc', 'neighbourhood']
    success_url = '/'

    def test_func(self):
        groups = self.request.user.groups.all()
        groups_refined = []
        for group in groups:
            groups_refined.append(group.name)
        
        if 'normal users' and 'neighbourhood admin' in groups_refined:
            return True
        return False

@method_decorator(login_required, name='dispatch')
class HoodCreateView(UserPassesTestMixin, CreateView):
    model = Neighbourhood
    fields = '__all__'


    def test_func(self):
        groups = self.request.user.groups.all()
        groups_refined = []
        for group in groups:
            print(group.name)
            groups_refined.append(group.name)

        if 'admin' in groups_refined:
            return True
        return False                 

    def form_valid(self, form):
        return super().form_valid(form)


class HoodDetailView(DetailView):
    model = Neighbourhood

@method_decorator(login_required, name='dispatch')
class HoodUpdateView(UserPassesTestMixin, UpdateView):
    model = Neighbourhood
    fields = '__all__'


    def test_func(self):
        groups = self.request.user.groups.all()
        groups_refined = []
        for group in groups:
            print(group.name)
            groups_refined.append(group.name)

        if 'admin' in groups_refined:
            return True
        return False                 

    def form_valid(self, form):
        print('great')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class HoodDeleteView(UserPassesTestMixin, DeleteView):
    model = Neighbourhood
    fields = '__all__'
    success_url = '/'


    def test_func(self):
        groups = self.request.user.groups.all()
        groups_refined = []
        for group in groups:
            print(group.name)
            groups_refined.append(group.name)

        if 'admin' in groups_refined:
            return True
        return False                 

    def form_valid(self, form):
        print('great')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content', 'image']

    def form_valid(self, form):
        print('great')
        print(self.request.user.userprofile.neighbourhood)
        form.instance.neighbourhood = self.request.user.userprofile.neighbourhood
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
 