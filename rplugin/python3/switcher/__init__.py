# ===========================================================================
#  FILE    : switcher.py
#  AUTHOR  : callmekohei <callmekohei at gmail.com>
#  License : MIT license
# ===========================================================================

   # ----------------------------------------------------
   # Great thanks:
   #     Github: https://gist.github.com/pudquick/cff1ecdc02b4cabe5aa0dc6919d97c6d
   #     pudquick/input_sources.py
   #
   #     stackoverflow: https://stackoverflow.com/a/35007079
   #     How can we reading / coerce CFArray and CFString etc values from within OS X JXA?
   # ----------------------------------------------------

from Foundation import NSBundle
import ctypes
import ctypes.util
import neovim
import objc
import os

@neovim.plugin
class Switcher(object):
    def __init__(self, vim):
        self.vim = vim

        # import Carbon by now
        carbon_path = ctypes.util.find_library('Carbon')
        carbon = ctypes.cdll.LoadLibrary(carbon_path)

        # use HITToolbox's functions
        HIToolbox_bundle = NSBundle.bundleWithIdentifier_("com.apple.HIToolbox")

        # bundle many...
        HIToolbox_functions = [ ('TISGetInputSourceProperty', b'@@@'), ('TISCopyCurrentKeyboardInputSource', b'@') ]
        objc.loadBundleFunctions(HIToolbox_bundle, globals(), HIToolbox_functions)

        HIToolbox_constants = [('kTISPropertyInputModeID', b'@') ]
        objc.loadBundleVariables(HIToolbox_bundle, globals(), HIToolbox_constants)


    @neovim.autocmd('InsertLeave', pattern='*', eval='expand("<afile>")', sync=False)
    def autocmd_handler(self, filename):

        if TISGetInputSourceProperty(TISCopyCurrentKeyboardInputSource() , kTISPropertyInputModeID) == None :

            pass

        else:

            # TODO: do by objctive-c with python

            cmd = """
            osascript -e 'tell application "System Events" to key code 102' &
            """

            os.system(cmd)
