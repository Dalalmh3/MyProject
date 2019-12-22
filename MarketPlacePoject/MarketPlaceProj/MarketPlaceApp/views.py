from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm
# Create your views here.

def index(request):
    context= {
        "all_products": Product.objects.all(),
    }
    return render(request, "MarketPlaceApp/index.html", context ) 

def login(request):
    return render(request, 'Registration/login.html')

def Add_Product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect("/")

    form = ProductForm()
    return render(request, 'MarketPlaceApp/add_product.html',{'form':form})

def logout(request):
    pass



# def upload_file(request):

#     try:
#         if request.method == 'POST' : #and request.FILES['myfile']:
#             #The request.FILES will hold the uploaded file
#             myfile = request.FILES['myfile']
#             fs = FileSystemStorage() #store uploaded file
#             filename = fs.save(myfile.name, myfile) #save the name of uploaded file
#             fileURL = fs.url(filename) #convert the name of uploaded file to URL
    
#             new_poduct = Product.objects.create( pName = request.POST['pname'] , description = request.POST['pDescription'], img_url = fileURL) #, img_url = fileURL)
#             messages.info(request, 'The product has been Created successfully!')
#             return redirect('/')
                     
#     except Exception as e:
#         print (e)
#         messages.info(request, " Upload Image please") #error message if the user presses upload without uploading an image
#         return redirect("/")