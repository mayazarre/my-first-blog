from django.shortcuts import render

# Create your views heredef post_list(request):

def post_list(request):
    return render(request, 'blog/post_list.html', {})
