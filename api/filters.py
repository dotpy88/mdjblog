import django_filters
from blog.models import Blog

class BlogFilter(django_filters.FilterSet):

  class Meta:
    model = Blog
    fields = ('__all__')