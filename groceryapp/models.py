# from django.db import models

# class GroceryKit(models.Model):
#     title = models.CharField(max_length=100)
#     badge = models.CharField(max_length=50)
#     tag = models.CharField(max_length=100)
#     members = models.CharField(max_length=50)
#     rating = models.IntegerField()
#     reviews = models.CharField(max_length=20)
#     price = models.IntegerField()
#     description = models.TextField()
#     image = models.URLField()

#     def __str__(self):
#         return self.title
    

# # ✅ Order model
# class Order(models.Model):
#     PAYMENT_TYPE = (
#         ('full', 'Full Payment'),
#         ('weekly', 'Weekly Payment'),
#     )

#     kit = models.ForeignKey(GroceryKit, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     total_amount = models.IntegerField()
#     payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE)
#     delivery_date = models.DateField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.kit.title} - {self.payment_type}"


# # ✅ Payment model (FIXED)
# class Payment(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     week_number = models.IntegerField(null=True, blank=True)
#     status = models.CharField(max_length=20, default='pending')

#     def __str__(self):
#         return f"{self.order.id} - {self.amount}"


from django.db import models

class GroceryKit(models.Model):
    title = models.CharField(max_length=100)
    badge = models.CharField(max_length=50)
    tag = models.CharField(max_length=100)
    members = models.CharField(max_length=50)
    rating = models.IntegerField()
    reviews = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title


# ✅ ORDER MODEL
class Order(models.Model):
    PAYMENT_TYPE = (
        ('full', 'Full Payment'),
        ('weekly', 'Weekly Payment'),
    )

    kit = models.ForeignKey(GroceryKit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_amount = models.IntegerField()
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE)
    delivery_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kit.title} - {self.payment_type}"


# ✅ PAYMENT MODEL (THIS WAS MISSING)
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.IntegerField()
    week_number = models.IntegerField(null=True, blank=True)
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order.id} - {self.status}"