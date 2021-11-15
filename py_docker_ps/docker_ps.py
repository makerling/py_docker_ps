"""This module provides the py_docker_ps main module"""

class Container():

    """A Class used to represent a docker connection"""

    def __init__(self, dall, dfilter, dformat, last, latest, notrunc, quiet, size):

        self.dall = dall
        self.dfilter = dfilter
        self.dformat = dformat
        self.last = last
        self.latest = latest
        self.notrunc = notrunc
        self.quiet = quiet
        self.size = size        

    def generate(self, dc):
        """Generates the py-docker-ps command to be run"""

        pass

