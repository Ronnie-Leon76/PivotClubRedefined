from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {'user': user})


@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.save()

            user_profile.bio = form.cleaned_data['bio']
            user_profile.course = form.cleaned_data['course']
            user_profile.reg_no = form.cleaned_data['reg_no']
            user_profile.team = form.cleaned_data['team']
            user_profile.save()

            return HttpResponseRedirect(reverse('account:profile'))
    else:
        default_data = {'username': user.username,
                        'bio': user_profile.bio, 'course': user_profile.course,
                        'reg_no':user_profile.reg_no, 'team':user_profile.team}
        form = ProfileForm(default_data)

    return render(request, 'account/profile_update.html', {'form': form, 'user': user})