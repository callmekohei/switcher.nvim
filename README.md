# switcher.nvim

switcher.nvim is tiny util tool.

auto switch en when it's just normal mode from insert mode.

```
              insert      normal
------------------------------
Input Source  any     ->  en
```

## require

macOSX  
pyobjc-core  
pyobjc-framework-Cocoa  

```
$ pip3 install pyobjc-core
$ pip3 install pyobjc-framework-Cocoa
```

## install

```
$ git clone --depth 1 https://github.com/callmekohei/switcher.nvim

$ nvim .vimrc
  set runtimepath+=/path/to/switcher.nvim

$ nvim
    :UpdateRemotePlugins

```

## usage

Neovim / MacVim
```
autocmd InsertLeave * :call SwitchEnglish('')
```

Vim ( It's not recommend! Very Very Slow! )
```
autocmd InsertLeave * :call SwitchEnglish('')
```
