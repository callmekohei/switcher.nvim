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
neovim
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

## Great thanks

[pudquick/input_sources.py](https://gist.github.com/pudquick/cff1ecdc02b4cabe5aa0dc6919d97c6d)

[Khande/auto_switch_kb.py](https://gist.github.com/Khande/76f24ba90607fb5d54185bd8e4520de6)

[How can we reading / coerce CFArray and CFString etc values from within OS X JXA?](https://stackoverflow.com/a/35007079)
