from django.shortcuts import render
import datetime
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
import random
# Create your views here.
from web.user import logger
from web.user.forms import LoginForm, RegisterForm, OTPForm, AddEmailForm
from web.user.models import Profile, AddEmails


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        if 'next' in request.GET:
            return redirect(request.GET["next"])
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')

        check_user = User.objects.filter(username__iexact=username).first()
        check_profile = Profile.objects.filter(phone_number=phone_number).first()

        if check_user or check_profile:
            logger.error('User already Exists')
            messages.add_message(request, messages.ERROR, "user already exists", form.errors)
            return redirect('register')

        user = User(email=email, username=username)
        user.save()
        otp = str(random.randint(1000, 9999))
        profile = Profile(user=user, phone_number=phone_number, otp=otp)
        profile.save()
        print("Login OTP >>>>>> ", otp)
        request.session['phone_number'] = phone_number
        print("sending ........................... Welcome Email ........................... ")
        print("Hello Welcome to the DRC System.... Please verify Your phone number")
        return redirect('otp')
    return render(request, 'register.html', {'form': form})


def otp(request):
    phone_number = request.session['phone_number']
    form = OTPForm(request.POST or None)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(phone_number=phone_number).first()
        # print("otp>>", otp)
        # print("profile.otp>>", profile.otp)

        print("Hello>>>>>>>>>>", profile.updated_ts.strftime("%m/%d/%Y, %H:%M:%S") > (datetime.datetime.now() - timedelta(minutes=2)).strftime("%m/%d/%Y, %H:%M:%S"))
        # print("Hello>>>>>>>>>>2", (datetime.datetime.now() - timedelta(minutes=2)))
        if otp == profile.otp and (profile.user_attempt < 3 or (
                profile.user_attempt >= 3 and profile.updated_ts.strftime("%m/%d/%Y, %H:%M:%S") < (datetime.datetime.now() - timedelta(minutes=1)).strftime("%m/%d/%Y, %H:%M:%S"))):

            # profile.user.is_active = True
            # if profile.user_attempt >= 3 and profile.updated_ts < datetime.datetime.now()-timedelta(minutes=15):
            profile.user_attempt = 0
            profile.user.is_active = True
            profile.save()
            auth_login(request, profile.user)
            logger.info('{0} Login Successfully'.format(request.user.username))

            return redirect('dashboard')
        else:
            if profile.user_attempt >= 3:
                profile.user.is_active = False
            else:
                profile.user_attempt = 1 + profile.user_attempt
            profile.save()
            logger.error('Invalid OTP')
            messages.add_message(request, messages.ERROR, "Invalid OTP", form.errors)
            return redirect("otp")
    return render(request, 'otp.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        if 'next' in request.GET:
            return redirect(request.GET["next"])
        return redirect("dashboard")
    form = LoginForm(request.POST or None)
    if form.is_valid():
        try:
            user_profile = Profile.objects.get(phone_number=form.cleaned_data['phone_number'])

            # print("valid")
        except Profile.DoesNotExist or User.DoesNotExist:
            logger.error('Invalid login credentials')
            messages.add_message(request, messages.ERROR, "Invalid login credentials", form.errors)
            return redirect("admin_login")
        user = user_profile.user
        if user is not None and user.is_active:
            otp = str(random.randint(1000, 9999))
            user_profile.otp = otp
            user_profile.save()
            logger.info('{0} OTP send Successfully'.format(request.user.username))
            print("Login OTP >>>>>> ", otp)
            request.session['phone_number'] = form.cleaned_data['phone_number']
            return redirect("otp")
        else:
            logger.error('Invalid login credentials')
            messages.add_message(request, messages.ERROR, "Invalid login credentials", form.errors)
    return render(request, "login.html", {'form': form})


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def logout(request):  # logout
    logger.info('{0} Logout Successfully'.format(request.user.username))
    auth_logout(request)
    return redirect("admin_login")


@login_required
def add_emails(request):
    form = AddEmailForm(request.POST or None, request.FILES or None, use_required_attribute=False)
    if form.is_valid():
        email = request.POST.get('email')
        is_primary = request.POST.get('is_primary')
        if User.objects.filter(email__iexact=email).exists() or AddEmails.objects.filter(email__iexact=email).exists():
            logger.error('Email already exist!')
            messages.add_message(request, messages.ERROR, "Email already exist", form.errors)
            return redirect('add_email')
        if is_primary:
            request.user.email = email
            request.user.save()
        else:
            AddEmails(user=request.user, email=email).save()
        logger.info("Email added successfully")
        messages.add_message(request, messages.SUCCESS, "Email added successfully")
        return redirect('list_email')
    return render(request, "profile.html", {"form": form})


@login_required
def list_emails(request):
    return render(request, "list_email.html", {'user_email_obj': AddEmails.objects.filter(user=request.user)})
