from django.shortcuts import render, get_object_or_404, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from .models import Blog
# Create your views here.

def blog_list(request):
	today = timezone.now().date()

	paginator = Paginator(queryset_list, 9) # Show 9 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug=None):
	blog = get_object_or_404(Blog, id=id, slug=slug, available=True)
	context = {
		'title': title,
		'blog': blog,
	}
	return render(request, 'blog/blog_detail.html', context)