from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.validators import URLValidator
from . import service
from .forms import UrlForm

# import pyshorteners


def index(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)

            question.hash = service.shorten(question.original_url)

            question.save()
            return redirect("main:shorten", url=question.hash)
    else:
        form = UrlForm()

    return render(request, "main/index.html", {"form": form})


def shorten(request, hash):
    # returns the full url ie: https://google.com
    shortened_url: str = request.build_absolute_uri(
        reverse("main:redirect", args=[hash])
    )
    return render(request, "main/link.html", {"shortened_url": shortened_url})


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)
