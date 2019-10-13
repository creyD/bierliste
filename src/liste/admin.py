from django.contrib import admin
from .models import Student, Item, StudentItems


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('student_ID', 'nickname', 'card_ID')


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('item_ID', 'item_name', 'item_price', 'category', 'beer')


@admin.register(StudentItems)
class StudentItems(admin.ModelAdmin):
    list_display = ('transaction_ID', 'transaction_date', 'student', 'item', 'item_count', 'transaction_price', 'payment_status')
