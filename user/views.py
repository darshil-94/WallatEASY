from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from user.models import signup
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        if signup.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        user = signup.objects.create(username=username, password=password)
        user.save()
        
        return  redirect('signin')

    return render(request, 'signup.html')

def sigin(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        user = signup.objects.filter(username=username, password=password).first()

        if user:
            request.session['username'] = username
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid username or password")
    return render(request, 'signin.html')

def dashboard(request):
    username = request.session.get('username')
    return render(request, 'dashboard.html', {'username': username})

def logout(request):
    if request.method == 'POST':
        request.session.flush()  # Clears all session data
        return redirect('signin')  # Or HttpResponse("Logged out")
    return HttpResponse("Invalid logout request")

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())