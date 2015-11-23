__author__ = 'yusuf'
from gaadi.models import connections
import logging

dbconn = connections.mysql_con('gaadi_panel')
logger = logging.getLogger(__name__)

def user_authenticaton(username, password):
    logger.info(username)
    query = """SELECT user_id, username, role_id FROM user_master WHERE username="%s" AND password="%s" """%(username,password)
    result = dbconn.execute_query(query)
    print result
    return result