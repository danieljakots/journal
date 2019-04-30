#!/usr/bin/env python3

# Copyright (c) 2019 Daniel Jakots
#
# Licensed under the MIT license. See the LICENSE file.

import datetime
import os
import subprocess

REPO_PATH = "/path/to/your/journal/repo/"


def now_to_strftime(strf_t_format):
    now = datetime.datetime.now()
    return now.strftime(strf_t_format)


def run_editor(editor):
    subprocess.run([editor, f"{REPO_PATH}/journal.txt"])


def git(action, *args):
    args = list(args)  # otherwise it's a tuple? wtf?
    subprocess.run(["git", "-C", REPO_PATH, action] + args)


def add_day_marker(path):
    with open(path, "r+") as f:
        if f.readline().strip("\n") == now_to_strftime("%Y-%m-%d"):
            return
        f.seek(0, 0)
        content = f.read()
        f.seek(0, 0)
        f.write(now_to_strftime("%Y-%m-%d") + '\n\n\n' + content)


def get_editor():
    return os.environ.get("VISUAL") or os.environ.get("EDITOR") or "vim"


def main():
    git("pull")
    add_day_marker(f"{REPO_PATH}/journal.txt")
    run_editor(get_editor())
    git("add", f"{REPO_PATH}/journal.txt")
    # first, commit with a default commit message but offer the user to change it
    git("commit", "-m", now_to_strftime("%Y/%m/%d %H:%M"))
    git("commit", "-v", "--amend")
    git("push")


if __name__ == "__main__":
    main()
