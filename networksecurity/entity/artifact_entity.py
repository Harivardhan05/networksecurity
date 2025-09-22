from dataclasses import dataclass
'''
It just acts like a decorator which probably creates a variable for an empty class.
In my class I don't have any functions. I just need to have some variables defined, a class variable 

'''

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str