# -*- coding: utf-8 -*-
import os

class FileReader:
    """
    A generic file parser capable of handling data in the same format as the RR Lyrae files.
    """
    
    def read_files(path):
        data = {}
        for i in os.listdir(path):
            dirEntryPath = os.path.join(path, i)
            if os.path.isfile(dirEntryPath):
                with open(dirEntryPath, 'r') as obsFile:
                    data[i] = obsFile.read()
        return data


    def parse_files(data, i):
        """
        Parses files in the chosen directory, grabbing time and light values and placing them in an array of tuples.
        """
        tuples = {}
        lines = data.split('/n')
        for l in lines:
            values = l.split(' ')
            obsTuple = (values[0], values[1])
            tuples.append(obsTuple)
        return tuples    
        
            
            
            
            
            
            


