__author__ = 'yusuf'
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from gaadi.models import user_master
from django.http import Http404
from gaadi_panel import config

# region logging
login_log = config.myLog.get_logger('login')
config.myLog.setup_logger('login', config.log_path + '/login.logs')
login_log.setLevel(1)
# endregion

def login(request):
    context_data = None
    request.session.set_expiry(3600)
    try:
        if not request.session.get('auth', default=True):
            return HttpResponseRedirect('/dashboard')
        url = "/"
        context_data = {'tname': "Gaadi", "aUrl": url, "error": "false"}
        if len(request.POST):
            print request.POST.getlist('username')
            print request.POST.getlist('password')
            username = request.POST['username']
            password = request.POST['password']
            remember = request.POST.getlist('remember_me')
            user_details = user_master.user_authenticaton(username, password)
            print user_details
            if user_details:
                if remember:
                    request.session.set_expiry(86400)
                request.session['user_id'] = user_details[0]['user_id']
                request.session['username'] = user_details[0]['username']
                request.session['role_id'] = str(user_details[0]['role_id'])
                request.session['auth'] = False
                return HttpResponseRedirect('/dashboard')
            else:
                context_data['error'] = "true"
    except Exception as e:
        login_log.info("Exception: " + str(e))
    print "inside login7"
    context = RequestContext(request, context_data)
    template = loader.get_template('login/login.html')
    return HttpResponse(template.render(context))


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')