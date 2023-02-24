from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeSlider, HomeSliderActive, Category, SubCategory, Product
# Create your views here.

class HomeListView(ListView):
    template_name = 'main/index.html'

    def get(self, request):
        tertox = HomeSliderActive.objects.all()[0]
        tertvox = HomeSlider.objects.all()
        category_list = Category.objects.all().order_by('name')
        product_list = Product.objects.all()
        brand_list = SubCategory.objects.all()
        return render(request, self.template_name, context={
            'tertox':tertox,
            'tertvox':tertvox,
            'category_list':category_list,
            'product_list':product_list,
            'brand_list':brand_list
        })

class ShopListView(ListView):
    template_name = 'main/shop.html'

    def get(self, request, id):
        products = SubCategory.objects.filter(pk=id)
        brand_list = SubCategory.objects.all()
        category_list = Category.objects.all().order_by('name')
        

        return render(request, self.template_name, context={
            'products':products, 
            'category_list':category_list,
            'brand_list':brand_list})
