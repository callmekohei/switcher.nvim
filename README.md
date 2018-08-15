# switcher.nvim

switcher.nvim is tiny util tool.

auto switch ascii from Japanese when it's just normal mode from insert mode.

```
mode     insert       normal
------------------------------
keycode  102          102
keycode  104     ->   102
```

## require

Neovim  
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

not especially
