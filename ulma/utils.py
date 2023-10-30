import requests

class Utils:

    def __init__(self):
        self.mode = None

    def set_mode(self):
        try:
            r = requests.get("https://google.com")

            if r.status_code == 200 or r.status_code == 301:
                self.mode = "online"
            else:
                self.mode = "offline"
        except:
            self.mode = "offline"

    def get_mode(self):
        if self.mode is None:
            self.set_mode()

        return self.mode
    
    
