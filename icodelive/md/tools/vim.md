## vim

Move to:
    
    `k` move up  
    `l` move right  
    `j` move down  
    `h` move left  
        
    `w` move to start of next word  
    `e` move to end of next word  

    `^` move to start of current line  
    `$` move to end of current line  
    
Find character:

    `f` char move to next occurrence of char  
    `F` char move back to previous occurrence of char  

    `t` char move to just before next occurrence of char  
    `T` char move back to just before previous occurrence of char  

cmd {i|a} shortcuts:

d delete:
    
    `dd` delete line  
    `dw` delete word  
    `d$` delete to end of line  
    `d^` delete to start of line  

d{i|a} delete:

    **i**nside quotes `di"`
    **a**ll including quotes `da"`

y Yank:

    `yy` yank line
    `yw` yank word
    `y$` yank to end of line
    `y^` yank to start of line

y{i|a} yank:

    **i**nside quotes `yi"`
    **a**ll including quotes `ya"`

c Change:

    .. `cw` change word (not working )
    `ciw` (change inner word) will change the whole word under the cursor
    `c$` change to end of line
    `c^` change to start of line

c{i|a} change:

    **i**nside quotes `ci"` (it deletes and put you in insert mode)
    **a**ll including quotes `ca"` (it deletes and put you in insert mode)

other useful commands:

    `ctrl-o` temporally go into command mode (shortcut for; Esc, command, i)
    `.` repeat last *set* of command
    `:lclose` - Hides the Location Panel (error messages ...)

