from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Book


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Book.objects.order_by("-add_date")[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("books:detail", args=[item.pk])