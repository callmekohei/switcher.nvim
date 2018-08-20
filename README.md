# switcher.nvim

switcher.nvim is tiny util tool.

auto switch 'com.apple.keylayout.US' from any keyboard input sources when it's just normal mode from insert mode.

```
              insert      normal
------------------------------
Input Source  any     ->  'com.apple.keylayout.US'
```

## require

macOSX  
pyobjc-core  
pyobjc-framework-Cocoa  

```shell
$ pip3 install pyobjc-core
$ pip3 install pyobjc-framework-Cocoa
```

## install

```shell
$ git clone --depth 1 https://github.com/callmekohei/switcher.nvim

$ nvim .vimrc
    set runtimepath+=/path/to/switcher.nvim

$ nvim
    :UpdateRemotePlugins
```

## vimrc

Neovim / MacVim
```vim
autocmd InsertLeave * :call SwitchEnglish('')
```

Vim ( It's not recommend! Very Very Slow! )
```vim
autocmd InsertLeave * :call SwitchEnglish('')
```

## option

if you use your favarit keyboard input source ...

```vim
  let g:switcher_keyboardInputSource = 'your favarite keyboard input source'
```

check code

1. create `foo.py`

```python
# foo.py
from AppKit import NSTextInputContext , NSTextView

txt = NSTextInputContext.alloc().initWithClient_( NSTextView.new() )
print( txt.selectedKeyboardInputSource() )
```

2. write command
```shell
$ python3 foo.py
```

3. set your favarite keyboard input source  

4. return
```shell
$ python3 foo.py <Return>
com.apple.keylayout.ABC
```




