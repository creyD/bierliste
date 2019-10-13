from django.urls import path
from . import views

urlpatterns = [
    path('', views.startbildschirm, name="home"),
    path('offerings/<int:student_ID>', views.offerings, name="offerings"),
    path('students/', views.student_overview, name="person_select"),
    path('order/<int:student_ID>/<int:item_ID>_<int:count>', views.order, name="order"),
    path('settings/', views.settings, name="settings"),
    path('add/<int:card_number>', views.student_add, name="addStudent"),
    path('confirm/<int:student_ID>', views.student_confirm, name="addName"),
    path('update/<int:student_ID>', views.student_edit, name="updateStudent"),
    path('add-item/', views.createItem, name="addItem"),
    path('ranking/', views.ranking, name="ranking")
]
