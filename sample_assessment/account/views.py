from django.shortcuts import render, redirect
from .forms import UserForm
from django.db.models import Count
from .models import User
from .filters import *
from sample_assessment.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, 'account/index.html')


def users(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERR FORM INVALID')

    return render(request, 'account/users.html', {'form': form})


def admin(request):
    labels = []
    data = []

    user = User.objects.all()
    my_filter = UserFilter(request.GET, queryset=user)
    user = my_filter.qs

    pie_chart_qs = User.objects.values('req_status').annotate(Count('req_status'))
    for qs in pie_chart_qs:
        labels.append(qs['req_status'])
        data.append(qs['req_status__count'])

    context = {'users': user, 'my_filter': my_filter, 'labels': labels, 'data': data}
    return render(request, 'account/admin.html', context)


def update_status(request, pk):
    user = User.objects.get(user_id=pk)

    if request.method == 'POST':
        status = ""
        if "confirm" in request.POST:
            user.req_status = 'confirmed'
            status = "confirmed"
        elif "reject" in request.POST:
            user.req_status = 'rejected'
            status = "rejected"

        subject = 'Status of request'
        message = """Hi {name},
        Your request has been {status}.
        """.format(name=user.name, status=status)
        recepient = str(user.email)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

        user.save()
        return redirect('/account/admin')

    context = {'user': user}
    return render(request, 'account/update_status.html', context)
