from django.urls import path
from . import views

urlpatterns = [
    path('', views.startbildschirm, name="home"),
    path('offerings/<int:student_ID>', views.offerings, name="offerings"),
    path('students/', views.student_overview, name="person_select"),
    path('order/<int:student_ID>/<int:item_ID>', views.selector, name="selector"),
    path('order/<int:student_ID>/<int:item_ID>_<int:count>_<int:payed>', views.order, name="order"),
    path('settings/', views.settings, name="settings"),
    path('pay/<int:student_ID>', views.pay, name="pay"),
    path('pay-now/<int:transaction_ID>', views.pay_now_confirm, name="pay_now"),
    path('pay-now/<int:transaction_ID>/done', views.pay_now, name="pay_now_done"),
    path('pay-all/<int:student_ID>', views.pay_all_confirm, name="pay_all"),
    path('pay-all/<int:student_ID>/done', views.pay_all, name="pay_all_done"),
    path('add/', views.simpleAdd, name="simpleAdd"),
    path('update/<int:student_ID>', views.student_edit, name="updateStudent"),
    path('add-item/', views.createItem, name="addItem"),
    path('ranking/', views.ranking, name="ranking")
]
