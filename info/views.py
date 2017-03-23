from django.shortcuts import render

# Create your views here.
def sourcecode(request):
    context = {}
    return render(request, 'info/sourcecode.html', context)