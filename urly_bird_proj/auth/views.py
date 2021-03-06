from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf

def login_user(request):
    c = {}
    c.update(csrf(request))
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html', {'state':state, 'username': username})
                            #how do I get the "c" in here without breaking things?
                            #context_instance=RequestContext(requeset) tried this too