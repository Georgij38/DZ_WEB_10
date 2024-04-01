from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Author, Quote, Tag



def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotes/index.html', {'quotes': quotes_on_page})


def author_detail(request, author_id):
    try:
        author = get_object_or_404(Author, pk=author_id)
    except Http404:
        return render(request, 'quotes/404.html', status=404)

    return render(request, 'quotes/author.html', {'author': author})


def tag_detail(request, tag_id):
    try:
        tag = Tag.objects.get(id=tag_id)
        quotes = Quote.objects.filter(tags=tag)
    except Tag.DoesNotExist:
        return render(request, 'quotes/404.html', status=404)
    except Quote.DoesNotExist:
        return render(request, 'quotes/404.html', status=404)

    return render(request, 'quotes/tag_detail.html', {'tag': tag, 'quotes': quotes})