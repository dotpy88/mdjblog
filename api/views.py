from rest_framework import mixins, viewsets
from rest_framework import permissions
from .serializers import BlogSerializer
from .filters import BlogFilter
from blog.models import Blog

# Create your views here.

class BlogView(
  mixins.CreateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  viewsets.GenericViewSet,
):

  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  filterset_class = BlogFilter
  #permission_classes = [permissions.IsAuthenticated]
