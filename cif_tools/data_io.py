

from cif_tools import cif_functions as cf

def load_cif(load_filename,index_dict,working_file):
    '''
    load file is the file you want to copy over into your working_file
    must have an index_dict for that working_file
    '''
    with open(load_filename, "r") as f:
        while line := f.readline():
            if line[0] == "(": #klayout stuff
                pass
            else:
                split_line = line.split(" ")
                if split_line[0] == "DS": #new subset
                    end = False
                    old_index = int(split_line[1])
                    scale_num = int(split_line[2])
                    scale_denom = int(split_line[3].removesuffix(";\n"))
                    working_file.write(line)
                    # next line
                    line = f.readline()
                    split_line = line.split(" ")
                    if split_line[0] == "9": #we have a name
                        name = split_line[1].removesuffix(";\n")
                    else: #no name     will name always be second?
                        name = "imported_from_"+load_filename[0:-3]+"index_"+str(old_index)
                    index_dict.add_new_index(name)
                    working_file.write('9 '+name+';\n')
                    while not end:
                        line = f.readline()
                        print(line)
                        if line[0:3] == "DF;":
                            end = True
                        working_file.write(line)
                elif line[0:2] == "E;":
                    pass
                else:
                    print("line not understood")
                    print(line)
                    
                
            
                    
                    
        
    
