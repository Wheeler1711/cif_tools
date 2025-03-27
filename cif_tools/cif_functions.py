import numpy as np
import matplotlib.pyplot as plt
import pkg_resources



# find the csv file where everit is
# feel free to edit excel file then save as csv to change font
stream = pkg_resources.resource_stream(__name__, 'font.csv')
my_bitmap_font = np.genfromtxt(stream,delimiter = ",",filling_values=0)


# this is class to handel asigning a new index to new shapes and subsets
# basically I like to have a string to describe everything but cif format
# wants an index so I use this class to map my string names to a nubmer i
# index which increaments with every new asignment 
class index_dictionary():
    
    def __init__(self):
        self.id = {}
        self.index_offset = 0 #allow for incrementing to start intergers >0
        self.appendix_name = '' #when nesting many similar subsets a subset name

    def add_new_index(self,name):
        if self.appendix_name != '':
            self.id[name+'_'+self.appendix_name] = self.index_offset+len(self.id)+1
            return name+'_'+self.appendix_name
        else:
            self.id[name] = self.index_offset+len(self.id)+1
            return name

    def lookup(self,name):
        if self.appendix_name != '':
            return self.id[name+'_'+self.appendix_name]
        else:
            return self.id[name]

def parse_index_input(index,name):
    if not isinstance(index, int):
        if name == '':
            print("name required is supplying an index class")
            return
        else:
            #print(index)
            name = index.add_new_index(name)
            num_index = index.id[name]
            #print("test")
            #print(num_index)
    else:
        num_index = index
    return index,num_index
    

def start_subset(f,index,scale_num = 1,scale_denom = 1,subset_name = '' ): #default scale is 1/100 of a micron
    index, num_index = parse_index_input(index,subset_name)
    f.write('DS '+str(num_index)+' '+str(scale_num)+' '+str(scale_denom)+';\n') 
    if subset_name != '':
        f.write('9 '+subset_name+';\n') # name subset

def end_subset(f):
    f.write('DF;\n') # end subset

def end_file(f):
    f.write('E;\n')

def translate(f,index,x,y):
    f.write('C'+str(index)+' T'+str(int(x))+','+str(int(y))+';\n')

def rotate(f,index,rotation):
    f.write('C'+str(index)+' R'+str(int(np.cos(rotation*np.pi/180)*2147483647))+' '+str(int(np.sin(rotation*np.pi/180)*2147483647))+';\n')
    #f.write('C'+str(index)+' R'+str(round(np.cos(rotation*np.pi/180)*1000))+' '+str(round(np.sin(rotation*np.pi/180)*1000))+';\n') #need lots of precision 32 bit unsigned integer is max? 

def translate_and_rotate(f,index,x,y,rotation):
#    f.write('C'+str(index)+' T'+str(int(x))+','+str(int(y))+
#                ' R'+str(round(np.cos(rotation*np.pi/180)*1000))+' '+str(round(np.sin(rotation*np.pi/180)*1000))+';\n')
    f.write('C'+str(index)+' T'+str(int(x))+','+str(int(y))+
                ' R'+str(round(np.cos(rotation*np.pi/180)*2147483647))+' '+str(round(np.sin(rotation*np.pi/180)*2147483647))+';\n')
    
def mirror_y(f,index):
    #print('C'+str(index)+' R'+str(int(np.cos(rotation*np.pi/180)*1000))+' '+str(int(np.sin(rotation*np.pi/180)*1000))+';\n')
    f.write('C'+str(index)+' MY'+';\n')

def mirror_x(f,index):
    #print('C'+str(index)+' R'+str(int(np.cos(rotation*np.pi/180)*1000))+' '+str(int(np.sin(rotation*np.pi/180)*1000))+';\n')
    f.write('C'+str(index)+' MX'+';\n')


