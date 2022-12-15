from django.shortcuts import render
from .models import Company, Product
from django.http import HttpResponseRedirect, HttpResponseNotFound

def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def create(request):
    create_companies()

    if request.method== 'POST':
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return HttpResponseRedirect("/")
    companies = Company.objects.all()
    return render(request, 'create.html', {"companies": companies})

def edit(request, id):
    try:
        product = Product.get(id=id)
        if request.method == "POST":
            product.name = request.post.get("name")
            product.price = request.post.get("price")
            product.company_id = request.post.get("company")
            product.save()
            return HttpResponseRedirect("/")
        else:
            companies = Company.objects.all()
            return render(request, "edit.html", {"product": product, "companies": companies})
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2> Product not found</h2>")

def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return  HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2> Product not found </h2>")

def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name = "Apple")
        Company.objects.create(name="Asus")
        Company.objects.create(name="MSI")
