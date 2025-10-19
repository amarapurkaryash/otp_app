from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import RequestOTPForm, VerifyOTPForm
from .models import UnsecureOTP
import random
from django.conf import settings



def generate_code():
    return f"{random.randint(0, 999999):06d}"  # zero-padded 6-digit

def request_otp(request):
    if request.method == 'POST':
        form = RequestOTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = generate_code()
            # Save to DB (no expiry, unsecure)
            UnsecureOTP.objects.create(email=email, code=code)
            # Send email
            subject = "Your OTP (Unsecure demo)"
            body = f"Your OTP is: {code}\n\n(This is an UNSECURE demo OTP for learning only.)"
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
            messages.success(request, "OTP sent to your email (demo).")
            return redirect('unsecure_otp:verify')
    else:
        form = RequestOTPForm()
    return render(request, 'unsecure_otp/request.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = VerifyOTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = form.cleaned_data['code'].strip()
            # Simple check: exists in DB
            match = UnsecureOTP.objects.filter(email=email, code=code).first()
            if match:
                # delete after success to avoid reuse
                match.delete()
                messages.success(request, "OTP valid — (demo).")
                return render(request, 'unsecure_otp/success.html')
            else:
                messages.error(request, "Invalid OTP.")
    else:
        form = VerifyOTPForm()
    return render(request, 'unsecure_otp/verify.html', {'form': form})

def unsecure_otp_home(request):
    # Simple landing page for unsecure OTP
    return render(request, 'unsecure_otp/index.html')
