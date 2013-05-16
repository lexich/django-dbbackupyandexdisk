__author__ = 'lexich'

"""
Yandex Storage object.

"""
import os, tempfile
from dbbackup.storage.base import BaseStorage, StorageError
from django.conf import settings
from yandexwebdav import Config

################################
#  Filesystem Storage Object
################################

class Storage(BaseStorage):
    """ Filesystem API Storage. """
    BACKUP_DIRECTORY = getattr(settings, 'DBBACKUP_YANDEX_DIRECTORY', None)
    BACKUP_DIRECTORY = '/%s/' % BACKUP_DIRECTORY.strip('/')

    def __init__(self, server_name=None):
        self.conf = Config(dict(
            user=getattr(settings, "YANDEX_DISK_NAME"),
            password=getattr(settings, "YANDEX_DISK_PASSWORD")
        ))
        self._check_filesystem_errors()
        self.name = 'YandexDisk'
        BaseStorage.__init__(self)

    def _check_filesystem_errors(self):
        """ Check we have all the required settings defined. """
        if not self.BACKUP_DIRECTORY:
            raise StorageError('Yandexdisk storage requires DBBACKUP_YANDEX_DIRECTORY to be defined in settings.')

    ###################################
    #  DBBackup Storage Methods
    ###################################

    def backup_dir(self):
        return self.BACKUP_DIRECTORY

    def delete_file(self, filepath):
        """ Delete the specified filepath. """
        self.conf.delete(filepath)

    def list_directory(self):
        """ List all stored backups for the specified. """
        folders, files = self.conf.list(self.backup_dir())
        return files.keys()

    def write_file(self, filehandle):
        """ Write the specified file. """
        href = os.path.join(self.backup_dir(), filehandle.name)
        filehandle.seek(0, 2)
        length = filehandle.tell()
        filehandle.seek(0)
        self.conf.write(filehandle._file, href, length=length)

    def read_file(self, filepath):
        """ Read the specified file and return it's handle. """
        return self.conf.download(filepath)