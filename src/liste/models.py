from django.db import models


# Nicht zu sehr triggern lassen, ist englisch
class Student(models.Model):
    student_ID = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, null=True)
    card_ID = models.IntegerField(null=True)


# Alle angebotenen Produkte
class Item(models.Model):
    item_ID = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    # True = Essen/ Trinken; False = Sonstiges
    category = models.BooleanField(default=True)


# Transaktionsliste
class StudentItems(models.Model):
    transaction_ID = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    item_count = models.PositiveIntegerField()
    # Preis zum Zeitpunkt der Transaktion
    transaction_price = models.DecimalField(max_digits=6, decimal_places=2)
    # Bezahlt? Ja/ Nein
    payment_status = models.BooleanField(default=False)
