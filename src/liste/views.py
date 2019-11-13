from django.shortcuts import render, get_object_or_404, redirect

from .models import Student, Item, StudentItems
from .forms import UpdateStudent, CreateItem


def startbildschirm(request):
    return render(request, 'liste/home.html')


def offerings(request, student_ID):
    student = False
    if student_ID == 0:
        student = Student.objects.create()
    else:
        student = get_object_or_404(Student, student_ID=student_ID)

    context = {
        'student': student,
        'offerings': Item.objects.all()
    }
    return render(request, 'liste/offerings.html', context)


def student_overview(request):
    context = {
        'students': Student.objects.filter(nickname__isnull=False)
    }
    return render(request, 'liste/students.html', context)


def order(request, student_ID, item_ID, count, payed):
    student = get_object_or_404(Student, student_ID=student_ID)
    item = get_object_or_404(Item, item_ID=item_ID)
    bill = StudentItems.objects.create(student=student, item=item, transaction_price=item.item_price * count, item_count=count)

    if payed == 1:
        bill.payment_status = True
        bill.save()

    return redirect(startbildschirm)


def settings(request):
    return render(request, 'liste/settings.html')


def simpleAdd(request):
    form = UpdateStudent(request.POST or None)
    student = Student.objects.create()
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(startbildschirm)
    return render(request, 'liste/created.html', {'student': student, 'form': form})


def student_edit(request, student_ID):
    student = get_object_or_404(Student, student_ID=student_ID)
    form = UpdateStudent(request.POST or None, instance=student)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(startbildschirm)
    return render(request, 'liste/edit.html', {'form': form, 'student': student})


def createItem(request):
    form = CreateItem(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(startbildschirm)
    return render(request, 'liste/createItem.html', {'form': form})


def ranking(request):
    beer_list = {}
    for transaction in StudentItems.objects.all():
        if transaction.item.beer:
            if transaction.student.student_ID in beer_list:
                beer_list[transaction.student.student_ID]['bier_count'] += transaction.item_count
            else:
                beer_list[transaction.student.student_ID] = {
                    'nickname': (transaction.student.nickname if transaction.student.nickname else 'Anon'),
                    'bier_count': transaction.item_count
                }
    beer_list_sorted = sorted(beer_list.items(), key=lambda x: x[1]['bier_count'])
    return render(request, 'liste/bierliste.html', {'bierliste': beer_list_sorted})


def selector(request, student_ID, item_ID):
    return render(request, 'liste/selector.html', {'student_ID': student_ID, 'item': get_object_or_404(Item, item_ID=item_ID)})


def pay(request, student_ID):
    person = get_object_or_404(Student, student_ID=student_ID)
    debt = 0
    bills = StudentItems.objects.filter(student=person, payment_status=False)
    for item in bills:
        debt += item.transaction_price

    context = {
        'student': person,
        'bills': bills,
        'debt': debt
    }
    return render(request, 'liste/pay.html', context)


def pay_now_confirm(request, transaction_ID):
    context = {
        'transaction': get_object_or_404(StudentItems, transaction_ID=transaction_ID)
    }
    return render(request, 'liste/pay_now.html', context)


def pay_now(request, transaction_ID):
    transaction = get_object_or_404(StudentItems, transaction_ID=transaction_ID)
    transaction.payment_status = True
    transaction.save()
    return redirect(startbildschirm)


def pay_all_confirm(request, student_ID):
    person = get_object_or_404(Student, student_ID=student_ID)
    debt = 0
    bills = StudentItems.objects.filter(student=person, payment_status=False)
    for item in bills:
        debt += item.transaction_price

    context = {
        'student': person,
        'bills': bills,
        'debt': debt
    }
    return render(request, 'liste/pay_all.html', context)


def pay_all(request, student_ID):
    person = get_object_or_404(Student, student_ID=student_ID)
    for item in StudentItems.objects.filter(student=person, payment_status=False):
        item.payment_status = True
        item.save()
    return redirect(startbildschirm)
