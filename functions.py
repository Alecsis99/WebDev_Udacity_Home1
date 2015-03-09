__author__ = 'FUrian'

import cgi

def ROT13(s):
    i = 0
    res = ""

    for chr in s:
            if chr.isalpha():
                if chr.isupper(): # Character is uppercase
                    if ord(chr) + 13 > 90:
                        res += unichr(ord(chr) - 13)
                    else:
                        res += unichr(ord(chr) + 13)
                else: # Character is lowercase
                    if ord(chr) + 13 > 122:
                        res += unichr(ord(chr) - 13)
                    else:
                        res += unichr(ord(chr) + 13)
                continue
            res += chr
    return res

def escape_html(s):
    return cgi.escape(s, quote=True)