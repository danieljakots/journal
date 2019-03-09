#!/usr/bin/env python3

# Copyright (c) 2019 Daniel Jakots
#
# Licensed under the MIT license. See the LICENSE file.

import datetime
import tempfile
import os
import subprocess

REPO_PATH = "/path/to/your/journal/repo/"


def commit_message():
    with tempfile.NamedTemporaryFile(mode="r+", suffix=".tmp") as tf:
        tf.write(now_to_strftime())
        tf.flush()
        subprocess.run(["vim", tf.name])
        tf.seek(0)
        edited_message = tf.read()
    return edited_message


def now_to_strftime():
    now = datetime.datetime.now()
    return now.strftime("%Y/%m/%d %H:%M")


def run_editor(editor):
    subprocess.run([editor, f"{REPO_PATH}/journal.txt"])


def git(action, *args):
    args = list(args)  # otherwise it's a tuple? wtf?
    subprocess.run(["git", "-C", REPO_PATH, action] + args)


def load_current_journal(path):
    with open(path, "r") as f:
        f.read()


def get_editor():
    return os.environ.get("VISUAL") or os.environ.get("EDITOR") or "vim"


def main():
    git("pull")
    run_editor(get_editor())
    git("add", f"{REPO_PATH}/journal.txt")
    # first, commit with a default commit message but offer the user to change it
    git("commit", "-m", now_to_strftime())
    git("commit", "-v", "--amend")
    git("push")


if __name__ == "__main__":
    main()
