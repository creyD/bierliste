from django.shortcuts import render, get_object_or_404, redirect

from .models import Student, Item, StudentItems
from .forms import UpdateName, UpdateStudent, CreateItem


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


def order(request, student_ID, item_ID, count):
    student = get_object_or_404(Student, student_ID=student_ID)
    item = get_object_or_404(Item, item_ID=item_ID)
    StudentItems.objects.create(student=student, item=item, transaction_price=item.item_price * count, item_count=count)
    return redirect(startbildschirm)


def settings(request):
    return render(request, 'liste/settings.html')


def student_add(request, card_number):
    student, created = Student.objects.get_or_create(card_ID=card_number)
    return render(request, 'liste/created_s1.html', {'student': student, 'created': created, 'form': UpdateName()})


def student_confirm(request, student_ID):
    form = UpdateName(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        student = get_object_or_404(Student, student_ID=student_ID)
        student.nickname = form.cleaned_data['nickname']
        student.save()
    return redirect(startbildschirm)


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
    return render(request, 'liste/selector.html', {'student_ID': student_ID, 'item_ID': item_ID})
