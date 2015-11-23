__author__ = 'yusuf'
import logging
from gaadi.models import connections

dbconn = connections.mysql_con('gaadi_panel')
logger = logging.getLogger("default")

def get_roles_menu(role_id):
    query = """SELECT m.* FROM menu m
            INNER JOIN role_menu rm ON m.`menu_id` = rm.`menu_id`
            INNER JOIN user_master um ON rm.`role_id` = um.`role_id`
            WHERE um.`role_id` = %s ORDER BY m.order """%role_id
    role_menu = dbconn.execute_query(query)
    return role_menu


