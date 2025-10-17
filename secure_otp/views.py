from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import RequestOTPForm, VerifyOTPForm
from .models import SecureOTP
import random
from django.utils import timezone

def generate_code():
    """Generate a 6-digit OTP"""
    return f"{random.randint(0, 999999):06d}"

def secure_otp_home(request):
    """Landing page for secure OTP"""
    return render(request, 'secure_otp/index.html')

def request_otp(request):
    if request.method == 'POST':
        form = RequestOTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = generate_code()
            SecureOTP.objects.create(email=email, code=code)

            # Send email
            subject = "Your Secure OTP"
            body = f"Your OTP is: {code}\nValid for 5 minutes."
            send_mail(subject, body, None, [email], fail_silently=False)
            
            messages.success(request, "OTP sent to your email (valid 5 mins).")
            return redirect('secure_otp:verify')
    else:
        form = RequestOTPForm()
    return render(request, 'secure_otp/request.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = VerifyOTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = form.cleaned_data['code'].strip()
            otp_entry = SecureOTP.objects.filter(email=email, code=code).first()

            if otp_entry:
                if otp_entry.is_expired():
                    otp_entry.delete()
                    messages.error(request, "OTP expired!")
                    return render(request, 'secure_otp/fail.html')
                
                otp_entry.delete()  # Remove after success
                messages.success(request, "OTP verified successfully!")
                return render(request, 'secure_otp/success.html')
            else:
                messages.error(request, "Invalid OTP!")
    else:
        form = VerifyOTPForm()

    return render(request, 'secure_otp/verify.html', {'form': form})
