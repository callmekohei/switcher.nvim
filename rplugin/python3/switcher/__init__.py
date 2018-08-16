# ===========================================================================
#  FILE    : switcher.py
#  AUTHOR  : callmekohei <callmekohei at gmail.com>
#  License : MIT license
# ===========================================================================

from Foundation import NSBundle
import CoreFoundation
import ctypes
import ctypes.util
import neovim
import objc


@neovim.plugin
class Switcher(object):
    def __init__(self, vim):
        self.vim = vim

        # add carbon lib
        self.carbon = ctypes.cdll.LoadLibrary(ctypes.util.find_library('Carbon'))

        # re-define arg and return types
        self.carbon.TISSelectInputSource.restype           = ctypes.c_void_p
        self.carbon.TISSelectInputSource.argtypes          = [ctypes.c_void_p]
        self.carbon.TISCopyInputSourceForLanguage.argtypes = [ctypes.c_void_p]
        self.carbon.TISCopyInputSourceForLanguage.restype  = ctypes.c_void_p


    @neovim.autocmd('InsertLeave', pattern='*', eval='expand("<afile>")', sync=False)
    def autocmd_handler_switchEnglish(self, filename):

        lang = u'en'

        self.carbon.TISSelectInputSource(
            self.carbon.TISCopyInputSourceForLanguage(
                CoreFoundation.CFSTR(lang).__c_void_p__())
        )

    @neovim.function("SwitchEnglish", sync=False)
    def switchEnglish(self, args):

        lang = u'en'

        self.carbon.TISSelectInputSource(
            self.carbon.TISCopyInputSourceForLanguage(
                CoreFoundation.CFSTR(lang).__c_void_p__())
        )

