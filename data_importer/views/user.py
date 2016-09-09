# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import simplejson
from data_importer.utils import mongo_util

db = mongo_util.get_db('mydb')


@login_required
def index(request):
    return render(request, 'user_list.html', {'user': request.user})


@require_http_methods(["GET", "POST"])
@csrf_exempt
@login_required
def user_list(request):
    page_num = request.GET.get('pageNum') if request.GET.get('pageNum') else 1
    page_size = request.GET.get('pageSize') if request.GET.get('pageSize') else 10
    result = {}
    result_list = mongo_util.pagger(db, 'user', page_size, page_num)
    result.append({"list": result_list, "code": 1, "type": "USER", "desc": "处理成功"});
    return HttpResponse(simplejson.dumps({}, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")