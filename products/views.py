from django.shortcuts import render
from .models import Product
from django.views import View
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.


class Home(View):
    def get(self, request):
        print(request.GET)
        CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
        print(request.GET.get('filter_query'))
        if request.GET.get('filter_query') is None:
            data = Product.objects.all()
        else:
            if cache.get(request.GET.get('filter_query')):
                data = cache.get(request.GET.get('filter_query'))
                print('Data coming from cache')
            else:
                data=Product.objects.filter(name__contains=request.GET.get('filter_query'))
                cache.set(request.GET.get('filter_query'), data)
                print('Data coming from DB')
        return render(request, 'home.html', {'datas': data})


