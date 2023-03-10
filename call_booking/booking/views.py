from django.shortcuts import render

# Create your views here.
import paystack
from django.shortcuts import render, redirect
from .forms import CallBookingForm
from paystackapi.transaction import Transaction
from paystackapi.paystack import Paystack 



def book_call(request):
    form = CallBookingForm(request.POST or None)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.save()
        from decouple import config  
        # Initialize Paystack API
        #paystack.api_key = 'sk_test_5ff6980044e0064be985cb2f1080b67967ea1006'
        paystack = Paystack(secret_key=config('PAYSTACK-SECRET-KEY'))
        # Get amount to charge from user
        
        amount = 2000 * booking.hours  # example amountC

        # Create Paystack transaction
        transaction = Transaction.initialize(
            amount=amount * 100,
            email=booking.email,
            reference=f'call_booking_{booking.id}'
        )

        

        # Redirect to Paystack payment page
        return redirect(transaction.get('data').get('authorization_url'))

    context = {'form': form}
    return render(request, 'book_call.html', context)

from django.http import HttpResponse
from .models import Book
def payment_callback(request):
    
    reference = request.GET.get('reference')
    print(reference)
    transaction = Transaction.verify(reference)
    reference = transaction.get('data').get('reference')
    #print(transaction)

    if transaction.get('data').get('status') == 'success':
        booking_id = int(reference.split('_')[-1])
        booking = Book.objects.get(id=booking_id)
        booking.paid = True
        booking.save()
        print(booking)
        return HttpResponse(f'Payment successful your call has been booked at {booking.date}, {booking.time}, for {booking.hours} hours')
    else:
        return HttpResponse('Payment failed please try again')
    

