import uuid
from django.shortcuts import redirect, render_to_response
from requests import Request,post
from django.http import Http404
from django.http import HttpResponse
from .forms import UploadFileForm

def agliq_connect(request):
    state = uuid.uuid4().get_hex()
    request.session['auth_state'] = state
    params = {
        'client_id': 'Xyfu4m8Z7wpzBVX64iNpNBrfzOgnqRhMlL0ZmlboQMPnsAL7Bf',
        'redirect_uri' : 'http://127.0.0.1:8000/agliq_join/callback/',
        'state': state
    }
    agliq_auth_url = 'http://join.agiliq.com/oauth/authorize/'
    r = Request('GET', url=agliq_auth_url, params=params).prepare()
    return redirect(r.url)


def callback(request):
    original_state = request.session.get('auth_state')
    if not original_state:
        raise Http404
    del(request.session['auth_state'])
    state = request.GET.get('state')
    code = request.GET.get('code')
    if not state or not code:
        raise Http404
    if original_state != state:
        raise Http404
    # request token...
    params = {
        'client_id': 'Xyfu4m8Z7wpzBVX64iNpNBrfzOgnqRhMlL0ZmlboQMPnsAL7Bf',
        'client_secret': 'nn2mc75oAALh4GyevHy0bOrOhcrtFHcRBwyOThSzmFfvKY2Ut1',
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/agliq_join/callback/',
    }
    headers = {'accept':'application/json'}
    url = 'http://join.agiliq.com/oauth/access_token/'
    r = post(url, params=params,headers=headers)
    if not r.ok:
        raise Http404
    data = r.json()
    access_token = data['access_token']
    print "Acess token is..",access_token
    form = UploadFileForm()
    return render_to_response("agliq_join/home.html",{'acesstoken':access_token, 'form':form})
