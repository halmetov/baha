from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import math
from main.models import ClientSays, Information, Brand, Service, BestService, Recovery, ServiceProcess, Product, \
    Feedback, Blog, Staff, About_service, About, About_action, BlogQoute, Blogcomment, Price, Faq, Contact,\
    Productcomment, ProductCategory, BlogCategory, ContactPost,Cart,CartItem
# Create your views here.



def indexHandler (request):
    cart = {}
    cart_items = []
    open_carts =Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart



    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    best_services = BestService.objects.filter()[:4]
    recoveries = Recovery.objects.filter()
    service_processs = ServiceProcess.objects.filter()[:6]
    products = Product.objects.filter()
    feedbacks = Feedback.objects.filter()[:4]
    blogs = Blog.objects.filter(is_latest=True)[:3]



    return render(request, 'index.html', {
        'active_page': 'main',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'best_services': best_services,
        'recoveries': recoveries,
        'service_processs': service_processs,
        'products': products,
        'feedbacks': feedbacks,
        'blogs': blogs,

        'cart': cart,
        'cart_items': cart_items,
    })


def aboutHandler (request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    staffs = Staff.objects.filter()
    recoveries = Recovery.objects.filter()
    about_services = About_service.objects.filter()[:4]
    abouts = About.objects.filter()[:2]
    about_actions = About_action.objects.filter()[:6]


    return render(request, 'about.html', {
        'active_page': 'about',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'staffs': staffs,
        'recoveries': recoveries,
        'about_services': about_services,
        'abouts': abouts,
        'about_actions': about_actions,

        'cart': cart,
        'cart_items': cart_items,
    })


def serviceHandler(request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    ex_staffs = Staff.objects.filter(is_experienced=True)
    main_services = Service.objects.filter(is_main=True)
    service_processs = ServiceProcess.objects.filter()[:6]



    return render(request, 'service.html',{
        'active_page': 'service',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'ex_staffs': ex_staffs,
        'main_services': main_services,
        'service_processs': service_processs,

        'cart': cart,
        'cart_items': cart_items,
    })


def service_listHandler(request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    ex_staffs = Staff.objects.filter(is_experienced=True)



    return render(request, 'service-list.html',{
        'active_page': 'service-list',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'ex_staffs': ex_staffs,

        'cart': cart,
        'cart_items': cart_items,
    })


def service_detailHandler(request, detail_id):
    detail = Service.objects.get(id=int(detail_id))
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    ex_staffs = Staff.objects.filter(is_experienced=True)
    recoveries = Recovery.objects.filter()
    blogs = Blog.objects.filter()[:6]
    if detail.id == 1:
        prev_service = Service.objects.get(id=int(detail_id) + 2)
    else:
        prev_service = Service.objects.get(id=int(detail_id) - 1)

    if len(services) == detail.id:
        next_service = Service.objects.get(id=int(detail_id) - 2)
    else:
        next_service = Service.objects.get(id=int(detail_id) + 1)

    return render(request, 'service-detail.html', {
        'detail': detail,
        'active_page': 'service-detail',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'ex_staffs': ex_staffs,
        'recoveries': recoveries,
        'blogs': blogs,
        'prev_service': prev_service,
        'next_service': next_service,

    })



def blogHandler(request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    which_one_id = int(request.GET.get('which_one_id', 0))

    limit = int(request.GET.get('limit', 2))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    if which_one_id:
        blogs = Blog.objects.filter(which_one__id=which_one_id)[start:stop]
        total = Blog.objects.filter(which_one__id=which_one_id).count()
    else:
        blogs = Blog.objects.filter()[start:stop]
        total = Blog.objects.count()

    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    latest_blogs = Blog.objects.filter(is_latest=True)[:4]
    categories = BlogCategory.objects.filter()






    return render(request, 'blog.html',{
        'current_page': current_page,
        'prev_page': prev_page,
        'next_page': next_page,
        'total': total,
        'limit': limit,

        'active_page': 'blog',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'blogs': blogs,
        'latest_blogs': latest_blogs,
        'categories': categories,

        'which_one_id': which_one_id,

        'cart': cart,
        'cart_items': cart_items,
    })


def blog_detailHandler(request, blog_detail_id):
    if request.POST:
        print('***'*100)
        print(request.POST)
        new_post_comment = Blogcomment()
        new_post_comment.email = request.POST.get('email', '')
        new_post_comment.phone = request.POST.get('phone', '')
        new_post_comment.comment_id = int(request.POST.get('comment_id', 0))
        new_post_comment.blog_id = int(request.POST.get('blog_id', 0))
        new_post_comment.name = request.POST.get('name', '')
        new_post_comment.text = request.POST.get('text', '')
        new_post_comment.date = datetime.now()
        new_post_comment.save()

    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    which_one_id = int(request.GET.get('which_one_id', 0))
    limit = int(request.GET.get('limit', 2))
    total = Blog.objects.count()

    blog_detail = Blog.objects.get(id=int(blog_detail_id))
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    blog_quotes = BlogQoute.objects.filter()
    latest_blogs = Blog.objects.filter(is_latest=True)[:4]
    blog_categories = Blog.objects.filter()[:4]
    blog_comments = Blogcomment.objects.filter(blog_id=int(blog_detail_id))
    categories = BlogCategory.objects.filter()

    if blog_detail.id == 1:
        prev_blog = Blog.objects.get(id=int(blog_detail_id) + 2)
    else:
        prev_blog = Blog.objects.get(id=int(blog_detail_id) - 1)

    if len(services) == blog_detail.id:
        next_blog = Blog.objects.get(id=int(blog_detail_id) - 2)
    else:
        next_blog = Blog.objects.get(id=int(blog_detail_id) + 1)

    return render(request, 'blog-detail.html', {
        'blog_detail': blog_detail,
        'active_page': 'blog-detail',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'blog_quotes': blog_quotes,
        'prev_blog': prev_blog,
        'next_blog': next_blog,
        'latest_blogs': latest_blogs,
        'blog_categories': blog_categories,
        'blog_comments': blog_comments,
        'categories': categories,

        'which_one_id': which_one_id,
        'limit': limit,
        'total': total,

        'cart': cart,
        'cart_items': cart_items,
    })


def priceHandler(request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    prices = Price.objects.filter()[:3]



    return render(request, 'price.html',{
        'active_page': 'price',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'prices': prices,

        'cart': cart,
        'cart_items': cart_items,
    })


def faqHandler(request):
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    faqs = Faq.objects.filter()
    service_processs = ServiceProcess.objects.filter(is_in_service=True)[:3]
    ex_staffs = Staff.objects.filter(is_experienced=True)



    return render(request, 'faq.html', {
        'active_page': 'price',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'faqs': faqs,
        'service_processs': service_processs,
        'ex_staffs': ex_staffs,
    })


def shopHandler(request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    q = request.GET.get('q', '')
    category_id = int(request.GET.get('category_id', 0))

    limit = int(request.GET.get('limit', 3))
    p = int(request.GET.get('p', 1))
    stop = p * limit
    start = (p - 1) * limit

    if q:
        products = Product.objects.filter(status=0).filter(title__contains=q)[start:stop]
        item_count = Product.objects.filter(status=0).filter(title__contains=q).count()
    else:
        if category_id:
            products = Product.objects.filter(status=0).filter(category__id=category_id)[start:stop]
            item_count = Product.objects.filter(status=0).filter(category__id=category_id).count()
        else:
            products = Product.objects.filter()[start:stop]
            item_count = Product.objects.count()

    page_count = math.ceil(item_count / limit)
    page_range = range(1, page_count + 1)
    prev_p = p - 1
    next_p = p + 1


    categories = ProductCategory.objects.filter()
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()[:6]

    return render(request, 'shop.html', {
        'active_page': 'shop',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'products': products,
        'categories': categories,

        'limit': limit,
        'item_count': item_count,
        'p': p,
        'page_count': page_count,
        'page_range': page_range,
        'prev_p': prev_p,
        'next_p': next_p,

        'category_id': category_id,
        'q': q,

        'cart': cart,
        'cart_items': cart_items,

    })


def shop_detailHandler(request, product_id):
    if request.POST:
        print('*'*100)
        print(request.POST)
        new_product_comment = Productcomment()
        new_product_comment.name = request.POST.get('name', '')
        new_product_comment.text = request.POST.get('text', '')
        new_product_comment.comment_id = int(request.POST.get('comment_id', ''))
        new_product_comment.product_id = int(request.POST.get('product_id', ''))
        new_product_comment.date = datetime.now()
        new_product_comment.save()

    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    category_id = int(request.GET.get('category_id', 0))
    limit = int(request.GET.get('limit', 3))
    item_count = Product.objects.count()

    product = Product.objects.get(id=int(product_id))
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()[:6]
    relateds = Product.objects.filter(is_related=True )[:3]
    product_comments = Productcomment.objects.filter()
    categories = ProductCategory.objects.filter()

    return render(request, 'shop-detail.html', {
        'product': product,
        'active_page': 'shop',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'relateds': relateds,
        'product_comments': product_comments,
        'categories': categories,

        'category_id': category_id,
        'limit': limit,
        'item_count': item_count,

        'cart': cart,
        'cart_items': cart_items,
    })


def contactHandler(request):
    if request.method == 'GET':
        cart = {}
        cart_items = []
        open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
        if open_carts:
            open_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
            cart = open_cart

        client_sayss = ClientSays.objects.filter(status=0)
        informations = Information.objects.all()
        brands = Brand.objects.filter()[:5]
        services = Service.objects.filter()
        contacts = Contact.objects.filter()

        return render(request, 'contact.html', {
            'active_page': 'contact',
            'client_sayss': client_sayss,
            'informations': informations,
            'brands': brands,
            'services': services,
            'contacts': contacts,

            'cart': cart,
            'cart_items': cart_items,
        })
    else:
        r = ContactPost()
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        r.first_name = first_name
        r.last_name = last_name
        r.email = email
        r.phone = phone
        r.message = message
        r.save()

        return JsonResponse({'success': True, 'errorMsg': '', '_success': True})



def Handler404(request):
    informations = Information.objects.all()
    services = Service.objects.filter()
    contacts = Contact.objects.filter()

    return render(request, '404.html', {
        'informations': informations,
        'services': services,
        'contacts': contacts,
    })



def applicationHandler(request):
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()



    return render(request, 'application.html', {
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
    })

def cartHandler (request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        if action == 'add_to_cart':
            new_cart = None
            product_id = int(request.POST.get('product_id', 0))
            amount = int(request.POST.get('amount', 0))
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            if not open_carts:
                new_cart = Cart()
                new_cart.session_id = request.session.session_key
                new_cart.save()
            else:
                new_cart = open_carts[0]

            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(product__id=product_id).filter(status=0)
            if cart_items:
                new_cart_item = cart_items[0]
                new_cart_item.amount += amount
                new_cart_item.save()
            else:
                new_cart_item = CartItem()
                new_cart_item.product = Product.objects.get(id=product_id)
                new_cart_item.cart = Cart.objects.get(id=new_cart.id)
                new_cart_item.amount = amount
                new_cart_item.product_price = new_cart_item.product.price
                new_cart_item.save()

        elif action == 'remove_from_cart':
            product_id = int(request.POST.get('product_id', 0))
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            if open_carts:
                new_cart = open_carts[0]
            if new_cart:
                cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(product__id=product_id).filter(status=0)
                for ci in cart_items:
                    ci.status = -1
                    ci.save()

        elif action == 'checkout':
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            if open_carts:
                new_cart = open_carts[0]
                new_cart.fn = request.POST.get('fn', '')
                new_cart.ln = request.POST.get('ln', '')
                new_cart.city = request.POST.get('city', '')
                new_cart.country = request.POST.get('country', '')
                new_cart.zip_code = request.POST.get('zip_code', '')
                new_cart.email = request.POST.get('email', '')
                new_cart.phone = request.POST.get('phone', '')
                new_cart.address = request.POST.get('address', '')
                new_cart.status = 1
                new_cart.save()

        if action in ['add_to_cart', 'remove_from_cart']:
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            if open_carts:
                new_cart = open_carts[0]
                cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

                all_summ = 0
                item_count = 0
                for ci in cart_items:
                    all_summ += ci.amount * ci.product_price
                    item_count += ci.amount
                    ci.summ = ci.product_price * ci.amount
                    ci.save()
                new_cart.orig_price = all_summ
                new_cart.price = all_summ
                new_cart.amount = item_count
                new_cart.save()
        return JsonResponse({'success': True, 'errorMsg': '', '_success': True})
    else:
        cart = {}
        cart_items = []
        open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
        if open_carts:
            open_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
            cart = open_cart


        client_sayss = ClientSays.objects.filter(status=0)
        informations = Information.objects.all()
        brands = Brand.objects.filter()[:5]
        services = Service.objects.filter()
        categories = ProductCategory.objects.filter()



        return render(request, 'cart.html', {
            'active_page': 'shop',
            'client_sayss': client_sayss,
            'informations': informations,
            'brands': brands,
            'services': services,
            'categories': categories,

            'cart': cart,
            'cart_items': cart_items,
        })



def orderHandler(request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    orders = Cart.objects.filter(status=1)



    return render(request, 'order.html', {
        'active_page': 'order',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'orders': orders,

        'cart': cart,
        'cart_items': cart_items,
    })



def order_itemHandler(request, order_id):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    order_items = CartItem.objects.filter(status=0).filter(cart__id=order_id)



    return render(request, 'order_item.html', {
        'active_page': 'order',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'order_items': order_items,

        'cart': cart,
        'cart_items': cart_items,
    })





def chekHandler (request):
    cart = {}
    cart_items = []
    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart



    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()



    return render(request, 'chek.html', {
        'active_page': 'shop',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'cart': cart,
        'cart_items': cart_items,
    })