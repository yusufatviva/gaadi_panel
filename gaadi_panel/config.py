__author__ = 'yusuf'
import os
from gaadi_panel import settings
from gaadi.models import logClass


# <!--*********************Log setting*********************-->
log_path = os.path.join(settings.BASE_DIR, 'logs')
if not (os.path.exists(log_path)):
    os.makedirs(log_path)
myLog = logClass.Log()
# <!--*****************************************************-->
