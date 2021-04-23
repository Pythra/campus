from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, View
from .forms import ProductForm, ShopForm, ServiceForm, ReviewForm, RequestForm, UserRegisterForm, HouseForm
from .models import Product, Service, Shop, Review, Request, House


def market_index(request):
    houses =House.objects.all()[:12]
    products =Product.objects.all()[:12]
    services =Service.objects.all()[:12]
    new_shops = Shop.objects.order_by('-created_on')[:6]
    requests = Request.objects.order_by('-created_on')
    context = {
            'houses': houses, 
            'products': products,
            'services': services, 
            'new_shops': new_shops,
            'requests': requests,
                }
    return render(request, 'market/index.html', context)
   


def product_detail(request, slug):
    template_name = 'market/product_detail.html'
    product = get_object_or_404(Product, slug=slug)
    reviews = product.reviews.all
    context = {'product': product, 'slug': slug, 'reviews': reviews}
    return render(request, template_name, context)


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('market_home')
    template_name = 'market/my_shop.html'


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.school = request.user.shop.school
            product.shop = request.user.shop
            product.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'market/product_form.html', context)


def service_detail(request, slug):
    template_name = 'market/service_detail.html'
    service = get_object_or_404(Service, slug=slug)
    reviews = service.reviews.all
    context = {'service': service, 'slug': slug, 'reviews': reviews}
    return render(request, template_name, context)


class ServiceUpdate(UpdateView):
    model = Service
    form_class = ServiceForm


class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('market_home')


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.school = request.user.shop.school
            service.shop = request.user.shop
            service.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ServiceForm()
    context = {'form': form}
    return render(request, 'market/service_form.html', context)


@login_required
def my_shop(request):
    my_services = request.user.shop.service_set.all
    my_products = request.user.shop.product_set.all
    if request.method == 'POST':
        profile_form = ShopForm(request.POST, request.FILES, instance=request.user.shop)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return HttpResponseRedirect(reverse('shop', kwargs={'pk': request.user.id}))

    else:
        profile_form = ShopForm(instance=request.user.shop)

    context = {'p_form': profile_form, 'my_products': my_products, 'my_services': my_services}
    return render(request, 'market/my_shop.html', context)


@login_required
def visit_shop(request, pk):
    user = User.objects.get(pk=pk)
    services = user.shop.service_set.all
    products = user.shop.product_set.all
    context = {'user': user, 'products': products, 'services': services}
    return render(request, 'market/visit_shop.html', context)


class ShopUpdate(UpdateView):
    model = Shop
    form_class = ShopForm


class ShopDelete(DeleteView):
    model = Shop
    success_url = reverse_lazy('market_home')


@login_required
def review_create(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.customer = request.user
            review.dp = request.user.shop.establishment_pic.url
            review.save()
            return HttpResponseRedirect(reverse('product_detail', kwargs={'slug': slug}))
    else:
        form = ReviewForm()
    context = {'form': form, 'product': product}
    return render(request, 'market/review_form.html', context)


class ReviewUpdate(UpdateView):
    model = Review
    form_class = ReviewForm


class ReviewDelete(DeleteView):
    model = Review
    success_url = reverse_lazy('product_detail')


def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    services = Service.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {'products': products, 'services': services}
    return render(request, 'market/search/search_home.html', context)


def all_products(request):
    products = Product.objects.all.order_by('-created_on')
    context = {'products': products}
    return render(request, 'market/list_all/all_products.html', context)

def all_services(request):
    services = Service.objects.all.order_by('-created_on')
    context = {'services': services}
    return render(request, 'market/list_all/all_services.html', context)


def all_shops(request):
    shops = Shop.objects.filter.all.order_by('-created_on')
    context = {'shops': shops}
    return render(request, 'market/list_all/all_shops.html', context)


@login_required
def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            req = form.save(commit=False)
            req.shop = request.user.shop
            req.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RequestForm()
    context = {'form': form}
    return render(request, 'market/request_form.html', context)


def request_detail(request, pk):
    template_name = 'market/request_detail.html'
    req = get_object_or_404(Request, pk=pk)
    context = { 'req': req}
    return render(request, template_name, context)


def settings(request):
    template_name = 'market/settings.html'
    return render(request, template_name)


class SignUpView(View):
    form_class = UserRegisterForm
    template_name = 'market/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            return redirect('login')

        return render(request, self.template_name, {'form': form})


@login_required
def house_create(request):
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
            house.school = request.user.shop.school
            house.shop = request.user.shop
            house.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = HouseForm()
    context = {'form': form}
    return render(request, 'market/house_form.html', context)




def house_detail(request, pk):
    template_name = 'market/house_detail.html'
    house = get_object_or_404(House, pk=pk)
    context = {'house': house,}
    return render(request, template_name, context)


