from django.db import models


# Nicht zu sehr triggern lassen, ist englisch
class Student(models.Model):
    student_ID = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, null=True, verbose_name='Nickname')
    card_ID = models.IntegerField(null=True, verbose_name='Kartennummer')


# Alle angebotenen Produkte
class Item(models.Model):
    item_ID = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100, verbose_name='Produkt Name')
    item_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Produkt Preis')
    # True = Essen/ Trinken; False = Sonstiges
    category = models.BooleanField(default=True, verbose_name='Erste Seite?')
    # True = Zählt für Getränke
    beer = models.BooleanField(default=False, verbose_name='Zählt für Bierliste?')


# Transaktionsliste
class StudentItems(models.Model):
    transaction_ID = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField(auto_now_add=True, verbose_name='Rechnungsdatum')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Studierende')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, verbose_name='Produkt', related_name='Produkt')
    item_count = models.PositiveIntegerField(verbose_name='Menge')
    # Preis zum Zeitpunkt der Transaktion
    transaction_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preis')
    # Bezahlt? Ja/ Nein
    payment_status = models.BooleanField(default=False, verbose_name='Bezahlung erfolgt')
