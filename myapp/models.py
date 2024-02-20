from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
# class TrafficViolation(models.Model):
#     license_plate = models.CharField(max_length=20)

#     def __str__(self):
#         return self.license_plate
    
# class LicensePlateRecord(models.Model):
#     license_plate = models.CharField(max_length=20)
#     owner_name = models.CharField(max_length=100)
#     address = models.TextField()
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return f"{self.license_plate} - {self.owner_name}"
    
# class ViolationHistory(models.Model):
#     traffic_violation = models.ForeignKey(TrafficViolation, on_delete=models.CASCADE)
#     fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     fine_status = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.traffic_violation.license_plate} - Fine: {self.fine_amount} - Status: {self.fine_status} - Date: {self.date}"

class TrafficViolation(models.Model):
    license_plate = models.CharField(max_length=20)

    def __str__(self):
        return self.license_plate
    
class LicensePlateRecord(models.Model):
    license_plate = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    
    # ForeignKey to TrafficViolation model
    traffic_violation = models.ForeignKey(TrafficViolation, on_delete=models.CASCADE, null=True, blank=True)
    
    # ForeignKey to User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.license_plate} - {self.owner_name}"
    
class ViolationHistory(models.Model):
    traffic_violation = models.ForeignKey(TrafficViolation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fine_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.traffic_violation.license_plate} - User: {self.user.username} - Fine: {self.fine_amount} - Status: {self.fine_status} - Date: {self.date}"