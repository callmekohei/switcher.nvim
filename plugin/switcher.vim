" ===========================================================================
"  FILE    : switcher.vim
"  AUTHOR  : callmekohei <callmekohei at gmail.com>
"  License : MIT license
" ===========================================================================

if has('nvim')
  finish
endif

let s:switcher = yarp#py3('switcher_wrap')

function! SwitchEnglish(v)
  return s:switcher.call('switchEnglish',a:v)
endfunction
