
# Working at the Console


## working in the terminal

[Whitson Gordon](http://lifehacker.com/5743814/become-a-command-line-ninja-with-these-time-saving-shortcuts)

`Up/Down Arrows`: The up and down arrows on your keyboard move through your last used commands.  
`Ctrl+Left` and `Ctrl+Right`: jumps between arguments in your command line  
`Ctrl-a` (or Home) and `Ctrl-e` (or End): jump your cursor to the beginning and the end of the currently typed command line  

`Ctrl+u`: delete the line from cursor position to begin of the line.  
`Ctrl+k`: delete the line from cursor position to the end of the line.  
`Ctrl+w`: This deletes the word before the cursor only.  
`Ctrl+r`: This lets you search your command history for something specific  


## working with the command shell

`Tab`: to autocomplete a text

`cd`   : got to home directory  
`cd -` : go to previous working directory  

`!!`   : represents the last command you ran. ex `sudo !!`  
`!$` : represents the arguments from your last command  
`!` : run last specified command. ex `!cat`  run last command that used *cat*  
`!`command`:p` : show dont run last command use. ex: `!cat:p` see what the last cat command was.  

`^`mispelledCmd`^`Cmd :  find the first instance of mispelledCmd in the last run command and replace it with Cmd. ex `^nanp^nano`  

`history` then `!`number : will repeat the command in your history with the specified number ex: `!455`  

`{}` :  perform batch operations on multiple versions of a file: 
    ex `mv /path/to/file.txt /path/to/file.xml`  
    becomes `mv /path/to/file.{txt,xml}`  
    Make backup `cp /etc/rc.conf{,-old}`  
    Restore backup `mv /etc/rc.conf{-old,}`  
    Make multiple directories `mkdir myfolder{1,2,3}`  


## working with commandline tools

### find

find searches for files in a directory hierarchy

Find Files : `find . –name "*.txt" –mtime 5`  find all files with .txt in the name that were modified in the last 5 days.  

### grep

grep  searches  the  named  input  FILEs  for  lines  containing a match to the given PATTERN.

Find a Text String in Files: `grep –ir "text string" *`
 
</div><!-- container --></section><!-- section -->
