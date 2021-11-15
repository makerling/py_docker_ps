"""This module provides the py_docker_ps cli arguments"""

import argparse

def parse_cli_args():
    """Sets up parser for cli options"""

    my_parser = argparse.ArgumentParser(
        description='use the docker ps command in python',
        add_help=True
    )

    my_parser.add_argument(
        '-a',
        '--all',
        action='store_true',
        default=False,
        help='Show all containers (default shows just running)'
    )
    my_parser.add_argument(
        '-n',
        '--last',
        action='store_true',
        help='Show n last created containers (includes all states)'
    )
    my_parser.add_argument(
        '-l',
        '--latest',
        action='store',
        default=0,
        type=int,
        help='Show the latest created container (includes all states)'
    )
    my_parser.add_argument(
        '--notrunc',
        action='store_true',
        default=False,
        help='Don\'t truncate output'
    )
    my_parser.add_argument(
        '-q',
        '--quiet',
        action='store_true',
        default=False,
        help='Only display container IDs'
    )

    args = vars(my_parser.parse_args())

    return args
    