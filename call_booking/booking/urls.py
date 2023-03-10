from django.urls import path
from .views import book_call, payment_callback

urlpatterns = [
    path('book-call/', book_call, name='book_call'),
    path('paystack/callback/', payment_callback, name='payment_callback'),
]
