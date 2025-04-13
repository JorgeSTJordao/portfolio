from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def timeline(request):
    return render(request, "routes/timeline.html")