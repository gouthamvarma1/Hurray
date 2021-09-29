import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import KudoForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Kudo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from kudos.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT,EMAIL_HOST


# Create your views here.

def home(request):
    return render(request, 'givekudo/home.html')

@csrf_exempt
def givekudo(request):
    if request.user.is_authenticated:
        form = KudoForm(request)
        if request.method == "POST":
            form = KudoForm(request, data=request.POST)
            if form.is_valid():
                today = datetime.now().date()
                start = today - timedelta(days=today.weekday())
                end = start + timedelta(days=6)
                from_user=User.objects.get(pk=request.user.id)
                to_user=User.objects.get(pk=form.data.get('collegue_name'))
                kudo_data=Kudo.objects.filter(from_user=from_user).exclude(kudo_date__lt=start).filter(kudo_date__lt=end+timedelta(days=1))
                kudos_already_given=sum([kudo.kudo_count for kudo in kudo_data])
                kudos_tobe_given=form.data.get('kudo_count')
                total_kudos=kudos_already_given + int(kudos_tobe_given)
                if (total_kudos) > 3:
                    messages.info(request, 'For current week from {}, to {}. Kudos given by {} exceeds 3. \
                            Change kudo count to a value less than {}'.format(str(start), str(end), from_user.username, form.data.get('kudo_count')))
                else:
                    kudo_details=Kudo.objects.create(from_user=from_user, to_user=to_user, content=form.data.get("message"), kudo_count=form.data.get("kudo_count"))
                    kudo_details.save()
                    messages.success(request, 'Thank you for appreciating. Kudo Given!')
                    #r = requests.post('http://127.0.0.1:8000/api/students/sendEmail', data=
                    #{
                     #   "email":  to_user.email,
                      #  "status": 1
                   # })
                    sendmail("Hurray You have received KUDOS",to_user.email, "You have received kudso from "+ from_user.username+ "please login to you dashboard to view/redeem")
                    #if r.status_code == 200:
                        #return HttpResponse('Yay, notified the receiver')
                   # return HttpResponse('Sorry, Could not notify the receiver')

        context = {'form': form}
        return render(request, 'givekudo/kudo.html', context)
    return render(request, 'givekudo/home.html')


def dashboard(request):
    if request.user.is_authenticated:
        to_user=User.objects.get(pk=request.user.id)
        today=datetime.now().date()
        start=today - timedelta(days=today.weekday())
        end=start + timedelta(days=6)
        kudo_data=Kudo.objects.filter(to_user=to_user).exclude(kudo_date__lt=start).filter(kudo_date__lt=end+timedelta(days=1))
        dashboard_data=[{'from_user':kudo.from_user.username,
                         'kudo_count': kudo.kudo_count,
                         'date_posted': str(kudo.kudo_date)} for kudo in kudo_data]
        context = {'dashboard': dashboard_data}
        return render(request, 'givekudo/dashboard.html', context)
    return render(request, 'givekudo/home.html')


def sendmail(subject, tolist, content):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    mail_content = content

    # The mail addresses and password
    from_address = EMAIL_HOST_USER
    from_pass = EMAIL_HOST_PASSWORD
    to_address = tolist.split(',')  # from input parameter

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = "," . join (to_address) 
    print("," . join (to_address) )
    message['Subject'] = subject  # from input parameter

    # The body and the attachments for the mail (if any - as of now, it is a plain mail)
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    # use gmail with port
    session = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    # enable security
    session.starttls()
    # login with mail_id and password
    session.login(from_address, from_pass)

    text = message.as_string()
    
    session.sendmail(from_address, to_address, text)
    session.quit()
    print('Mail Sent successfully')
    return

