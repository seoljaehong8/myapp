from django.http.response import HttpResponse
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
    else:
        return HttpResponse({'hello post'})