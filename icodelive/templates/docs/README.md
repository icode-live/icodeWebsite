## usage

```bash
$ cd icodeWebsite

$ python md/mkpage.py templates/tools/index.html md/tools/header_index.md md/tools/terminal.md
$ python manage.py runserver
```

## obsolete. just for info

```bash
$ cd templates
```

[index](file:///home/tac/Dropbox/md/md2html5_icode/templates/home/index.html)

```bash
$ pandoc -t html5 -c ../../static/css/style.css ../md/header.md ../md/header_index.md ../md/index.md ../md/footer.md -o home/index.html
```

[concept](file:///home/tac/Dropbox/md/md2html5_icode/templates/concept/index.html)

```bash
$ pandoc -t html5 -c ../../static/css/style.css ../md/header.md ../md/index.md ../md/footer.md -o concept/index.html
```


[tools](file:///home/tac/Dropbox/md/md2html5_icode/templates/tools/index.html)

```bash
$ pandoc -t html5 -c ../../static/css/style.css ../md/header.md ../md/index.md ../md/footer.md -o tools/index.html
```

[practice](file:///home/tac/Dropbox/md/md2html5_icode/templates/practice/index.html)

```bash
$ pandoc -t html5 -c ../../static/css/style.css ../md/header.md ../md/index.md ../md/footer.md -o practice/index.html
```


