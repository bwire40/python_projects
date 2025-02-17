from django.shortcuts import render

# Create your views here.
def postsPage(request):
    return render(request,'posts/posts.html')