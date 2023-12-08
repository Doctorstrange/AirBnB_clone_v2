#!/usr/bin/env bash
"""creates and distributes an archive to your web servers"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.157.145.222', '100.26.227.184']


def do_pack():
    """make tgz archive"""
    
    time = datetime.now()
    archive_name = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(archive_name))
    if archive is not None:
        return archive_name
    else:
        return None

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


def deploy():
    """creates and transfer archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
