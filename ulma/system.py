from __future__ import absolute_import

import subprocess

from time import sleep

class System:

    def __init__(self):
        self.command = None
        self.result = None

    def execute(self, commands):
        results = []
        if len(commands) > 0:
            for command in commands:
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                result = process.stdout.readlines()
                self.parse_output(result)
                results.append(self.result)
                sleep(.5)

        return results

    def parse_output(self, result):
        self.result = ""
        for line in result:
            line.strip("\n")
            line = line.replace("‚", "e")
            line = line.replace("…", "a")
            line = line.replace("ÿ", " ")
            
            self.result += line
        