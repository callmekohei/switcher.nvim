# ===========================================================================
#  FILE    : switcher_wrap.py
#  AUTHOR  : callmekohei <callmekohei at gmail.com>
#  License : MIT license
# ===========================================================================

from switcher import Switcher as _Switcher
import vim

_obj = _Switcher(vim)

def switchEnglish(*args):
    return _obj.switchEnglish(args)

def isUS(*args):
    return _obj.isUS(args)
