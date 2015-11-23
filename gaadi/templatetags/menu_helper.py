__author__ = 'yusuf'

from django import template
import operator
from gaadi.models import roles_model

register = template.Library()


@register.inclusion_tag('commons/sidebar_menues.html')
def menu_creator(role_id):
    print "ROLE ID = %s"%role_id
    menu_data = []
    try:
        result = roles_model.get_roles_menu(role_id)
        main_menus=[]
        sub_menus=[]
        for row in result:
          if row['menu_type']=="main_menu":
            main_menus.append(row)
          else:
            sub_menus.append(row)

        for a in main_menus:
            a['sub_menu']=[]

        for menu_data in main_menus:
            for sub in sub_menus:
                if sub['parent_id']==menu_data['menu_id']:
                    menu_data['sub_menu'].append(sub)
        print main_menus
    except Exception as e:
        print e
    return {"role_menu": main_menus}