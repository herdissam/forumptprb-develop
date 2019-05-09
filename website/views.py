from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Post
from website.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
    queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 4) # Show 25 queryset per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list" : queryset,
    }
    return  render(request, "home.html", context)

def tentang(request):
    return render(request, 'tentang.html')

def bukukkn(request):
    return render(request, 'bukukkn.html')

def prosiding(request):
    return render(request, 'prosiding.html')

def riset(request):
    return render(request, 'riset.html')

def read(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 4) # Show 25 queryset per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list" : queryset, 
    }
    return  render(request, "read.html", context)

def read_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title" : instance.title,
        "instance" : instance,
    }
    return render(request, "read_detail.html", context)

def daftar(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = RegistrationForm()

        args = {
            'form': form
        }
        return render(request, 'daftar.html', args)

def view_profile(request):
    args = {'user', request.user}
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)
