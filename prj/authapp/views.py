from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import EventRegistration, user,eventc,club
from django.contrib.auth import authenticate, login, logout
from .forms import EventRegistrationform, LoginForm,RegistrationForm, clubform,eventcform






def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {
        'form': forms
    }
    return render(request, 'signin.html', context)


def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    user.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    return render(request, 'signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'signup.html', context)

def signout(request):
    logout(request)
    return redirect('signin')
    



@login_required(login_url='signin')
def index (request):
    events = eventc.objects.filter(status='approved').order_by('date')
    return render(request,'index.html', { 'events' : events})


def about (request):
    return render(request,'about.html')




def contact (request):
    return render(request,'contact.html')


def access(event_id,user_id):
    res=EventRegistration.objects.filter(event_id=event_id,user_id=user_id).count
    if res()<1:
        return(True)
    else:
        return(False)


def event (request,id):
    events = eventc.objects.get(pk=id)
    if access(id,request.user):
     form=EventRegistrationform
     if request.method=='POST':
        postdata=request.POST
        form=EventRegistrationform(postdata)
        if form.is_valid():
             obj=form.save(commit=False)
             obj.user=request.user
             obj.event=events
             obj.save()
    
    data={ 'events' : events,'access':access(id,request.user)}
    return render(request,'event.html',data)



def create_event (request): 
   form= eventcform ()
   if request.method =='POST' :
       postdata=request.POST
       postfile=request.FILES
       form = eventcform(postdata,postfile)
       if form.is_valid():
           obj=form.save(commit=False)
           obj.user=request.user
           obj.status='pending...'
           obj.save()
           return redirect(index)


  
   context = {'form':form}
   return render(request,'create_event.html',context)

def my_events (request,userid):
    events = eventc.objects.filter(user_id=userid)
    return render(request,'my_events.html',{ 'events' : events})


def participant (request,id):
    events = EventRegistration.objects.filter(event=id)
    total=events.count()
    return render(request,'participant.html',{ 'events' : events,'total':total})

def clubs(request):
    data=club.objects.all()
    return render(request,'clubs.html',{'data' : data})


def my_club(request,id):
    data=club.objects.get(chef_id=id)
    return render(request,'my_club.html',{'data' : data})
    
def club_update(request,id):
    cl=club.objects.get(id=id)
    form=clubform(request.POST or None,request.FILES or None,instance=cl)
    if form.is_valid():
        form.save()
        return render(request,'my_club.html',{'data' : cl})
    context={'form':form,
              'data':cl}
    
    return render(request,'club_update.html',context)

def event_update(request,id):
    cl=eventc.objects.get(id=id)
    form=eventcform(request.POST or None,request.FILES or None,instance=cl)
    if form.is_valid():
         obj=form.save(commit=False)
         obj.status='pending...'
         obj.feedback=''
         obj.save()
         form.save()
         events = eventc.objects.filter(user_id=request.user)
         return render(request,'my_events.html',{ 'events' : events})
    context={'form':form,
              'data':cl}
    return render(request,'update_event.html',context)
