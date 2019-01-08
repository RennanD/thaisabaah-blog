from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import PostForm
from blog.models import Post

# Create your views here.

def index(request):
	return redirect('login')

@login_required
def add(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect('add')

	return render(request, 'add.html', {'form': form})

@login_required
def dashboard(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') 
    paginator = Paginator(posts, 7)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {'post': post,'page': page}
    return render(request, 'dashboard.html', context)

@login_required
def update(request,id):
	posts = get_object_or_404(Post,pk=id)
	form = PostForm(request.POST or None, instance=posts)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect('dashboard')
	
	return render(request, 'update.html', {'posts': posts, 'form':form })

@login_required
def delete(request,id):
	post = get_object_or_404(Post,pk=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=post)
	delete_msg = "Post Deletado com Sucesso!"

	if request.method == 'POST':
		post.delete()
		return redirect('dashboard')
	return render(request,'delete.html',{'form':form, 'delete_msg':delete_msg})


def logout_view(request):
	logout(request)
	return redirect('login')