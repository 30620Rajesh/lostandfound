from django.shortcuts import render,redirect
from lost.models import itemlost
from lost.models import itemfound
from users.models import itemfoundfull,itemlostfull
# from django.core.paginator import Paginatorpython 
#from .forms import lostform , foundform,RegistrationForm
from .forms import lostform , foundform
#from.models import RegistrationData 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

from users.forms import lostfullform, foundfullform

from users.models import Profile

from django.core.paginator import Paginator

def lost_view(request,*args,**kwargs):
    obj=itemlost.objects.all()
    obj1=list(reversed(obj))
    paginator=Paginator(obj1, 4)
    page=request.GET.get('page') # ?page=number
    objpic=Profile.objects.all()
    context={
        'object':paginator.get_page(page),
        'objectpic':objpic
        }
    return render(request,"lostlist.html",context)
@login_required
def lost_enter(request,*args,**kwargs):
    if request.method=='POST':
        dict1=request.POST.copy()
        dict1['username']=request.user.username
        form=lostform(dict1 or None)
        if form.is_valid():
            formfull=lostfullform(dict1 or None)
            formfull.save()
            form.save()
            messages.success(request,'Your form has been posted successfully!')
            return redirect('home')
    else:
        form=lostform()
    context={
        'form':form
        }
    return render(request,"lost.html",context)

def found_enter(request,*args,**kwargs):
    if request.method=='POST':
        dict2=request.POST.copy()
        dict2['username']=request.user.username
        form1=foundform(dict2 or None)
        if form1.is_valid():
            formfull1=foundfullform(dict2 or None)
            formfull1.save()
            form1.save()
            messages.success(request,'Your form has been posted successfully!')
            return redirect('home')
    else:
        form1=foundform()
    context={
        'form1':form1
        }
    return render(request,"found.html",context)
@login_required
def found_view(request,*args,**kwargs):
    obj=itemfound.objects.all()
    obj1=list(reversed(obj))
    paginator=Paginator(obj1, 4)
    page=request.GET.get('page') # ?page=number
    objpic=Profile.objects.all()
    context={
        'object':paginator.get_page(page),
        'objectpic':objpic
        }

    return render(request,"foundlist.html",context)




# def found_view(request, *args, **kwargs):
#     # Check if the user has submitted a search query
#     query = request.GET.get('query')
    
#     if query:
#         # If a search query is provided, filter found items based on the query
#         found_items = search_found_items_in_database(query)
#     else:
#         # If no search query is provided, retrieve all found items
#         found_items = itemfound.objects.all()

#     # Reverse the order of items, paginate them, and fetch page number from the request
#     found_items_reversed = list(reversed(found_items))
#     paginator = Paginator(found_items_reversed, 4)
#     page = request.GET.get('page')

#     # Retrieve profile objects
#     objpic = Profile.objects.all()

#     context = {
#         'object': paginator.get_page(page),
#         'objectpic': objpic,
#     }

#     return render(request, "foundlist.html", context)

def search_found_items_in_database(query):
    # Use case-insensitive search for the product_title field
    results = itemfound.objects.filter(product_title__icontains=query)
    return results