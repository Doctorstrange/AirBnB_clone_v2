#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    archive_name = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(archive_name))
    if archive is not None:
        return archive_name
    else:
        return None
