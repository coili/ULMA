import json
import requests
import time

from bs4 import BeautifulSoup
from ulma.utils import Utils

class Endpoint:

    def __init__(self):
        self.command = None
        self.last_command = None
        self.utils = Utils()
        self.set_endpoint()

    def set_endpoint(self):
        if self.utils.get_mode() == "online":
            self.endpoint = "<changeme>"
        else:
            self.endpoint = None

    def get_endpoint(self):
        return self.endpoint
    
    def handle_command(self, content):
        self.command = content[0]
        
        if self.command != self.last_command:
            print("Command actuelle: ", self.command)
            self.last_command = self.command
    
    def receive_command(self):
        while True:
            if self.endpoint is not None:
                page = requests.get(self.get_endpoint())
                
                content = page.text

        time.sleep(5)