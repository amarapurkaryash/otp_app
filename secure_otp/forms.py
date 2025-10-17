from django import forms

class RequestOTPForm(forms.Form):
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'})
    )

class VerifyOTPForm(forms.Form):
    email = forms.EmailField(label="Email")
    code = forms.CharField(label="OTP code", max_length=6)
