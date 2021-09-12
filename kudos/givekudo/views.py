from django.shortcuts import render
from django.http import HttpResponse
from .forms import KudoForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Kudo

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

