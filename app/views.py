from django.shortcuts import render, redirect
from .models import Trainer, Trainee, Financial
from .forms import TrainerForm, TraneeForm, FinancialForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")


def traine(request):
    return render(request, "traine.html", {"traine": TraneeForm()})


def savetraine(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    addressl1 = request.POST.get("addressl1")
    addressl2 = request.POST.get("addressl2")
    city = request.POST.get("city")
    state = request.POST.get("state")
    zipcode = request.POST.get("zipcode")
    country = request.POST.get("country")
    jobtitle = request.POST.get("jobtitle")
    technology = request.POST.get("technology")
    rate = request.POST.get("rate")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    startdate = request.POST.get("startdate")
    enddate = request.POST.get("enddate")
    trainer = request.POST.get("trainer")
    status = request.POST.get("status")
    traine = TraneeForm(request.POST)
    if traine.is_valid():
        Trainee(fname=fname, lname=lname, addressl1=addressl1, addressl2=addressl2, city=city, state=state,
                zipcode=zipcode,
                country=country, jobtitle=jobtitle, technology=technology, rate=rate, phone=phone, email=email,
                startdate=startdate, enddate=enddate, trainer=trainer, status=status).save()
        messages.success(request, "saved")
        return redirect('traine')
    else:
        return render(request, "traine.html", {"traine": traine})


def trainedashboard(request):
    td = Trainee.objects.all()
    return render(request, "trainedashboard.html", {"traindashboard": td})


def trainer(request):
    return render(request, "trainer.html", {"trainer": TrainerForm()})


def savetrainer(request):
    trainr = TrainerForm(request.POST)
    if trainr.is_valid():
        trainr.save()
        messages.success(request, "saved")
        return redirect('trainer')
    else:
        return render(request, "trainer.html", {"trainer": trainr})


def finacial(request):
    return render(request, "financial.html")


def savefinacial(request):
    bill = request.POST.get("bill")
    pay = request.POST.get("pay")
    tax = float(bill) * (15 / 100)
    margin = (float(bill) - (float(pay) + float(tax)))
    Financial.objects.create(Billrate=float(bill), payrate=float(pay), Tax=float(tax), margin=format(margin))
    messages.success(request, "saved")
    return redirect('financial')


def lead(request):
    leads = Trainee.objects.filter(status="Lead")
    return render(request, "lead.html", {"data": leads})


def prospect(request):
    pros = Trainee.objects.filter(status="Prospect")
    return render(request, "prospect.html", {"data": pros})


def Intraining(request):
    intrain = Trainee.objects.filter(status="In Training")
    return render(request, "intraing.html", {"data": intrain})


def completed(request):
    complete = Trainee.objects.filter(status="Completed")
    return render(request, "completed.html", {"data": complete})


def rejected(request):
    reject = Trainee.objects.filter(status="Rejected")
    return render(request, "rejected.html", {"data": reject})


def invalid(request):
    invale = Trainee.objects.filter(status="Invalid")
    return render(request, "invalid.html", {"data": invale})


def vtrainer(request):
    vtrain = Trainer.objects.all()
    return render(request, "vtrainer.html", {"data": vtrain})
