from __future__ import absolute_import
from __future__ import print_function

from multiprocessing import Process

from ulma.endpoint import Endpoint
from ulma.utils import Utils

if __name__ == "__main__":

    mode = Utils().get_mode()
    endpoint = Endpoint()

    receive_command_process = Process(target=endpoint.receive_command)
    receive_command_process.start()
    receive_command_process.join()

    #endpoint.receive_command()