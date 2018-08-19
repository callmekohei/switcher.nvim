# ===========================================================================
#  FILE    : switcher.py
#  AUTHOR  : callmekohei <callmekohei at gmail.com>
#  License : MIT license
# ===========================================================================

import neovim
from AppKit import NSObject, NSTextInputContext , NSTextView

@neovim.plugin
class Switcher(object):
    def __init__(self, vim):
        self.vim = vim
        self.text_input_context = NSTextInputContext.alloc().initWithClient_( NSTextView.new() )

    @neovim.function("SwitchEnglish", sync=False)
    def switchEnglish(self, args):
        self.text_input_context.setValue_forKey_('com.apple.keylayout.US', 'selectedKeyboardInputSource')
