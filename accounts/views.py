from django.shortcuts import render
from django.shortcuts import redirect
from . forms import CustomUserCreationForm

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('registerUser')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/registerUser.html', context)