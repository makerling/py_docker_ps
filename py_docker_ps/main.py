"""This module provides the py_docker_ps main module"""

from docker import client
from cliparser import parse_cli_args
import docker_ps as d

# create a client object to connect to the daemon
DCONT = client.Client(base_url='unix://var/run/docker.sock')

def main():
    """Parses user input and passes those values to the Container object"""

    args = parse_cli_args()

    dall = args['all']
    last = args['last']
    latest = args['latest']
    notrunc = args['notrunc']
    quiet = args['quiet']

    container = d.Container(dall, last, latest, notrunc, quiet)
    container.data_scope(DCONT)

if __name__ == "__main__":
    main()
