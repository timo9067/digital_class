from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(
        request=request,
        template_name="lesson/homepage.html",
        context={}
    )

def lesson_list_view(request):
    pass

def lesson_detail_view(request):
    pass
