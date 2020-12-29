from django.shortcuts import render
from datetime import datetime

from main.models import ClientSays, Information, Brand, Service, BestService, Recovery, ServiceProcess, Product, \
    Feedback, Blog, Staff, About_service, About, About_action, BlogQoute, Blogcomment, Price, Faq, Contact, Productcomment
# Create your views here.



def indexHandler (request):
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
    })


def aboutHandler (request):
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
    })


def serviceHandler(request):
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
    })


def service_listHandler(request):
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
    })


def service_detailHandler(request, detail_id):
    detail = Service.objects.get(id=int(detail_id))
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    ex_staffs = Staff.objects.filter(is_experienced=True)
    recoveries = Recovery.objects.filter()
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
        'prev_service': prev_service,
        'next_service': next_service,

    })



def blogHandler(request):
    limit = int(request.GET.get('limit', 2))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    blogs = Blog.objects.filter()[start:stop]
    latest_blogs = Blog.objects.filter(is_latest=True)[:4]
    blog_categories = Blog.objects.filter()[:4]

    total = Blog.objects.count()
    prev_page = current_page-1
    next_page = 0
    if total > stop:
        next_page = current_page + 1




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
        'blog_categories': blog_categories,
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

    blog_detail = Blog.objects.get(id=int(blog_detail_id))
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    blog_quotes = BlogQoute.objects.filter()
    latest_blogs = Blog.objects.filter(is_latest=True)[:4]
    blog_categories = Blog.objects.filter()[:4]
    blog_comments = Blogcomment.objects.filter(blog_id=int(blog_detail_id))

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

    })


def priceHandler(request):
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
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    products = Product.objects.all()

    return render(request, 'shop.html', {
        'active_page': 'shop',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'products': products,
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


    product = Product.objects.get(id=int(product_id))
    client_sayss = ClientSays.objects.filter(status=0)
    informations = Information.objects.all()
    brands = Brand.objects.filter()[:5]
    services = Service.objects.filter()
    relateds = Product.objects.filter(is_related=True )[:3]
    product_comments = Productcomment.objects.filter()

    return render(request, 'shop-detail.html', {
        'product': product,
        'active_page': 'shop',
        'client_sayss': client_sayss,
        'informations': informations,
        'brands': brands,
        'services': services,
        'relateds': relateds,
        'product_comments': product_comments,
    })


def contactHandler(request):
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
    })