__author__ = 'yusuf'

import datetime
import json
import logging
from gaadi.models import connections
from django.http import HttpResponse
from django.template import RequestContext, loader

logger = logging.getLogger("default")

def dashboard(request):
    con = connections.mysql_con('gaadi')
    result = con.execute_query("SELECT * FROM vmn_cp")
    context_data = {'body_template': 'dashboard/dashboard.html', 'session_data': request.session, 'vmn_table':result}
    print "inside dashboard"
    try:
        user_id = request.session['user_id']
    except Exception as e:
        logger.error("dashboard : " + str(e))
    context = RequestContext(request, context_data)
    template = loader.get_template('commons/main_include.html')
    return HttpResponse(template.render(context))
