"""This module provides the py_docker_ps cli arguments"""

import argparse

def parse_cli_args():
    """Sets up parser for cli options"""

    my_parser = argparse.ArgumentParser(
        description='use the docker ps command in python',
        add_help=True
    )
    my_parser.version = f"py_docker_ps version: {__version__}"

    my_parser.add_argument(
        '-a',
        '--all',
        action='store',
        help='Show all containers (default shows just running)'
    )
    my_parser.add_argument(
        '-f',
        '--filter',
        action='store',
        help='Filter output based on conditions provided'
    )
    my_parser.add_argument(
        '--format',
        action='store',
        help='Pretty-print containers using a Go template'
    )
    my_parser.add_argument(
        '-n',
        '--last',
        action='store',
        help='Show n last created containers (includes all states)'
    )
    my_parser.add_argument(
        '-l',
        '--latest',
        action='store',
        help='Show the latest created container (includes all states)'
    )
    my_parser.add_argument(
        '--no-trunc',
        action='store',
        help='Don\'t truncate output'
    )
    my_parser.add_argument(
        '-q',
        '--quiet',
        action='store',
        help='Only display container IDs'
    )
    my_parser.add_argument(
        '-s',
        '--size',
        action='store',
        nargs='store',
        help='Display total file sizes'
    )

    args = vars(my_parser.parse_args())

    return args