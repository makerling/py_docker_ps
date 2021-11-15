"""This module provides the py_docker_ps main module"""

from columnar import columnar

class Container():

    """A Class used to represent a docker connection"""

    @staticmethod
    def create_table(data, cont_data):
        """Creates columnar table from arguments"""

        headers = ['CONTAINER ID', 'IMAGE', 'COMMAND', 'CREATED', 'STATUS', 'PORTS', 'NAMES']
        if len(cont_data) > 0:
            table = columnar(data, headers, no_borders=True)
            print(table)
        else:
            print("{:<15} {:<15} {:<26} {:<15} {:<26} {:<10} {n}". \
            format('CONTAINER ID', 'IMAGE', 'COMMAND', 'CREATED', 'STATUS', 'PORTS', n='NAMES'))


    def __init__(self, dall, last, latest, notrunc, quiet):

        self.dall = dall
        self.last = last
        self.latest = latest
        self.notrunc = notrunc
        self.quiet = quiet

    def data_scope(self, dcont):
        """Determines the logic of the arguments from user input"""

        cont_data = dcont.containers(limit=self.latest)
        if self.last:
            self.latest = 1
        if self.latest > 0:
            cont_data = dcont.containers(limit=self.latest)

        if self.notrunc or self.quiet:
            cont_data = dcont.containers(all=True)

        if (self.notrunc or self.quiet) \
            and self.latest > 0:
            cont_data = dcont.containers(limit=self.latest)

        self.generate(cont_data)

    def generate(self, cont_data):
        """Generates a list of all docker containers"""

        data = []

        if self.notrunc is True:
            for row in cont_data:
                data.append([
                    row['Id'],
                    row['Image'],
                    row['Command'],
                    row['Created'],
                    row['Status'],
                    ''.join(row['Ports']),
                    row['Names'][0][1:]
                    ])
        elif self.quiet is True:
            for row in cont_data:
                data.append([row['Id']])
        else:
            for row in cont_data:
                data.append([
                    row['Id'][0:12],
                    row['Image'][7:19],
                    row['Command'][0:21],
                    row['Created'],
                    row['Status'],
                    ''.join(row['Ports']),
                    row['Names'][0][1:]
                    ])

        self.create_table(data, cont_data)
