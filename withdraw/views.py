from django.shortcuts import render
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from regis.models import Account
from .forms import WithdrawalForm
from django.contrib.auth.decorators import login_required

# Placeholder function for M-Pesa withdrawal (simulated)
def mpesa_withdrawal(amount, phone_number):
    # In a real application, you would integrate with an M-Pesa API here.
    # This is just a simulation.
    print(f"Initiating M-Pesa withdrawal of Ksh{amount} to phone number: {phone_number}")
    return True  # Simulating a successful transaction.

@login_required
def withdraw(request):
    user_account = Account.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            withdrawal_amount = form.cleaned_data['amount']
            
            if withdrawal_amount <= user_account.balance:
                # Process withdrawal
                user_account.balance -= withdrawal_amount
                user_account.save()
                phone_number = request.user.phone_number  # Assuming phone_number is a profile field
                success = mpesa_withdrawal(withdrawal_amount, phone_number)
                
                if success:
                    messages.success(request, f"Withdrawal of Ksh{withdrawal_amount} successful!")
                    return redirect('feenax')  # Redirect to a success page or dashboard
                else:
                    messages.error(request, "M-Pesa transaction failed. Please try again later.")
            else:
                messages.error(request, "Insufficient balance.")
        else:
            messages.error(request, "Invalid amount entered.")
    else:
        form = WithdrawalForm()

    return render(request, 'withdraw.html', {'form': form, 'account': user_account})
# Create your views here.
