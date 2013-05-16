Storage for
`django-dbbackup <https://pypi.python.org/pypi/django-dbbackup/>`_ using
WEB-DAV api `yandexwebdav <https://pypi.python.org/pypi/yandexwebdav>`_
to work with disk.yandex.ru

django settings for
`django-dbbackup <https://pypi.python.org/pypi/django-dbbackup/>`_

    DBBACKUP\_MEDIA\_PATH = MEDIA\_ROOT

    DBBACKUP\_STORAGE = 'dbbackupyandexdisk.yandex\_storage'

Remote directory on yandex disk

    DBBACKUP\_YANDEX\_DIRECTORY=' remote directory '

Authorization

    YANDEX\_DISK\_NAME=' username '

    YANDEX\_DISK\_PASSWORD=' password '
