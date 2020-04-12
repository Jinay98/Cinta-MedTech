from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import Patient, Attendance
from django.urls import reverse
import datetime


# Create your views here.
# @login_required 
def home(request):
    submit_button = request.POST.get('Submit')
    if submit_button == 'Submit':
        obj = Patient(name=request.POST.get('name'), age=int(request.POST.get('age')),
                      gender=request.POST.get('gender'))
        obj.save()

    return render(request, 'accounts/home.html')


def get_patient_details(request):
    patients = Patient.objects.all()
    list_of_patients = []
    for patient in patients:
        patient_dict = {}
        patient_dict["id"] = patient.id
        patient_dict["name"] = patient.name
        patient_dict["age"] = patient.age
        patient_dict["gender"] = patient.gender
        list_of_patients.append(patient_dict)

    return render(request, 'accounts/get_patient_details.html', {"list_of_patients": list_of_patients})


def mark_patient_attendance(request, pk):
    id = int(pk)
    current_date = datetime.datetime.now()
    patient = Patient.objects.get(id=id)

    attendance = Attendance.objects.filter(patient=patient)

    if len(attendance) == 0:
        a = Attendance(patient=patient, date=current_date, present_status=True)
        a.save()
    else:
        a = attendance[0]
        a.date = current_date
        a.present_status = True
        a.save()

    return render(request, 'accounts/home.html')


def unmark_patient_attendance(request, pk):
    id = int(pk)
    current_date = datetime.datetime.now()
    patient = Patient.objects.get(id=id)

    attendance = Attendance.objects.filter(patient=patient)

    if len(attendance) == 0:
        a = Attendance(patient=patient, date=current_date, present_status=False)
        a.save()
    else:
        a = attendance[0]
        a.date = current_date
        a.present_status = False
        a.save()

    return render(request, 'accounts/home.html')


def show_present_patients(request):
    patients = Patient.objects.all()

    list_of_patients = []
    for patient in patients:
        if Attendance.objects.filter(patient=patient, present_status=True).exists():
            patient_dict = {}
            patient_dict["id"] = patient.id
            patient_dict["name"] = patient.name
            patient_dict["age"] = patient.age
            patient_dict["gender"] = patient.gender
            list_of_patients.append(patient_dict)

    return render(request, 'accounts/get_present_patient_details.html', {"list_of_patients": list_of_patients})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


# @login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


# @login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)

        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


# @login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
