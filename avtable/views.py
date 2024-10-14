from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.templatetags.static import static
from django.http import HttpResponse

from .models import Mavito, Region, Mavhouse, Street, Youkv, Flat

cols=['obj','addr','m2','floor','floors','descr','linkimg','date']

def home(request):
    #qs_youla = Youkv.objects.all()
    #qs_avito = Mavito.objects.all()
    #qu = qs_avito.union(qs_youla).order_by('-date')[:120]
    qu = Flat.objects.all()[:120]
    for obj in qu:
        if 'nofoto1.jpg' in obj.linkimg:
            obj.linkimg = static('nofoto1.jpg')
        else:
            obj.linkimg = obj.linkimg.split('|')[0]
    page_number = request.GET.get('page', 1)
    paginator = Paginator(qu, 12)
    page_obj = paginator.get_page(page_number)
    count = qu.count()
    base_url = request.META['HTTP_HOST']
    context = {
    'page_obj': page_obj,
    'count': count,
    'base_url': base_url,
    'flat': True
    }
    return render(request, 'home_src.html', context=context)

def articles(request):
    """
    Fetch paginated articles and render them.
    """
    page_number = request.GET.get('page', 1)
    pobj = Mavito.objects.order_by('-date')[:120]
    # get only first url from linkimg field
    for obj in pobj:
            if 'nofoto1.jpg' in obj.linkimg:
                obj.linkimg = static('nofoto1.jpg')
            else:
                obj.linkimg = obj.linkimg.split('|')[0]
    
    base_url = request.META['HTTP_HOST']
    paginator = Paginator(pobj, 12)
    page_obj = paginator.get_page(page_number)
    count = Mavito.objects.count()
    reg = Region.objects.all()
    regs = {}
    for r in reg:
        regs['id'] = r.id
        regs['name'] = r.name
    base_url = request.META['HTTP_HOST']
    context = {
    'page_obj': page_obj,
    'count': count,
    'base_url': base_url,
    'flat': True
    }
    return render(request, 'home_src.html', context=context)
########################################################################################
def obj_detail(request, id):
    if 'flat' in request.path:
        obj = get_object_or_404(Flat, pk=id)
    elif 'house' in request.path:
        obj = get_object_or_404(Mavhouse, pk=id)
    else:
        obj = get_object_or_404(Flat, pk=id)

    if obj.linkimg:
        
        if 'nofoto1.jpg' in obj.linkimg:
            obj.linkimg = [static('nofoto1.jpg'),]
        else:
            obj.linkimg = obj.linkimg.split('|')
    else:
        obj.linkimg = [static('nofoto1.jpg'),]
    #print(obj.linkimg)
    return render(request, 'obj_detail.html', {'obj': obj})
#######################################################################################
def search(request):
    reg = ['Ави','Вах','Кир','Мос','Нов','При','Сов']
    if request.method == 'POST':
        mid_price = request.POST.get('price')
        addr = request.POST.get('addr')
    else:
        mid_price = request.GET.get('price',0)
        addr = request.GET.get('addr','')
        obj_type = request.GET.get('otype','')
        regs = [request.GET.get(f'{name}','') for name in reg]
    
    ### TODO
    
        reg_filter = []
        for i,r in enumerate(regs):
            if r =='on':
                reg_filter.append(reg[i])
    
    

    
    sq = request.META['QUERY_STRING']
    base_url = request.META['HTTP_HOST']

    if obj_type in ['Дом','Дача','Коттедж','Таунхаус']:
        house = True
        flat = False
        q =  Mavhouse.objects.filter(price__gt=mid_price)
    else:
        flat = True
        house = False
        q =  Flat.objects.filter(price__gt=mid_price)    

    q = q.filter(obj__icontains=obj_type)

    if len(reg_filter) == 1:
        q = q.filter(region__startswith=reg_filter[0])
    elif len(reg_filter) == 2:
        q = q.filter(Q(region__startswith=reg_filter[0]) | Q(region__startswith=reg_filter[1]))
    else:
        pass

    if addr:
        q = q.filter(addr__icontains=addr)
    result = q
    # DEBUG 
    #print(q.query)

    if result:
        for obj in result:
            if obj.linkimg is None:
                obj.linkimg = static('nofoto1.jpg')
            elif 'nofoto1.jpg' in obj.linkimg:
                obj.linkimg = static('nofoto1.jpg')
            else:
                obj.linkimg = obj.linkimg.split('|')[0]

    count = len(result)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(result, 12)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'count': count,
        'base_url': base_url,
        'q': sq,
        'obj_type': obj_type,
        'house': house,
        'flat': flat
    }
    #print(obj_type)
    return render(request, 'home_src.html', context)

def find_st(request):
    if request.method == 'POST':
        search_query = request.POST['addr']
        sts = Street.objects.filter(name__icontains=search_query)
        if sts:
            slist = [x.name for x in sts ]
            res = sorted(slist, key=len)[0]
        else:
            res = ''
        return HttpResponse(res, content_type="text/plain")
    else:
        search_query = request.GET['addr']
        sts = Street.objects.filter(name__icontains=search_query)
        if sts:
            slist = [x.name for x in sts ]
            res = sorted(slist, key=len)[0]
        else:
            res = ''
        return HttpResponse(res, content_type="text/plain")
        