#!/usr/bin/env bash
"""distributes an archive to your web servers, using the function do_deploy"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.157.145.222', '100.26.227.184']


def do_deploy(archive_path):
    """archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_name_no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_name_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, file_name_no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_name_no_ext))
        run('rm -rf {}{}/web_static'.format(path, file_name_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_name_no_ext))
        return True
    except:
        return False
