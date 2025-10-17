from django.db import models

class UnsecureOTP(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=10)   # 6-digit OTP fits fine
    created_at = models.DateTimeField(auto_now_add=True)
    # NO expiry, NO secure flags — this is intentionally minimal/insecure

    def __str__(self):
        return f"{self.email} - {self.code}"
