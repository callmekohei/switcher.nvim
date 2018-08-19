# ===========================================================================
#  FILE    : switcher.py
#  AUTHOR  : callmekohei <callmekohei at gmail.com>
#  License : MIT license
# ===========================================================================

import neovim

import multiprocessing
import os

from AppKit import NSObject, NSTextInputContext , NSTextView
from AppKit import NSTextInputContextKeyboardSelectionDidChangeNotification
from PyObjCTools import AppHelper
import objc
import Foundation


@neovim.plugin
class Switcher(object):

    def __init__(self, vim):

        self.vim = vim

        # create Cocoa's text obj
        self.text_input_context = NSTextInputContext.alloc().initWithClient_( NSTextView.new() )

        # create observer obj
        self.obs = Observer.new().initWithValue_( self.text_input_context )

        # create notify obj
        notify_obj = Foundation.NSNotificationCenter.defaultCenter()

        # add handle to notify obj
        notify_obj.addObserver_selector_name_object_(
              self.obs
            , 'bundle:'
            , NSTextInputContextKeyboardSelectionDidChangeNotification
            , None
        )

        p = Worker()
        # p.start() # Error! : Python quit unexpectedly.

    @neovim.function("SwitchEnglish", sync=False)
    def switchEnglish(self, args):

        if self.obs.lang != "com.apple.keylayout.US" :
            self.text_input_context.setValue_forKey_('com.apple.keylayout.US', 'selectedKeyboardInputSource')
        else:
            pass

    @neovim.function("IsUS", sync=True)
    def isUS(self, args):

        try:
            foo = self.obs.lang
            self.vim.command( 'echo "foo is {foo}"'.format(foo = foo ) )
        except Exception as e:
            self.vim.command( 'echo "error is {foo}"'.format(foo = str(e) ))


class Worker(multiprocessing.Process):

    # console loop
    def run(self):
        AppHelper.runConsoleEventLoop(installInterrupt=True)

    def __del__(self):
        AppHelper.stopEventLoop()


class Observer(NSObject):

    def initWithValue_(self, txtObj):

        self.txtObj = txtObj
        self = objc.super(Observer, self).init()
        self.lang = 'foo'
        return self

    def bundle_(self, aNotification):

        s = self.txtObj.selectedKeyboardInputSource()

        path_w = '/Users/callmekohei/tmp/foo.txt'
        with open(path_w, mode='w') as f:
            f.write( 'callmekohei: ' + foo )

        self.lang = s
