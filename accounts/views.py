from django.shortcuts import render
from django.shortcuts import redirect
from . forms import CustomUserCreationForm
from . models import User,UserProfile
from vendor.forms import VendorCreationForm
# message
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if(form.is_valid()):
        
            # Create User using form 
            # password = form.cleaned_data.get('password')
            # form.save(commit=False)
            # form.role = User.CUSTOMER
            # form.set_password(password)
            # form.is_active = True
            # print(form)
            # form.save()

            # Create the User using create_user method
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.createuser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password
            )
            user.role = User.CUSTOMER
            user.is_active = True
            user.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/registerUser.html', context)


def registerVendor(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        v_form = VendorCreationForm(request.POST,request.FILES)
        print(form.is_valid(), v_form.is_valid())
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.createuser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password
            )
            user.role = User.RESTARUNT
            user.is_active = False
            user.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, 'Account created successfully')
            return redirect('registerVendor')
        else:
            print(form.errors, v_form.errors)
    else:

        form = CustomUserCreationForm()
        v_form = VendorCreationForm()
    context = {'form': form, 'v_form': v_form}
    return render(request, 'accounts/registerVendor.html',context)