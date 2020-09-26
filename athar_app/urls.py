from django.urls import path
from athar_app import views

urlpatterns = [
   path('', views.athar, name='athar'),
   path('delete/<loosers_id>' , views.delete_loosers, name='delete_loosers'),
   path('edit/<loosers_id>' , views.edit_loosers, name='edit_loosers'),
   path('complete/<loosers_id>' , views.complete_loosers, name='complete_loosers'),
   path('pending/<loosers_id>' , views.pending_loosers, name='pending_loosers'),
]
