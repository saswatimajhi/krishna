from django.db import models

# Create your models here.
from accounts.models import Custom_User,Userprofile

class Vendor(models.Model):
    user=models.OneToOneField(Custom_User,on_delete=models.CharField)
    user_profile=models.OneToOneField(Userprofile,related_name='userprofile',on_delete=models.CharField)
    vendor_name=models.CharField(max_length=50)
    vendor_license=models.ImageField(upload_to='vendor/license')
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.vendor_name