from django.shortcuts import render
from django.http import HttpResponse
from .models import Resources
from apps.user.models import User
from django.db.models import Count
from .utils import generate_cat_list
from .form import PostResourceForm

# Create your views here.

def home_page(request):
    cnt_res = Resources.objects.all().count()
    user_count = User.objects.filter(is_active=True).count()
    
    res_count = (Resources.objects.values("cat_id__cat").annotate(count_cat=Count("cat_id"))) 
    
    context = {
        "cnt_res": cnt_res,
        "user_count": user_count,
        "res_count": res_count,
    }
    
    return render(
        request=request,
        template_name="resources/home.html",
        context=context
    )

def home_page_old(request):
    cnt_res = Resources.objects.all().count()
    user_count = User.objects.filter(is_active=True).count()
    
    res_count = Resources.objects.values("cat_id__cat").annotate(count_cat=Count("cat_id")) 

    response = f"""
    <html>
    <h1>Welcome to my page</h1>
    <p>We have {cnt_res} resources</p>
    <p>We have {user_count} users</p>
    <p>We have {generate_cat_list(res_count)}</p>
    </html>
    """
    
    return HttpResponse(response)

def resource_detail(request, id): 
    result = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .get(pk=id)
    )
    
    response = f"""
    <html>
    <h1>{result.title}</h1>
    <p>Uploaded by user: {result.username}</p>
    <p>Description {result.description} </p>
    <p>Link {result.link} </p>
    <p>Categories: {result.cat_id}</p>
    <p>Tags: {result.all_tags()} </p>
    
    </html>
    """
    return HttpResponse(response)
    
    
def resource_post(request):
    # breakpoint()
    
    # Unbound
    if request.method == "GET":
        form = PostResourceForm()
        context = {
            "form": form,
        }
        
        return render(
            request=request,
            template_name="resources/resource-post.html",
            context=context,
        )
    
    # Bound
    else:
        form = PostResourceForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            # TODO: manually add a user id
            
            user_id = 1 
            
            # TODO: Save it to the database
            # TODO: Redirect the user to the home page
            
            
        return render(
            request=request,
            template_name="resources/resource-post.html",
        )