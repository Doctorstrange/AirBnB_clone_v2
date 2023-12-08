#!/usr/bin/env bash
""" deletes out-of-date archives, using the function do_clean"""
import os
from fabric.api import *

env.hosts = ['52.87.155.66', '54.89.109.87']


def do_clean(number=0):
    """ deletes out-of-date archives, using the function do_clean"""
    number = 1 if int(number) == 0 else int(number)

    table = sorted(os.listdir("versions"))
    [table.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in table]

    with cd("/data/web_static/releases"):
        table = run("ls -tr").split()
        table = [a for a in table if "web_static_" in a]
        [table.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in table]
