" ===========================================================================
"  FILE    : switcher.vim
"  AUTHOR  : callmekohei <callmekohei at gmail.com>
"  License : MIT license
" ===========================================================================

if exists('g:loaded_switcher')
  finish
endif
let g:loaded_switcher = 1

if ! exists( 'g:switcher_keyboardInputSource' )
  let g:switcher_keyboardInputSource = 'com.apple.keylayout.US'
endif

if has('nvim')
  finish
endif

let s:switcher = yarp#py3('switcher_wrap')

function! SwitchEnglish(v)
  return s:switcher.call('switchEnglish',a:v)
endfunction
