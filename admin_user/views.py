from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import random
import string
from datetime import datetime

from admin_user.models import *
from academic_user.models import *
from django.db import transaction
# Create your views here.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def admin_logout(request):
    if 'Adm_id' in request.session:
        request.session.flush()
    return redirect('/as_admin')


def admin_navbar(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        return render(request, 'admin/admin_navbar.html', {'admin': admin})
    else:
        return redirect('/as_admin')

def admin_dashboard(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)

        academic_count = Academic_db.objects.all().count()
        regs_count = userRegistration_db.objects.filter(status = '1').count()
        seat_count = userRegistration_db.objects.all().count()
        unseat = int(seat_count)-int(regs_count)


        academic_latest = Academic_db.objects.all().order_by('-id')[:10]


        reg_latest = userRegistration_db.objects.filter(status = '1').order_by('-id')[:10]



        return render(request, 'admin/admin_dashboard.html', {'admin': admin,'academic_count':academic_count,'regs_count':regs_count,'seat_count':seat_count,'unseat':unseat,'academic_latest':academic_latest,'reg_latest':reg_latest})
    else:
        return redirect('/as_admin')

def admin_academic(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        academic = Academic_db.objects.all().order_by('-id')

    #countsection 
        academic_count = Academic_db.objects.all().count()
        ac_setstotal_count = AdminBasic_db.objects.get(data_is = 'EnrolmentNumber').value_is
        occupaid_seat_count = userRegistration_db.objects.filter(status = '1').count()
        unoccupaid_count = int(ac_setstotal_count)-int(occupaid_seat_count)


        return render(request, 'admin/admin_academic.html', {'admin': admin,'academic':academic,'academic_count':academic_count,'ac_setstotal_count':ac_setstotal_count,'occupaid_seat_count':occupaid_seat_count,'unoccupaid_count':unoccupaid_count})
    else:
        return redirect('/as_admin')

def admin_create_academic(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        return render(request, 'admin/admin_create_academic.html', {'admin': admin})
    else:
        return redirect('/as_admin')
        
@transaction.atomic
def save_academic(request):
    if request.method == 'POST':
        academic_name = request.POST['academic_name']
        coordinator_name = request.POST['coordinator_name']
        email = request.POST['email']
        phone = request.POST['phone']
        seat_count = request.POST['seat_count']


        a = Academic_db()
        a.academicName = academic_name
        a.coordinatorName = coordinator_name
        a.email = email
        a.phone = phone
        a.seatCount = seat_count
        a.save()
        a.username = str('ASU'+academic_name[:3]+str(a.id))
        a.password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
        a.status = '1'
        a.academicId = f"ASUA{str(a.id).zfill(5)}"
        a.saveDate = datetime.now()
        a.save()

        enrollment_count = AdminBasic_db.objects.get(data_is = 'EnrolmentNumber')

        for i in range(1, int(seat_count) + 1):
            enrollment_number = f"ASU{int(enrollment_count.value_is) + i:05d}"

            usr_db = userRegistration_db()
            usr_db.academic = Academic_db.objects.get(id=a.id)
            usr_db.EnrolmentNo = enrollment_number
            usr_db.save()

        enrollment_count.value_is = int(enrollment_count.value_is)+int(seat_count)
        enrollment_count.save()

        #sent email like link username  and password 

        # Zoho Mail SMTP server details
        smtp_server = 'smtp.zoho.in'
        smtp_port = 587  # Use 465 for SSL or 587 for TLS
        username = 'admin@skilluniversity.us'
        password = 'American123*#'

        sender_email = 'admin@skilluniversity.us'
        recipient_email = email

        subject = 'Academic Login Details - American Skill University'
        url = f"{request.scheme}://{request.get_host()}"+'/as_academic'
        username_value = a.username
        password_value = a.password

        # Email body with placeholders
        body_template = """
        Dear Academic Admin,

        Please access the academic portal using the provided credentials below:

        URL:  {url}
        Username: {username}
        Password: {password}

        Should you encounter any issues or require further assistance, feel free to reach out.

        Best regards,

        American Skill University
        """

        # Replace placeholders with actual values
        body = body_template.format(url=url, username=username_value, password=password_value)


        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Use this line if you're using TLS
                server.login(username, password)
                server.sendmail(sender_email, recipient_email, message.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print(f'Error: {e}')


















        return redirect(admin_academic)


def admin_academic_view(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        academi = Academic_db.objects.get(id=id)
        ac_usr_occu_count = userRegistration_db.objects.filter(academic = academi).filter(status = '1').count()
        ac_usr_unoccu_count = userRegistration_db.objects.filter(academic = academi).filter(status = '0').count()
        ac_users = userRegistration_db.objects.filter(academic = academi).filter(status = '1').order_by('-id')
        return render(request, 'admin/admin_academic_view.html', {'admin': admin,'a':academi,'ac_usr_occu_count':ac_usr_occu_count,'ac_usr_unoccu_count':ac_usr_unoccu_count,'ac_users':ac_users})
    else:
        return redirect('/as_admin')  

def admin_user_registrations(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        ac_users = userRegistration_db.objects.filter(status = '1').order_by('-id')
        return render(request, 'admin/admin_user_registrations.html', {'admin': admin,'ac_users':ac_users})
    else:
        return redirect('/as_admin')

def admin_user_reg_view(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        ac_user = userRegistration_db.objects.get(id=id)
        return render(request, 'admin/admin_user_reg_view.html', {'admin': admin,'ac':ac_user})
    else:
        return redirect('/as_admin')


def admin_Update_status(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        ac_user = userRegistration_db.objects.get(id=id)

        if request.method == 'POST':
            which = request.POST['which']
            if which == '1':
                status_select = request.POST['status_select']
                ac_user.user_status = status_select
                ac_user.save()
            elif which == '2':
                cirt_select = request.POST['cirt_select']
                ac_user.Certificate_status = cirt_select
                ac_user.save()
        
            return redirect('/admin_user/admin_user_reg_view/'+str(ac_user.id))
    else:
        return redirect('/as_admin')

def admin_academic_add_seat(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        academic = Academic_db.objects.get(id=id)
        
        if request.method == 'POST':
            count = request.POST['seatsCount']
            enrollment_count = AdminBasic_db.objects.get(data_is = 'EnrolmentNumber')

            for i in range(1, int(count) + 1):
                enrollment_number = f"ASU{int(enrollment_count.value_is) + i:05d}"
                usr_db = userRegistration_db()
                usr_db.academic = Academic_db.objects.get(id=id)
                usr_db.EnrolmentNo = enrollment_number
                usr_db.save()

            enrollment_count.value_is = int(enrollment_count.value_is)+int(count)
            enrollment_count.save()

            academic.seatCount = int(academic.seatCount) + int(count)
            academic.save()

            return redirect('/admin_user/admin_academic_view/'+str(academic.id))
    else:
        return redirect('/as_admin')


def update_academic(request,id):
    academic = Academic_db.objects.get(id=id)
    if request.method == 'POST':
        academic_name = request.POST['academic_name']
        coordinator_name  = request.POST['coordinator_name']
        email = request.POST['email']
        phone = request.POST['phone']

        academic.academicName = academic_name
        academic.coordinatorName = coordinator_name
        academic.email = email
        academic.phone = phone
        academic.save()

    return redirect('/admin_user/admin_academic_view/'+str(academic.id))


def shutDown_academi(request,id):
    academic = Academic_db.objects.get(id=id)
    academic.status = '0'
    academic.save()
    return redirect('/admin_user/admin_academic_view/'+str(academic.id))

def restart_academi(request,id):
    academic = Academic_db.objects.get(id=id)
    academic.status = '1'
    academic.save()
    return redirect('/admin_user/admin_academic_view/'+str(academic.id))


