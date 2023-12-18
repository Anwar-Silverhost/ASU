from django.shortcuts import render,redirect
from admin_user.models import *
from academic_user.models import *

# Create your views here.

def academic_logout(request):
    if 'AUser_id' in request.session:
        request.session.flush()
    return redirect('/as_academic')


def academic_navbar(request):
    if 'AUser_id' in request.session:
        if request.session.has_key('AUser_id'):
            AUser_id = request.session['AUser_id']
        else:
            return redirect('/')
        AUser = Academic_db.objects.filter(id=AUser_id)
        return render(request,'academic/academic_navbar.html',{'AUser':AUser})
    else:
        return redirect('/as_academic')

def academic_dashboard(request):
    if 'AUser_id' in request.session:
        if request.session.has_key('AUser_id'):
            AUser_id = request.session['AUser_id']

        else:
            return redirect('/')
        AUser = Academic_db.objects.filter(id=AUser_id)
        AUser_ac = Academic_db.objects.get(id=AUser_id)


        occupaidSeatCount = userRegistration_db.objects.filter(academic = AUser_ac).filter(status = '1').count()
        UnoccupaidSeatCount = int(AUser_ac.seatCount) - int(occupaidSeatCount)
        acusers = userRegistration_db.objects.filter(academic=AUser_ac, status='1').order_by('-EnrolmentNo')[:9]


        ac_status = Academic_db.objects.get(id=AUser_id)
        if ac_status.status == '0':
            if 'AUser_id' in request.session:
                request.session.flush()
            return redirect('/as_academic')

        return render(request,'academic/academic_dashboard.html',{'AUser':AUser,'occupaidSeatCount':occupaidSeatCount,'UnoccupaidSeatCount':UnoccupaidSeatCount,'acusers':acusers})
    else:
        return redirect('/as_academic')



def academic_registrations(request):
    if 'AUser_id' in request.session:
        if request.session.has_key('AUser_id'):
            AUser_id = request.session['AUser_id']
        else:
            return redirect('/')
        AUser = Academic_db.objects.filter(id=AUser_id)

        
        ace_user = userRegistration_db.objects.filter(academic = Academic_db.objects.get(id=AUser_id)).order_by('EnrolmentNo')

        for i in ace_user:
            if i.status == '0' :
                print(i.EnrolmentNo, '====', i.status)
                enr_user = userRegistration_db.objects.get(EnrolmentNo = i.EnrolmentNo)
                break
        else:
            request.session['noavilbleseat_message'] = 'Error'
            return redirect(academic_register)


        ac_status = Academic_db.objects.get(id=AUser_id)
        if ac_status.status == '0':
            if 'AUser_id' in request.session:
                request.session.flush()
            return redirect('/as_academic')

        return render(request,'academic/academic_registrations.html',{'AUser':AUser,'enr_user':enr_user})
    else:
        return redirect('/as_academic')

def academic_register(request):
    if 'AUser_id' in request.session:
        if request.session.has_key('AUser_id'):
            AUser_id = request.session['AUser_id']
        else:
            return redirect('/')
        AUser = Academic_db.objects.filter(id=AUser_id)
        users = userRegistration_db.objects.filter(academic__id=AUser_id, status='1').order_by('-id')

        noavilbleseat_message = request.session.pop('noavilbleseat_message', None)

        ac_status = Academic_db.objects.get(id=AUser_id)
        if ac_status.status == '0':
            if 'AUser_id' in request.session:
                request.session.flush()
            return redirect('/as_academic')
        return render(request,'academic/academic_register.html',{'AUser':AUser,'users':users,'noavilbleseat_message':noavilbleseat_message})
    else:
        return redirect('/as_academic')

def save_user(request,id):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        dateofbirth = request.POST['dateofbirth']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        country = request.POST['country']
        qualification = request.POST['qualification']
        course = request.POST['course']
        parentName = request.POST['parentName']
        contactNumber = request.POST['contactNumber']

        u = userRegistration_db.objects.get(id=id)
        u.firstName = firstName
        u.lastName = lastName
        u.dateofbirth = dateofbirth
        u.gender = gender
        u.email = email
        u.phone = phone
        u.city = city
        u.country = country
        u.qualification = qualification
        u.course = course
        u.parentName = parentName
        u.contactNumber = contactNumber
        u.status = '1'
        u.save()

        return redirect(academic_register)





def academic_profile(request):
    if 'AUser_id' in request.session:
        if request.session.has_key('AUser_id'):
            AUser_id = request.session['AUser_id']
        else:
            return redirect('/')
        AUser = Academic_db.objects.filter(id=AUser_id)
        academic = Academic_db.objects.get(id=AUser_id)

        ac_status = Academic_db.objects.get(id=AUser_id)
        if ac_status.status == '0':
            if 'AUser_id' in request.session:
                request.session.flush()
            return redirect('/as_academic')
        return render(request,'academic/academic_profile.html',{'AUser':AUser,'academic':academic})
    else:
        return redirect('/as_academic')


def academic_userProfile(request,id):
    if 'AUser_id' in request.session:
        if request.session.has_key('AUser_id'):
            AUser_id = request.session['AUser_id']
        else:
            return redirect('/')
        AUser = Academic_db.objects.filter(id=AUser_id)
        ac_status = Academic_db.objects.get(id=AUser_id)
        if ac_status.status == '0':
            if 'AUser_id' in request.session:
                request.session.flush()
            return redirect('/as_academic')

        try:
            ause = userRegistration_db.objects.filter(academic__id=AUser_id).get(id=id)
            return render(request,'academic/academic_userProfile.html',{'AUser':AUser,'ause':ause})
        except:
            return redirect(academic_register)
    else:
        return redirect('/as_academic')


  

def update_user(request,id):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        dateofbirth = request.POST['dateofbirth']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        country = request.POST['country']
        qualification = request.POST['qualification']
        course = request.POST['course']
        parentName = request.POST['parentName']
        contactNumber = request.POST['contactNumber']


        u = userRegistration_db.objects.get(id=id)
        u.firstName = firstName
        u.lastName = lastName
        u.dateofbirth = dateofbirth
        u.gender = gender
        u.email = email
        u.phone = phone
        u.city = city
        u.country = country
        u.qualification = qualification
        u.course = course
        u.parentName = parentName
        u.contactNumber = contactNumber
        u.save()


    return redirect('/academic_user/academic_user/Profile/'+str(id))