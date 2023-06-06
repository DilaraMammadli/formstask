from django.shortcuts import render, redirect
from .models import Book
from .forms import NewForm


def index_name(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html',context)

def detail_name(request):
    return render(request, 'detail.html')


# def create_name(request):
#     form = BookForm()
    
#     if request.method == "POST":
#         form = BookForm(request.POST)

#         if form.is_valid():
#             form.save()
#             # new_name = form.save()
#             # new_name.name = "Dilare" #burda verdiyim deyer goturulur databazada daxil etdiyim adin hec bir ehemiyyeti qalmir
#             # new_name.save()

#             return redirect("index")  #basqa sehe yonlendirir melumatlar elave etdikce indexde gorunecek
#         # print(request.POST)

#     context = {
#         "form":form
#     }
#     return render(request, 'create.html', context)



def new_product(request):
    form = NewForm()
    if request.method == "POST":
        
        form = NewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")


    context = {
        "form":form
    }
    return render(request, "create.html", context)