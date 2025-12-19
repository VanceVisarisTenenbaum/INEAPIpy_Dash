# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 13:26:48 2025

@author: mano
"""



def add_new_son(old_sons_list, new_son):
    for son in old_sons_list:
        if son['props']['id'] == new_son.id:
            # Si encuentra un hijo con el mismo id no se actualiza.
            return old_sons_list
    old_sons_list.append(new_son)
    return old_sons_list

def remove_sons(sons_list, starting_index):
    return sons_list[:starting_index]

