from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from admin_user.models import *
from academic_user.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_login(request):   # username : admin  password : asu
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('admin_user/admin_dashboard')
             #return redirect('admin_user/admin_navbar')
        else:
            request.session['saved_message'] = 'Error'
            return redirect('/as_admin')
    saved_message = request.session.pop('saved_message', None)
    return render(request,'admin_login.html',{'saved_message':saved_message})


def academic_login(request):   # username : admin  password : asu
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        if Academic_db.objects.filter( username=username, password=password).exists():
            academic = Academic_db.objects.get(username = request.POST['username'],password = request.POST['password'])
            if academic.status == '0':
                request.session['saved_message'] = 'Error'
                return redirect('/as_academic')

            request.session['AUser_id'] = academic.id
            return redirect('academic_user/academic_dashboard')
        else:
            request.session['saved_message'] = 'Error'
            return redirect('/as_academic')
    saved_message = request.session.pop('saved_message', None)
    return render(request,'academic_login.html',{'saved_message':saved_message})





    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         request.session['Adm_id'] = user.id
    #         return redirect('admin_user/admin_dashboard')
    #          #return redirect('admin_user/admin_navbar')
    #     else:
    #         request.session['saved_message'] = 'Error'
    #         return redirect('/as_admin')
    # saved_message = request.session.pop('saved_message', None)
    # return render(request,'academic_login.html',{'saved_message':saved_message})




# def enrolmentnumber_check(request,no):
#     print(no)

#     user = userRegistration_db.objects.get(EnrolmentNo = no)

#     print(user)


from django.http import JsonResponse
def enrolmentnumber_check(request, no):
    try:
        user = userRegistration_db.objects.get(EnrolmentNo=no)
        if user.status == '1':
            user_details = {
                'enrolment_no': user.EnrolmentNo,
                'name': f"{user.firstName} {user.lastName}",
                'course': user.course,
                'status': user.user_status,
                'certificate': user.Certificate_status,
            }
        else:
            user_details = None

        result = f"Enrollment number {no} exists. User: {user.firstName}"

    except userRegistration_db.DoesNotExist:
        result = f"Enrollment number {no} does not exist."
        user_details = None

    # Return the result and user details as JSON response
    response_data = {'result': result, 'user_details': user_details}
    return JsonResponse(response_data)
