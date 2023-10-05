from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Userform
from django.contrib import messages

from .models import Custom_User

# Create your views here.


def registerUser(request):
    if request.method == 'POST':
            form=Userform(request.POST)
             # here the details will save in user field but role not given automatically so we need to halt this
            #  another problem we are storing the password in a plane tect format we need to hash them before saving into the database 
             
            #  create the user using form 
            if form.is_valid():
            #      password=form.cleaned_data['password']
            #      user=form.save(commit=False)
            #      user.set_password(password)
            #      user.role=Custom_User.CUSTOMER
            #      user.save()
            
            #  crate the user using create_user
            
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                
                user=Custom_User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.role=Custom_User.CUSTOMER
                user.save()
                messages.success(request,'You Have succeefully Registerd')
                # messages.error(request,'You Have succeefully Registerd')
                
                # Ok if i receive some error then how my html pafe determine that whic type of error i ma receiving so
                # you have to do little bit configuration in setting 
                # after do some settins you will get the appropriate css color 
                
                return redirect('registerUser')
            else:          
                print('invalid form')

                print(form.errors)
                
        # after that you have to focus on fields error and non-fields error fields erroe like username and etc
        # and non-field error like confirm password 

            
             
               
    else:
        form=Userform()


    context={
                        'forms':form,
                    }
             
        

   
    return render(request,'accounts/registerUser.html',context)
