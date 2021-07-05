from .models import Profile


def profile_context(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return {'prof': profile}
    return 'you have to login first'
