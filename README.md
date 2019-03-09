# Journal

journal is a simple script to ease the manipulation/writing of a diary. You run
one command (the script and it will `git pull` then give your editor. Once you
quit it, it will let you enter a commit message. A default message is the date
if you don't want to write a specific one. Finally it pushes the result to the
git repo so you can sync/backup your journal.

# Usage

```
$ mkdir -p /path/to/where/you/want/your/repo
$ cd /path/to/where/you/want/your/repo
$ $EDITOR journal.txt # and write your first entry
$ ftp/wget/curl https://raw.githubusercontent.com/danieljakots/journal/master/journal.py
$ sed -i "s,/path/to/your/journal/repo/,`echo $PWD`," journal.py # update REPO_PATH
$ git init . && git add journal.* && git commit -m "Initial commit"
$ git remote add origin ssh://git@example.com/foo.git
$ git push --set-upstream origin master
[wait until you want to write your second entry]
$ ./journal.py
[everyday]
$ ./journal.py
```
