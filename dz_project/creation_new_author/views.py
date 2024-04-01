from django.shortcuts import render, redirect
from quotes.models import Author, Tag, Quote  # noqa
from django.contrib.auth.decorators import login_required


@login_required
def create_author(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        born_date = request.POST.get('born_date')
        born_location = request.POST.get('born_location')
        description = request.POST.get('description')
        Author.objects.create(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
        return redirect('quotes:root')

    return render(request, 'creation_new_author/create_author.html')


@login_required
def add_quote(request):
    if request.method == 'POST':

        quote_text = request.POST.get('quote')
        tag_names = request.POST.get('tags').split(',')
        author_name = request.POST.get('author')

        if author_name:
            author, _ = Author.objects.get_or_create(fullname=author_name)
        else:
            author = None

        new_quote = Quote(quote=quote_text, author=author)
        new_quote.save()

        for tag_name in tag_names:
            tag_name = tag_name.strip()
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            new_quote.tags.add(tag)

        return redirect('quotes:root')

    return render(request, 'creation_new_author/add_quote.html')