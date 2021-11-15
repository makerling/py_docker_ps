"""This module provides the py_docker_ps main module"""

from columnar import columnar

class Container():

    """A Class used to represent a docker connection"""

    def __init__(self, dall, last, latest, notrunc, quiet):

        self.dall = dall
        self.last = last
        self.latest = latest
        self.notrunc = notrunc
        self.quiet = quiet       

    def container_generate(self, dc):
        """Generates a list of all docker containers"""
        data = []

        if self.last is True:            
            c = dc.containers(limit = 1)
        if self.latest > 0:            
            c = dc.containers(limit = self.latest)
        else: 
            c = dc.containers(all = self.dall)  

        if self.notrunc is True:
            c = dc.containers(all = True)
            for x in c:
                data.append([
                    x['Id'],
                    x['Image'],
                    x['Command'],
                    x['Created'],
                    x['Status'],
                    ''.join(x['Ports']),
                    x['Names'][0][1:]
                    ])
        elif self.quiet is True:
            c = dc.containers(all = True)
            for x in c:
                data.append([x['Id']])
        else:
            for x in c:
                data.append([
                    x['Id'][0:12],
                    x['Image'][7:19],
                    x['Command'][0:21],
                    x['Created'],
                    x['Status'],
                    ''.join(x['Ports']),
                    x['Names'][0][1:]
                    ])

        self.create_table(data)

    def create_table(self,data):
        headers = ['CONTAINER ID','IMAGE','COMMAND','CREATED','STATUS','PORTS','NAMES']        
        if len(c) > 0: 
            table = columnar(data, headers, no_borders=True)
            print(table)
        else:
            print ("{:<15} {:<15} {:<26} {:<15} {:<26} {:<10} {n}".
	            format('CONTAINER ID','IMAGE','COMMAND','CREATED','STATUS','PORTS', n='NAMES'))