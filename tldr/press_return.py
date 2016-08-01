'''presses return key is all'''
from pykeyboard import PyKeyboard as PyK


def tap_return():
    '''single press of return key'''
    k = PyK()
    k.tap_key(k.return_key)


tap_return()
