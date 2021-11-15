from docker import client
from cliparser import parse_cli_args
import docker_ps as d

# create a client object to connect to the daemon
DC = client.Client(base_url='unix://var/run/docker.sock')

def main():
    """Parses user input and passes those values to the Container object"""

    args = parse_cli_args()

    dall = args['all']
    dfilter = args['filter']
    dformat = args['format']
    last = args['last']
    latest = args['latest']
    notrunc = args['notrunc']
    quiet = args['quiet']
    size = args['size']     

    container = d.Container(dall, dfilter, dformat, last, latest, notrunc, quiet, size)
    container.generate(DC)

if __name__ == "__main__":
    main()