'''
Created on 14 Sep 2017

@author: Azda Firmansyah
'''

def getLanguageList():
    data = {
        'id' : 'Indonesia',
        'en' : 'English',
        'fr' : 'France' #Just add another languange if you want to support it
        }
    return data

def isLanguangeExist(lang_param):
    lang_list = getLanguageList()
    if lang_param in lang_list:
        return True
    else:
        return False 
