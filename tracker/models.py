from django.db import models
from user.models import signup


class Wallet(models.Model):
    user = models.OneToOneField(signup, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('ADD', 'Add Money'),
        ('SEND', 'Spend Money'),
    )

    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    product_names = models.TextField(blank=True, default="")
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} ₹{self.amount} by {self.user.username} on {self.timestamp.strftime('%Y-%m-%d')}"
