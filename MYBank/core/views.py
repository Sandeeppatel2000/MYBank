from django.shortcuts import render
from .models import Customers, Transfer
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def transfer(request):
    if request.method == "POST":
        sender_email = request.POST.get("sender_email")
        sender_password = request.POST.get("sender_password")
        sender_account_no = request.POST.get("sender_acc")
        receiver_email = request.POST.get("reciever_email")
        print(sender_email, receiver_email)
        print(sender_account_no)
        try:
            o_cust = Customers.objects.get(user_email=receiver_email)
            print(o_cust.acoount_no)
            sender = Customers.objects.get(user_email=sender_email)
            print(sender.acoount_no)
            amount = float(request.POST.get("amount"))
            print(o_cust.id)
            print(sender.id)
            if(sender_email == receiver_email or int(sender_account_no) == o_cust.id or int(sender_account_no) != sender.id):
                context = {
                    'user_email': o_cust.user_email,
                    'first_name': o_cust.first_name,
                    'last_name': o_cust.last_name,
                    'flag': 1,
                }
                return render(request, 'make_transaction.html', context)
            receiver = Customers.objects.get(user_email=receiver_email)
            if(sender_password != sender.password):
                context = {
                    'user_email': o_cust.user_email,
                    'first_name': o_cust.first_name,
                    'last_name': o_cust.last_name,
                    'flag': 2,
                }
                return render(request, 'make_transaction.html', context)
            if(amount >= sender.current_balance):
                return HttpResponse("Not Enough Balance. Please Go Back.")
            sender.current_balance = sender.current_balance-(amount//2)
            receiver.current_balance = receiver.current_balance+(amount//2)
            tx = Transfer(tx_from=sender, tx_to=o_cust, amount=amount)
            tx.save()
            receiver.save()
            sender.save()
            return HttpResponseRedirect('/view_all_customers/')
        except:
            return HttpResponse("No Account Found. Enter Valid Account Details. Please Go Back.")


def view_customer(request, id):
    o_cust = Customers.objects.filter(acoount_no=id).first()
    context = {
        'user_email': o_cust.user_email,
        'first_name': o_cust.first_name,
        'last_name': o_cust.last_name,
        'acoount_no': o_cust.acoount_no,
        'current_balance': o_cust.current_balance,
    }
    return render(request, 'view_customer.html', context)


def make_transaction(request, id):
    o_cust = Customers.objects.get(acoount_no=id)
    context = {
        'user_email': o_cust.user_email,
        'first_name': o_cust.first_name,
        'last_name': o_cust.last_name,
        'acoount_no': o_cust.id,
        'flag': 0,
    }
    return render(request, 'make_transaction.html', context)


def view_all_customers(request):
    all_customers = Customers.objects.all()
    context = {
        'all_customers': all_customers,
    }
    return render(request, 'view_all_customers.html', context)


def services(request):
    return render(request, 'services.html')
