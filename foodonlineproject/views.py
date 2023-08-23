from django.shortcuts import render
from django.contrib.auth.models import User
import decouple
def index(request):
    # user_name=input('enter  a name')
    # pass_word=input('enter  a pasword')
    # s=User.objects.create(username=user_name,password=pass_word)
    s=User.objects.all()
    # s.save()
    for i in s:
        print(s)

    return render(request,'index.html')