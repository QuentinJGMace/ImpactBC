import pysftp
from sftp_manager.config import *

FOLDER = "/bilan_carbone_home"

# with pysftp.Connection(HOSTNAME, username=USERNAME, password=PASSWORD) as sftp:

#     with sftp.cd(FOLDER):
#         sftp.put('/pycode/filename')
#         sftp.get('remote_file')


class SFTPConnector:

    def __init__(self):
        self.sftp = None

    def connect(self):
        if self.sftp != None:
            self.sftp.close()
        self.sftp = pysftp.Connection(
            HOSTNAME, username=USERNAME, password=PASSWORD)

    def close(self):
        if self.sftp != None:
            self.sftp.close()
            self.sftp = None

    def upload(self, filename):
        if self.sftp != None:
            with self.sftp.cd(FOLDER):
                self.sftp.put(filename)
