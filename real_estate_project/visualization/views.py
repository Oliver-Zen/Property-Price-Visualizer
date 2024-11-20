# visualization/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Realtor
from django.db.models import Avg
from django.conf import settings
import joblib
import os
import numpy as np

MODEL_PATH = os.path.join(settings.BASE_DIR, 'visualization', 'models', 'decision_tree_model.joblib')
model = joblib.load(MODEL_PATH)

def visualization_view(request):
    return render(request, 'visualization.html')

def choropleth_view(request):
    return render(request, 'choropleth.html')

def get_data(request):
    realtors = Realtor.objects.all().values(
        'brokered_by', 'status', 'price', 'bed', 'bath',
        'acre_lot', 'street', 'city', 'state', 'zip_code',
        'house_size', 'prev_sold_date'
    )
    data = list(realtors)
    return JsonResponse(data, safe=False)

def price_query_view(request):
    price = None
    error = None
    if request.method == 'POST':
        bed = request.POST.get('bed')
        bath = request.POST.get('bath')
        if bed is not None and bath is not None:
            try:
                bed = float(bed)
                bath = float(bath)
                # 简单的查询：取卧室和浴室数量匹配的房子的平均价格
                queryset = Realtor.objects.filter(bed=bed, bath=bath)
                if queryset.exists():
                    avg_price = queryset.aggregate(Avg('price'))['price__avg']
                    price = round(avg_price, 2)
                else:
                    error = "没有找到匹配的房源。"
            except ValueError:
                error = "请输入有效的数字。"
        else:
            error = "请填写所有字段。"
    return render(request, 'price_query.html', {'price': price, 'error': error})
