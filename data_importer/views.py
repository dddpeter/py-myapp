# coding:utf-8

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import simplejson

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET


@login_required
def index(request):
    return render(request, 'index.html')

@require_POST
@csrf_exempt
def process_json_request(request):
    result = {}
    print request.body
    message = simplejson.loads(request.body)
    result['result'] = 1
    result['content'] = {"a": message['a'], "message": "请求已经成功了"}
    return HttpResponse(simplejson.dumps(result), content_type="application/json;charset=utf-8")