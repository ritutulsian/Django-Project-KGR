from django.shortcuts import render, redirect

# Create your views here.
def register(request):
  form = UserCreationForm()
  return render(request, 'user/register.html', content={'form':form})