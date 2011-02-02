# -*- coding: UTF-8 -*-

'''
Created on 29/01/2011

@author: ThiagoP
'''
from exceptions import Exception

from models import Map
from string import upper

def geraChave():
    ct = Map.objects.count()
    ct += 1
    
    if len(baseN(ct, 36)) > 6:
        raise Exception("Ultrapassou o limite de URL's suportadas pelo serviço.")
    
    retorno = '0'*(6-len(baseN(ct, 36)))+baseN(ct, 36)
    
    return upper(retorno)


"""
O código abaixo foi retirado de:
http://code.activestate.com/recipes/65212-convert-from-decimal-to-any-base-number/
"""
def baseN(num, base, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    """
    Convert any int to base/radix 2-36 string. Special numerals can be used
    to convert to any base or radix you need. This function is essentially
    an inverse int(s, base).

    For example:
    >>> baseN(-13, 4)
    '-31'
    >>> baseN(91321, 2)
    '10110010010111001'
    >>> baseN(791321, 36)
    'gyl5'
    >>> baseN(91321, 2, 'ab')
    'babbaabaababbbaab'
    """
    if num == 0:
        return "0"

    if num < 0:
        return '-' + baseN((-1) * num, base, numerals)

    if not 2 <= base <= len(numerals):
        raise ValueError('Base must be between 2-%d' % len(numerals))

    left_digits = num // base
    if left_digits == 0:
        return numerals[num % base]
    else:
        return baseN(left_digits, base, numerals) + numerals[num % base]
    