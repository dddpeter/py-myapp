# coding:utf-8

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import simplejson
import traceback

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from data_importer.utils import mongo_util


@login_required
def index(request):
    return render(request, 'index.html')


def check_dictionary(code):
    db = mongo_util.get_db('mydb')
    result = mongo_util.get(db, 'dictionary', {'_id': str(code)}).count()
    if result < 1:
        return False
    else:
        return True


def check_area(code):
    db = mongo_util.get_db('mydb')
    result = mongo_util.get(db, 'area', {'_id': str(code)}).count()
    if result < 1:
        return False
    else:
        return True


@require_POST
@csrf_exempt
def user(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        check_message = ""
        user_id = m["_id"] = m["vol_ID"]
        vol_id = m['vol_ID']
        idcard_number = m['idcard_number']
        vol_true_name = m['vol_true_name']
        vol_province = m['vol_province']
        vol_city = m['vol_city']
        vol_district = m['vol_district']
        vol_street = m['vol_street']
        vol_committee = m['vol_committee']
        vol_address = m['vol_address']
        member_group_code = m['member_group_code']
        post_code = m['post_code']
        vol_gender = m['vol_gender']
        vol_birth_year = m['vol_birth_year']
        vol_birth_month = m['vol_birth_month']
        vol_birth_day = m['vol_birth_day']
        vol_birth_date = m['vol_birth_date']
        vol_ethnicity = m['vol_ethnicity']
        vol_hour = m['vol_hour']
        login_mobile = m['login_mobile']
        try:
            if not str(vol_id).isdigit():
                check_message += "志愿者代码格式错误|"
            if not str(idcard_number).strip():
                check_message += "证件号不能为空|"
            if not vol_true_name.strip():
                check_message += "志愿者姓名不能为空|"
            if not str(vol_province).isdigit():
                check_message += "省级代码格式错误|"
            else:
                if not check_area(str(vol_province)):
                    check_message += "省级代码在字典表中不存在|"

            if not str(vol_city).isdigit():
                check_message += "市级代码格式错误|"
            else:
                if not check_area(str(vol_city)):
                    check_message += "市级代码在字典表中不存在|"

            if not str(vol_district).isdigit():
                check_message += "区县级代码格式错误|"
            else:
                if not check_area(str(vol_district)):
                    check_message += "区县级代码在字典表中不存在|"

            if not str(vol_street).isdigit():
                check_message += "街道/乡镇代码格式错误|"
            else:
                if not check_area(str(vol_street)):
                    check_message += "街道/乡镇代码在字典表中不存在|"
            if not str(vol_committee).isdigit():
                check_message += "社区/村组代码格式错误|"
            else:
                if not check_area(str(vol_committee)):
                    check_message += "社区/村组代码在字典表中不存在|"
            if not vol_address.strip():
                check_message += "详细地址不能为空|"
            if not member_group_code.strip():
                check_message += "所属团组织不能为空|"
            if not str(post_code).isdigit():
                check_message += "邮政编码格式错误|"
            if not str(vol_gender).strip():
                check_message += "性别代码格式错误|"
            if not str(vol_birth_year).isdigit():
                check_message += "出生年格式格式错误|"
            if not str(vol_birth_month).isdigit():
                check_message += "出生月格式错误|"
            if not str(vol_birth_day).isdigit():
                check_message += "出生日格式错误|"
            if not vol_birth_date.strip():
                check_message += "生日字符串不能为空|"
            if not str(vol_ethnicity).isdigit():
                check_message += "民族代码格式错误|"
            else:
                if not check_dictionary(str(vol_ethnicity)):
                    check_message += "民族代码在字典表中不存在|"
            if not str(vol_hour).strip():
                check_message += "服务时长不能为空|"
            if not login_mobile.strip():
                check_message += "登陆手机号不能为空|"
            if check_message.strip():
                raise Exception(check_message)
            mongo_util.insert(db, 'user', m)
            result.append({"id": user_id, "code": 1, "type": "USER", "desc": "处理成功"})
        except Exception, e:
            print traceback.format_exc()
            result.append({"id": user_id, "code": 0,  "type": "USER", "desc": "处理失败:" + str(e)})
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def organ(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        check_message = ""
        organ_id = m["_id"] = m["org_ID"]
        org_id = m["org_ID"]
        org_parent_name = m["org_parent_name"]
        org_parent_id = m["org_parent_id"]
        org_station_flag = m["org_station_flag"]
        org_linkman = m["org_linkman"]
        org_linkman_mobile = m["org_linkman_mobile"]
        org_manager = m["org_manager"]
        org_manager_cert_number = m["org_manager_cert_number"]
        org_manager_mobile = m["org_manager_mobile"]
        org_name = m["org_name"]
        org_build_date = m["org_build_date"]
        org_province = m["org_province"]
        org_city = m["org_city"]
        org_district = m["org_district"]
        org_street = m["org_street"]
        org_committee = m["org_committee"]
        org_address = m["org_address"]
        org_hour = str(m["org_hour"])
        org_member = m["org_member"]
        org_introduce = m["org_introduce"]
        create_time = m["create_time"]
        system_code = str(m["system_code"])
        try:
            if not str(org_id).isdigit():
                check_message += "组织代码不能为空|"
            if not str(org_parent_id).isdigit():
                check_message += "组织上级代码不能为空|"
            if not org_parent_name.strip():
                check_message += "组织上级名称不能为空|"
            if int(org_station_flag) not in [0, 1]:
                check_message += "是否志愿者服务站代码格式错误|"
            if not org_linkman.strip():
                check_message += "联系人姓名不能为空|"
            if not org_linkman_mobile.strip():
                check_message += "联系人手机不能为空|"
            if not org_manager.strip():
                check_message += "负责人姓名不能为空|"
            if not org_manager_cert_number.strip():
                check_message += "负责人省份证号不能为空|"
            if not org_manager_mobile.strip():
                check_message += "负责人手机不能为空|"
            if not org_name.strip():
                check_message += "组织名称不能为空|"
            if not org_build_date.strip():
                check_message += "组织成立日期不能为空|"
            if not str(org_province).isdigit():
                check_message += "省级代码格式错误|"
            else:
                if not check_area(str(org_province)):
                    check_message += "省级代码在字典表中不存在|"

            if not str(org_city).isdigit():
                check_message += "市级代码格式错误|"
            else:
                if not check_area(str(org_city)):
                    check_message += "市级代码在字典表中不存在|"

            if not str(org_district).isdigit():
                check_message += "区县级代码格式错误|"
            else:
                if not check_area(str(org_district)):
                    check_message += "区县级代码在字典表中不存在|"

            if not str(org_street).isdigit():
                check_message += "街道/乡镇代码格式错误|"
            else:
                if not check_area(str(org_street)):
                    check_message += "街道/乡镇代码在字典表中不存在|"
            if not str(org_committee).isdigit():
                check_message += "社区/村组代码格式错误|"
            else:
                if not check_area(str(org_committee)):
                    check_message += "社区/村组代码在字典表中不存在|"
            if not org_address.strip():
                check_message += "详细地址不能为空|"
            if not org_hour.strip():
                check_message += "服务时长不能为空|"
            if not str(org_member).isdigit():
                check_message += "组织志愿者人数不能为空|"

            if not org_introduce.strip():
                check_message += "组织介绍不能为空|"
            if not create_time.strip():
                check_message += "组织成立日期不能为空|"
            if not system_code.strip():
                check_message += "系统来源不能为空|"

            if check_message.strip():
                raise Exception(check_message)
            mongo_util.insert(db, 'organ', m)
            result.append({"id": organ_id, "code": 1, "type": "ORGAN", "desc": "处理成功"})
        except Exception, e:
            print traceback.format_exc()
            result.append({"id": organ_id, "code": 0, "type": "ORGAN", "desc": "处理失败:" + str(e)})
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def activity(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        check_message = ""
        activity_id = m["_id"] = m["opp_ID"]
        opp_id = m["opp_ID"]
        opp_name = m["opp_name"]
        org_name = m["org_name"]
        org_id = m["org_ID"]
        opp_start_date = m["opp_start_date"]
        opp_end_date = m["opp_end_date"]
        opp_lng = m["opp_lng"]
        opp_lat = m["opp_lat"]
        opp_linkman = m["opp_linkman"]
        opp_linkman_mobile = m["opp_linkman_mobile"]
        opp_linkman_email = m["opp_linkman_email"]
        opp_province = m["opp_province"]
        opp_city = m["opp_city"]
        opp_district = m["opp_district"]
        opp_street = m["opp_street"]
        opp_committee = m["opp_committee"]
        opp_address = m["opp_address"]
        opp_memo = m["opp_memo"]
        opp_hour = str(m["opp_hour"])
        system_code = str(m["system_code"])
        try:
            if not str(opp_id).isdigit():
                check_message += "组织代码不能为空|"
            if not opp_name.strip():
                check_message += "活动名称不能为空|"
            if not str(org_id).isdigit():
                check_message += "组织代码不能为空|"
            if not org_name.strip():
                check_message += "组织名称不能为空|"
            if not opp_start_date.strip():
                check_message += "活动开始时间不能为空|"
            if not opp_end_date.strip():
                check_message += "活动结束时间不能为空|"
            if not opp_lng.strip():
                check_message += "活动经度不能为空|"
            if not opp_lat.strip():
                check_message += "活动纬度不能为空|"

            if not opp_linkman.strip():
                check_message += "联系人不能为空|"
            if not opp_linkman_mobile.strip():
                check_message += "联系人手机不能为空|"
            if not opp_linkman_email.strip():
                check_message += "联系人电子邮箱不能为空|"

            if not str(opp_province).isdigit():
                check_message += "省级代码格式错误|"
            else:
                if not check_area(str(opp_province)):
                    check_message += "省级代码在字典表中不存在|"

            if not str(opp_city).isdigit():
                check_message += "市级代码格式错误|"
            else:
                if not check_area(str(opp_city)):
                    check_message += "市级代码在字典表中不存在|"

            if not str(opp_district).isdigit():
                check_message += "区县级代码格式错误|"
            else:
                if not check_area(str(opp_district)):
                    check_message += "区县级代码在字典表中不存在|"

            if not str(opp_street).isdigit():
                check_message += "街道/乡镇代码格式错误|"
            else:
                if not check_area(str(opp_street)):
                    check_message += "街道/乡镇代码在字典表中不存在|"
            if not str(opp_committee).isdigit():
                check_message += "社区/村组代码格式错误|"
            else:
                if not check_area(str(opp_committee)):
                    check_message += "社区/村组代码在字典表中不存在|"
            if not opp_address.strip():
                check_message += "详细地址不能为空|"

            if not opp_memo.strip():
                check_message += "活动简介不能为空|"
            if not opp_hour.strip():
                check_message += "活动持续时间不能为空|"
            if not system_code.strip():
                check_message += "系统来源不能为空|"

            if check_message.strip():
                raise Exception(check_message)
            mongo_util.insert(db, 'activity', m)
            result.append({"id": activity_id, "code": 1, "type": "ACTIVITY", "desc": "处理成功"})
        except Exception, e:
            print traceback.format_exc()
            result.append({"id": activity_id, "code": 0, "type": "ACTIVITY", "desc": "处理失败:" + str(e)})
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def user_organ(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        check_message = ""
        org_id = m["org_ID"]
        organ_name = m["org_name"]
        vol_id = m["vol_ID"]
        system_code = m["system_code"]
        user_organ_id = m["_id"] = m["org_ID"] + "_" + m["vol_ID"]
        try:
            if not str(org_id).isdigit():
                check_message += "机构代码格式错误|"
            if not str(vol_id).isdigit():
                check_message += "志愿者代码格式错误|"
            if not str(system_code).isdigit():
                check_message += "来源系统代码格式错误|"
            if not organ_name.strip():
                check_message += "机构名称格式错误，不能为空|"
            if check_message.strip():
                raise Exception(check_message)
            mongo_util.insert(db, 'user_organ', m)
            result.append({"id": user_organ_id, "code": 1, "type": "USER_ORGAN", "desc": "处理成功"})
        except Exception, e:
            print traceback.format_exc()
            result.append({"id": user_organ_id, "code": 0, "type": "USER_ORGAN", "desc": "处理失败" + str(e)})
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json;charset=utf-8")


@require_POST
@csrf_exempt
def user_activity(request):
    result = []
    message = simplejson.loads(request.body)
    db = mongo_util.get_db('mydb')
    for m in message:
        check_message = ""
        vol_id = m["vol_ID"]
        opp_id = m["opp_ID"]
        vol_time = m["vol_Time"]
        get_type = m["gettype"]
        system_code = m["system_code"]
        user_activity_id = m["_id"] = m["opp_ID"] + "_" + m["vol_ID"]
        try:
            if not str(opp_id).isdigit():
                check_message += "活动代码格式错误|"
            if not str(vol_id).isdigit():
                check_message += "志愿者代码格式错误|"
            if not str(system_code).isdigit():
                check_message += "来源系统代码格式错误|"
            if not get_type.strip():
                check_message += "时长获取方式格式错误，不能为空|"
            if not str(vol_time).strip():
                check_message += "志愿者活动时长不能为空|"
            if check_message.strip():
                raise Exception(check_message)
            mongo_util.insert(db, 'user_activity', m)
            result.append({"id": user_activity_id, "code": 1, "type": "USER_ACTIVITY", "desc": "处理成功"})
        except Exception, e:
            print traceback.format_exc()
            result.append({"id": user_activity_id, "code": 0, "type": "USER_ACTIVITY", "desc": "处理失败:" + str(e)})
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json;charset=utf-8")