from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, ResultForm, CreateUser
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


  

@login_required(login_url='login')
def applicants_registration(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admission):
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/registration')
        context = {
            'form':form
            }
        return render(request, 'activities/Applicants Registration.html', context)
        
    else: 
        return redirect ('logout')
        

@login_required(login_url='login')
def changeStatus(request, pk):
    if request.user.is_authenticated:
        data = result.objects.get(id=pk)
        info = Applicants.objects.get(id=data.applicantNumber_id)
        information = ResultForm(instance=data)
        form = ResultForm()
        if request.method == 'POST':
            form = ResultForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('/interview')
        context = {
            'information':information,
            'info' : info
            }
        return render(request, 'activities/changeStatus.html', context)
    
    else: 
        return redirect ('logout')

@login_required(login_url='login')
def search_courseMajor(request):
    if request.user.is_authenticated:
        number = 0
        result = ''
        information = Applicants.objects.all()[:5]
        if 'changeCM' in request.POST:
            number = request.POST['changeCM']
            if number == '':
                result = 'Enter valid Applicant Number'
                information = []
            else:
                information = Applicants.objects.filter(applicantNumber = number)
                if information.count() == 0:
                    result = 'Applicant Number Not Found'
                else:
                    print(information[0].pk)
                    return redirect ('editProfile', information[0].pk)

        context = {
            'information' : information,
            'result' : result
            }    
        return render(request, 'activities/searchCourse.html', context)
    else: 
        return redirect ('logout')

@login_required(login_url='login')
def editProfile(request, pk):
    if request.user.is_authenticated:
    
        data = Applicants.objects.get(id=pk)
        information = RegistrationForm(instance=data)
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('/registration')
        context = {
            'information' : information
        }
        return render(request, 'activities/editProfile.html', context)

    else:
        return redirect ('logout')

@login_required(login_url='login')
def interview(request):
    if request.user.is_authenticated and request.user.is_faculty:
        number = 0
        statusResult = []
        numberOfResult = 0
        noStatus = ''
        applicantStatus = []
        applicantsId = []

        numberOfApplicants = Applicants.objects.all().count()
        if 'search' in request.POST:
            number = request.POST['search']
            if number == '':
                noStatus = 'Enter Valid Applicant Number'
            else:
                applicantsId = Applicants.objects.filter(applicantNumber = number)
                # print(applicantsId[0].lastName)
                if applicantsId.count() < 1:
                    numberOfResult = 0
                    noStatus = 'Applicant Number Not Found'
                else:
                    numberOfResult = result.objects.filter(applicantNumber_id = applicantsId[0].pk).count()
                    applicantStatus = result.objects.filter(applicantNumber_id = applicantsId[0].pk)
                    if numberOfResult < 1:
                        # numberOfResult = 0
                        statusResult = result.objects.create(applicantNumber_id = applicantsId[0].pk)
                        print(statusResult)
                        statusResult = result.objects.filter(applicantNumber_id = applicantsId[0].pk)
                        print(statusResult)
                    elif numberOfResult == 1:
                        statusResult = result.objects.filter(applicantNumber_id = applicantsId[0].pk)
                        print(statusResult[0].pk)
                    else:
                        print('Hi')                

        context = {
            'totalApplicants': numberOfApplicants,
            'result' : numberOfResult,
            'status' : statusResult,
            'noStatus' : noStatus,
        }

        return render(request, 'activities/interview.html', context)

    else: 
        return redirect ('logout')

@login_required(login_url='login')
def user_registration(request):
    if request.user.is_authenticated:
        form = CreateUser()
        if request.method == "POST":
            form = CreateUser(request.POST)
            if form.is_valid():
                userType = form.cleaned_data.get('userType')
                #userType = request.POST.get('userType')
                print(userType)
                if userType == "head":
                        form.instance.is_head = True
                elif userType == "admission":
                    form.instance.is_admission = True
                else:
                    form.instance.is_faculty = True
                form.save()
                return redirect('login')  

        context = {
            'form':form
        }           
        return render(request, 'activities/userRegistration.html', context)

    else: 
        return redirect ('logout')


def index(request):
    if request.user.is_authenticated:
        return redirect ('registration')

    elif request.user.is_authenticated and request.user.is_faculty:
        return redirect('interview')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pwd') 

            user = authenticate(request, username=username, password=password) 
            print(user)

            if (user is not None and user.is_superuser) or \
                (user is not None and user.is_admission):
                login(request, user)
                return redirect('registration')
            
            elif (user is not None and user.is_superuser) or \
                (user is not None and user.is_faculty):
                login(request, user)
                return redirect('interview')
            
            else:
                messages.info(request, 'Invalid Credentials')
                    
        context = {}
        return render(request, 'activities/Login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

    