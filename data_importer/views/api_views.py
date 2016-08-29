# coding:utf-8

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import simplejson

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
from data_importer.utils import mongo_util


@login_required
def index(request):
    return render(request, 'index.html')


@require_POST
@csrf_exempt
def user(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        user_id = m["_id"] = m["vol_ID"]
        try:
            mongo_util.insert(db, 'user', m)
            result.append({"id": user_id, "code": 1, "type": "USER", "desc": "处理成功"})
        except Exception :
            print Exception.message
            result.append({"id": user_id, "code": 0,  "type": "USER", "desc": "处理失败"})
    return HttpResponse(simplejson.dumps(result), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def organ(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        organ_id = m["_id"] = m["org_ID"]
        try:
            mongo_util.insert(db, 'organ', m)
            result.append({"id": organ_id, "code": 1, "type": "ORGAN", "desc": "处理成功"})
        except Exception :
            print Exception.message
            result.append({"id": organ_id, "code": 0, "type": "ORGAN", "desc": "处理失败"})
    return HttpResponse(simplejson.dumps(result), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def activity(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        activity_id = m["_id"] = m["opp_ID"]
        try:
            mongo_util.insert(db, 'activity', m)
            result.append({"id": activity_id, "code": 1, "type": "ACTIVITY", "desc": "处理成功"})
        except Exception :
            print Exception.message
            result.append({"id": activity_id, "code": 0, "type": "ACTIVITY", "desc": "处理失败"})
    return HttpResponse(simplejson.dumps(result), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def user_organ(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        user_organ_id = m["_id"] = m["org_ID"] + "_" + m["vol_ID"]
        try:
            mongo_util.insert(db, 'organ', m)
            result.append({"id": user_organ_id, "code": 1, "type": "USER_ORGAN", "desc": "处理成功"})
        except Exception :
            print Exception.message
            result.append({"id": user_organ_id, "code": 0, "type": "USER_ORGAN", "desc": "处理失败"})
    return HttpResponse(simplejson.dumps(result), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def user_activity(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        user_activity_id = m["_id"] = m["opp_ID"] + "_" + m["vol_ID"]
        try:
            mongo_util.insert(db, 'organ', m)
            result.append({"id": user_activity_id, "code": 1, "type": "USER_ACTIVITY", "desc": "处理成功"})
        except Exception :
            print Exception
            result.append({"id": user_activity_id, "code": 0, "type": "USER_ACTIVITY", "desc": "处理失败"})
    return HttpResponse(simplejson.dumps(result), content_type="application/json;charset=utf-8")