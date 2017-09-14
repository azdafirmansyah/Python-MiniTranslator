'''
Created on 14 Sep 2017

@author: Azda Firmansyah
'''
from textblob import TextBlob
from LanguageData import isLanguangeExist

class Translate():
    def __init__(self, lang_from, lang_to):
        self.lang_from = lang_from
        self.lang_to = lang_to
        self._translate_allow = False
        
    @property
    def translate_allow(self):
        return self._translate_allow
    
    @translate_allow.setter
    def translate_allow(self, value):
        if value:
            text = input("Enter Text to Translate :")
            if len(text) > 0:
                blob = TextBlob(text)
                print("Please wait...\nTranslate in progress")
                print("--->>>",blob.translate(from_lang=lang_from, to=lang_to))
                self.translate_allow = value
            else:
                print("Please Input Text, Try Again")
                self.translate_allow = value

lang_from = input("Input 'From' Languange ID :")
lang_to = input("Input 'To' Languange ID :")

is_from = isLanguangeExist(lang_from)
is_to = isLanguangeExist(lang_to)

if is_from and is_to == True:
    #print(True)
    T = Translate(lang_from, lang_to)
    T.translate_allow = True
    T.translate_allow
else:
    if is_from == False:
        print("Languange 'From' Not Found")
    if is_to == False:
        print("Languange 'To' Not Found")
