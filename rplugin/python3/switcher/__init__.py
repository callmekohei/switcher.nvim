# ===========================================================================
#  FILE    : switcher.py
#  AUTHOR  : callmekohei <callmekohei at gmail.com>
#  License : MIT license
# ===========================================================================

import neovim
from AppKit import NSTextInputContext , NSTextView

@neovim.plugin
class Switcher(object):
    def __init__(self, vim):
        self.vim = vim
        self.text_input_context = NSTextInputContext.alloc().initWithClient_( NSTextView.new() )

    @neovim.function("SwitchEnglish", sync=False)
    def switchEnglish(self, args):
        KeyboardInputSource = self.vim.eval('g:switcher_keyboardInputSource')
        self.text_input_context.setValue_forKey_( KeyboardInputSource , 'selectedKeyboardInputSource')
