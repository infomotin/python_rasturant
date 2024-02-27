from django.shortcuts import render
from django.shortcuts import redirect
from . forms import CustomUserCreationForm
from . models import User

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

            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/registerUser.html', context)