def draw_hexagon(f,index,diameter,x= 0,y= 0,layer = 1,scale_num = 1,scale_denom = 1,name=''):
    index, num_index = parse_index_input(index,name)
    '''
       _____    f is the file
      /     \   index is index for cif file
     /___.___\  x,y are dot 
     \   D   /  D is the diameter
      \_____/   scale_num in the scale numerator
                scale_denom is the scale denominator
    '''
    deg = np.pi/180.
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        f.write('P '+str(diameter//2)+','+str(0)+' '
                    +str(int(np.cos(60*deg)*diameter/2))+','+str(int(np.sin(60*deg)*diameter/2))+' '
                    +str(-int(np.cos(60*deg)*diameter/2))+','+str(int(np.sin(60*deg)*diameter/2))+' '
                    +str(-diameter//2)+','+str(0)+' '
                    +str(-int(np.cos(60*deg)*diameter/2))+','+str(-int(np.sin(60*deg)*diameter/2))+' '
                    +str(int(np.cos(60*deg)*diameter/2))+','+str(-int(np.sin(60*deg)*diameter/2))
                    +';\n')
    f.write('DF;\n') # end subset

def draw_rectangle(f,index,length,width,rotation = 0,x= 0,y= 0,
                       layer = 1,scale_num = 1,scale_denom = 1,name='',
                       fillet_corners = False,which_corners = 'all',corner_radius = 10,num_of_points = 100):
    '''
        l
  NW ________ NE
    |        |
    |    *   | w   * x,y
    |________|
  SW          SE
    '''
    index, num_index = parse_index_input(index,name)

    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
                  #B length width xpos ypos [rotation] ;
        if fillet_corners:
            # just do a polynomial now
            # rotation does not work with fillet corners
            poly_str = 'P'+' '
            if which_corners == 'all':
                which_corners = ['NW','NE','SE','SW']
            if 'NW' in which_corners:
                angles = np.linspace(np.pi,np.pi/2,num_of_points)
                for i in range(0,len(angles)):
                    poly_str += str(int(corner_radius*np.cos(angles[i])-length/2+corner_radius))+','+str(int(corner_radius*np.sin(angles[i])+width/2-corner_radius))+' '
            else:
                poly_str += str(int(-length/2))+','+str(int(width/2))+' '

            if 'NE' in which_corners:
                angles = np.linspace(np.pi/2,0,num_of_points)
                for i in range(0,len(angles)):
                    poly_str += str(int(corner_radius*np.cos(angles[i])+length/2-corner_radius))+','+str(int(corner_radius*np.sin(angles[i])+width/2-corner_radius))+' '
            else:
                poly_str += str(int(+length/2))+','+str(int(width/2))+' '

            if 'SE' in which_corners:
                angles = np.linspace(4*np.pi/2,3*np.pi/2,num_of_points)
                for i in range(0,len(angles)):
                    poly_str += str(int(corner_radius*np.cos(angles[i])+length/2-corner_radius))+','+str(int(corner_radius*np.sin(angles[i])-width/2+corner_radius))+' '
            else:
                poly_str += str(int(+length/2))+','+str(int(-width/2))+' '

            if 'SW' in which_corners:
                angles = np.linspace(3*np.pi/2,2*np.pi/2,num_of_points)
                for i in range(0,len(angles)):
                    poly_str += str(int(corner_radius*np.cos(angles[i])-length/2+corner_radius))+','+str(int(corner_radius*np.sin(angles[i])-width/2+corner_radius))+' '
            else:
                poly_str += str(int(-length/2))+','+str(int(-width/2))+' '

            #print(poly_str)


            f.write(poly_str+';\n')
        else:
            if rotation == 0:
                f.write('B '+str(length)+' '+str(width)+' '+str(x)+' '+str(y)+';\n')
            else:
                f.write('B '+str(length)+' '+str(width)+' '+str(x)+' '+str(y)+' '+str(int(np.cos(rotation*np.pi/180)*1000))+' '+str(int(np.sin(rotation*np.pi/180)*1000))+';\n')

            
    f.write('DF;\n') # end subset



def draw_wire(f,index,thickness,x,y,layer = 1,scale_num = 1,scale_denom = 1,name  =''):
    index, num_index = parse_index_input(index,name)
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        wire_str = 'W'+str(thickness)+' '
        for i in range(0,len(x)):
            wire_str += str(int(x[i]))+','+str(int(y[i]))+' '

        f.write(wire_str+';\n')
    f.write('DF;\n') # end subset
    
       

def draw_wire_circle(f,index,radius,thickness,layer = 1,scale_num = 1,scale_denom = 1,name  =''):
    index, num_index = parse_index_input(index,name)
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        wire_str = 'W'+str(thickness)+' '
        angles = np.linspace(-np.pi,np.pi,100)
        for i in range(0,len(angles)):
            wire_str += str(int(radius*np.sin(angles[i])))+','+str(int(radius*np.cos(angles[i])))+' '

        f.write(wire_str+';\n')
    f.write('DF;\n') # end subset

def draw_circle(f,index,radius,layer = 1,scale_num = 1,scale_denom = 1,name  ='',num_of_points = 100):
    index, num_index = parse_index_input(index,name)
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        circ_str = 'P'+' '
        angles = np.linspace(-np.pi,np.pi,num_of_points)
        for i in range(0,len(angles)):
            circ_str += str(int(radius*np.cos(angles[i])))+','+str(int(radius*np.sin(angles[i])))+' '

        f.write(circ_str+';\n')
    f.write('DF;\n') # end subset

def draw_round_flash(f,index,radius,layer = 1,scale_num = 1,scale_denom = 1,name  =''):
    index, num_index = parse_index_input(index,name)
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        circ_str = 'R'+' ' +str(radius*2) + ' 0 0'
        f.write(circ_str+';\n')
    f.write('DF;\n') # end subset

def draw_arc(f,index,radius,width,start_angle,end_angle,layer = 1,scale_num = 1,scale_denom = 1,name  ='',num_of_points = 100):
    index, num_index = parse_index_input(index,name)
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        circ_str = 'P'+' '
        if start_angle>end_angle:
            #print("hello")
            num_of_points_1 = int(num_of_points*(360-start_angle)/(360-start_angle+end_angle))
            num_of_points_2 = num_of_points-num_of_points_1
            angles = np.hstack((np.linspace(np.pi*start_angle/180.,np.pi*359.99999/180,num_of_points_1),np.linspace(0,np.pi*end_angle/180,num_of_points_2)))
        else:
            angles = np.linspace(np.pi*start_angle/180.,np.pi*end_angle/180,num_of_points)
        for i in range(0,len(angles)):
            circ_str += str(int(radius*np.cos(angles[i])))+','+str(int(radius*np.sin(angles[i])))+' '
        for i in reversed(range(0,len(angles))):
            circ_str += str(int((radius+width)*np.cos(angles[i])))+','+str(int((radius+width)*np.sin(angles[i])))+' '

        f.write(circ_str+';\n')
    f.write('DF;\n') # end subset


def draw_polygon(f,index,x_points,y_points,layer = 1,scale_num = 1,scale_denom = 1,name  =''):
    index, num_index = parse_index_input(index,name)
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        poly_str = 'P'+' '
        for i in range(0,len(x_points)):
            poly_str += str(int(x_points[i]))+','+str(int(y_points[i]))+' '

        f.write(poly_str+';\n')
    f.write('DF;\n') # end subset

def draw_arc_spiral(f,index,radius,radius_2,width,start_angle,end_angle,layer = 1,scale_num = 1,scale_denom = 1,name  ='',num_of_points = 100):
    index, num_index = parse_index_input(index,name)
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5
        circ_str = 'P'+' '
        radii = np.linspace(radius,radius_2,num_of_points)
        if start_angle>end_angle:
            #print("hello")
            num_of_points_1 = int(num_of_points*(360-start_angle)/(360-start_angle+end_angle))
            num_of_points_2 = num_of_points-num_of_points_1
            angles = np.hstack((np.linspace(np.pi*start_angle/180.,np.pi*359.99999/180,num_of_points_1),np.linspace(0,np.pi*end_angle/180,num_of_points_2)))
        else:
            angles = np.linspace(np.pi*start_angle/180.,np.pi*end_angle/180,num_of_points)
        for i in range(0,len(angles)):
            circ_str += str(int(radii[i]*np.cos(angles[i])))+','+str(int(radii[i]*np.sin(angles[i])))+' '
        for i in reversed(range(0,len(angles))):
            circ_str += str(int((radii[i]+width)*np.cos(angles[i])))+','+str(int((radii[i]+width)*np.sin(angles[i])))+' '

        f.write(circ_str+';\n')
    f.write('DF;\n') # end subset

def draw_text(f,index,text,pixel_size = 1000,layer = 1,scale_num = 1,scale_denom = 1,name  =''):
    index, num_index = parse_index_input(index,name)
    # find new line characters
    text_lines = []
    for i in range(0,text.count('\n')+1):
        text_lines.append(text.split('\n')[i])
    f.write('DS '+str(num_index)+' ' +str(scale_num)+' '+str(scale_denom)+ ';\n')
    if name != '':
        f.write('9 ' + name + ' ;\n')
    if isinstance(layer,list): # want to be able to put object in multiple layers
        layers = layer
    else:
        layers = []
        layers.append(layer)
    for layer in layers:
        f.write('L L'+str(layer)+'D0;;\n') #layer 5

        new_line = 0*pixel_size
        for text in text_lines:
            for i in range(0,len(text)):
                char_num = ord(text[i])
                if char_num < 48: #symbols 1
                    char_num = ord(text[i])-32
                    bitmap = my_bitmap_font[24:32,char_num*6:char_num*6+6]
                    cap = 1
                elif char_num<58:#number
                    char_num = ord(text[i])-48
                    bitmap = my_bitmap_font[16:24,char_num*6:char_num*6+6]
                    cap = 1
                elif char_num<65:#symbols 2
                    char_num = ord(text[i])-58
                    bitmap = my_bitmap_font[32:40,char_num*6:char_num*6+6]
                    cap = 1
                elif char_num<91: # upper case
                    char_num = ord(text[i])-65
                    bitmap = my_bitmap_font[0:8,char_num*6:char_num*6+6]
                    cap = 1
                elif char_num<97:#symbols 3
                    char_num = ord(text[i])-91
                    bitmap = my_bitmap_font[40:48,char_num*6:char_num*6+6]
                    cap = 1
                elif char_num<123:#lower case
                    char_num = ord(text[i])-97
                    bitmap = my_bitmap_font[8:16,char_num*6:char_num*6+6]
                    cap = 0
                else: #symbols 4
                    char_num = ord(text[i])-123
                    bitmap = my_bitmap_font[48:56,char_num*6:char_num*6+6]
                    cap = 0


                #print(text[i])
                #print(bitmap)
                for j in range(0,8):
                    for k in range(0,6):
                        if bitmap[j,k] != 0:
                            f.write('B '+str(pixel_size)+' '+str(pixel_size)+' '+str(pixel_size*k+i*pixel_size*6)+' '+str(8*pixel_size-pixel_size*j+cap*pixel_size-new_line)+';\n')

            new_line = new_line+12*pixel_size

    f.write('DF;\n') # end subset
        


