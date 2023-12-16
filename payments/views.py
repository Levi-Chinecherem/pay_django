from django.shortcuts import render, redirect
from .models import Payment, UserWallet
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import CreateWalletForm

@login_required
def view_wallet(request):
    user_wallet = UserWallet.objects.get(user=request.user)
    return render(request, 'view_wallet.html', {'user_wallet': user_wallet})

@login_required
def create_wallet(request):
    if request.method == 'POST':
        form = CreateWalletForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.user = request.user
            wallet.save()
            return redirect('view_wallet')  # Redirect to the wallet view
    else:
        form = CreateWalletForm()

    return render(request, 'create_wallet.html', {'form': form})

def initiate_payment(request):
	if request.method == "POST":
		amount = request.POST['amount']
		email = request.POST['email']

		pk = settings.PAYSTACK_PUBLIC_KEY

		payment = Payment.objects.create(amount=amount, email=email, user=request.user)
		payment.save()

		context = {
			'payment': payment,
			'field_values': request.POST,
			'paystack_pub_key': pk,
			'amount_value': payment.amount_value(),
		}
		return render(request, 'make_payment.html', context)

	return render(request, 'payment.html')


def verify_payment(request, ref):
	if not request.user.is_authenticated:
		return redirect('login')
	
	payment = Payment.objects.get(ref=ref)
	verified = payment.verify_payment()

	if verified:
		user_wallet = get_object_or_404(UserWallet, user=request.user)
		user_wallet.balance += payment.amount
		user_wallet.save()
		print(request.user.username, " funded wallet successfully")
		return render(request, "success.html")
	return render(request, "success.html")