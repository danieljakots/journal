#!/usr/bin/env python3

# Copyright (c) 2019 Daniel Jakots
#
# Licensed under the MIT license. See the LICENSE file.

import datetime
import os
import subprocess

REPO_PATH = "~/git/journal/repo/"


def now_to_strftime(strf_t_format):
    now = datetime.datetime.now()
    return now.strftime(strf_t_format)


def run_editor(editor, repo_path):
    subprocess.run([editor, f"{repo_path}/journal.txt"])


def git(action, repo_path, *args):
    args = list(args)  # otherwise it's a tuple? wtf?
    subprocess.run(["git", "-C", repo_path, action] + args)


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
    repo_path = os.path.expanduser(REPO_PATH)
    git("pull", repo_path)
    add_day_marker(f"{repo_path}/journal.txt")
    run_editor(get_editor(), repo_path)
    git("add", repo_path, f"{repo_path}/journal.txt")
    # first, commit with a default commit message but offer the user to change it
    git("commit", repo_path, "-m", now_to_strftime("%Y/%m/%d %H:%M"))
    git("commit", repo_path, "-v", "--amend")
    git("push", repo_path)


if __name__ == "__main__":
    main()
