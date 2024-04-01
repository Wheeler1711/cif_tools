import numpy as np
import matplotlib.pyplot as plt
#from cif_tools import cif_functions as cf
import cif_functions as cf

# n_arc and n_grids

microns = 100
nanometers = 0.1




def main(filename,
    file_write_mode ="w", #w is new file, a is append to file
    pixel_name = "meander_polekid",
    index_offset = 0,
    draw_entire_pixel = True,
    
    
    
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 4,#, #must be even
    arc_width = int(1100*nanometers),#int(800*nanometers),
    arc_width_right = int(1100*nanometers),#int(800*nanometers),
    arc_gap = int(1.1*microns),
    n_arcs = 8,#6,# default = 2 must be even
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(800*nanometers), # 0.8 um
    separation_x_pol = int(1300*nanometers),
    separation_y_pol = int(1300*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 13,#25,
    number_of_fingers_right = 30,#12,#15,
    capacitor_finger_overlap = 900*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -0*microns,
    capacitor_finger_width = 12*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 5*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 20,#20,
    number_of_coupling_fingers_right = 20,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 600*microns,
    feedline_width = 10*microns,
    pixel_size = 1400*microns,
    capacitor_layer = 4,
    short_layer = 4,
    liftoff_layer = 2,
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = -15,#-15,
    short_width = int(1000*nanometers),
    short_centers_x = np.linspace(-110,110,55)*microns,#[], # leave as [] for no shorts
    short_lengths_x = np.round(np.ones(55,dtype = int)*3*microns),
    short_centers_y = np.hstack((np.linspace(-110,-10,25),np.linspace(10,110,25,dtype = int)))*microns,
    short_lengths_y = np.round(np.ones(50,dtype = int)*3*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = None):#[], # leave as [] for no shorts):

    
    
    gap_size = separation_x_pol+between_pol_gap*2+line_width*2+(n_lines-2)*(separation_x_pol+line_width)#4*microns, # ums
    line_length = int(grid_spacing-gap_size/2)
    min_end_meander_length = 6*microns#meander_height/2+line_width
    meander_unit_cell_height = line_width*2+meander_height*2
    length_of_coupling_fingers = int(coupling_finger_overlap + coupling_capacitor_finger_end_gap)
    capacitor_width = capacitor_finger_overlap+2*capacitor_finger_end_gap+2*capacitor_rail_width
    capacitor_length = int((number_of_fingers-0.5)*capacitor_finger_width*2+capacitor_finger_start_gap*2)
    capacitor_length_right = int((number_of_fingers_right-0.5)*capacitor_finger_width_right*2+capacitor_finger_start_gap*2)

    f = open(filename, file_write_mode)

    if ic == None:
        ic = cf.index_dictionary()
        ic.index_offset = index_offset
        print("ic = None")
        
    else:
        ic.appendix_name = pixel_name
        
    print(short_centers_x)
    print(short_lengths_x)

    #####################################################################################
    #                            draw basic shapes
    #####################################################################################
    
    if not(meander_inside):
        #draw vertical grid line 
        cf.draw_rectangle(f,ic,line_width,line_length,layer = inductor_layer,scale_num = 1,name= 'vertical_line') #
        #draw horizontal grid line
        cf.draw_rectangle(f,ic,line_length,line_width,layer = inductor_layer,scale_num = 1,name= 'horizontal_line') #
        #draw vertical end cap 
        cf.draw_rectangle(f,ic,line_width*2+separation_y_pol,line_width,layer = inductor_layer,scale_num = 1,name= 'vertical_line_end_cap') #
        #draw horizontal grid line
        cf.draw_rectangle(f,ic,line_width,line_width*2+separation_x_pol,layer = inductor_layer,scale_num = 1,name= 'horizontal_line_end_cap') #

        for i in range(0,len(short_centers_x)):
            cf.draw_rectangle(f,ic,short_lengths_x[i],short_width,layer = short_layer,scale_num = 1,name= 'short_x_'+str(i)) #
        for i in range(0,len(short_centers_y)):
            cf.draw_rectangle(f,ic,short_width,short_lengths_y[i],layer = short_layer,scale_num = 1,name= 'short_y_'+str(i)) #
            


        print(line_length)
        print(min_end_meander_length)
        remainder_length_horizontal = int(grid_spacing-line_length+arc_width)

        remainder_length_vertical = int(grid_spacing-line_length-1*separation_x_pol/2-between_pol_gap-line_width+arc_width_right)
        remainder_length_vertical_2 = int(grid_spacing-line_length-1*separation_x_pol/2-between_pol_gap-line_width+arc_width_right*2+arc_gap)
        print(grid_spacing,line_length,1*separation_x_pol/2,between_pol_gap,line_width*2,arc_width_right)
        print("remainder_length_vertical",remainder_length_vertical)

        #meander_remainder
        #meander vertical
        cf.draw_rectangle(f,ic,remainder_length_horizontal,line_width,layer = inductor_layer,scale_num = 1,name= 'remainder_horizantal') #
        cf.draw_rectangle(f,ic,line_width,remainder_length_vertical,layer = inductor_layer,scale_num = 1,name= 'remainder_vertical') #
        cf.draw_rectangle(f,ic,line_width,remainder_length_vertical_2,layer = inductor_layer,scale_num = 1,name= 'remainder_vertical_2') #
    
    horizontal_connect_meander_length = 1*meander_unit_cell_height

    
    #####################################################################################
    #                           inside arcs
    #####################################################################################
    # arcs are kind of complicated the idea is to offset the radius of the arc so that it
    # will mate pefectly (squarely and at right radius) with the inductor. This results
    # in an imperfect mate on the other side might use a spiral arc to make match perfect
    # on both sides in the future

    angle_to_cut_short_inside_1 = 180/np.pi*np.arcsin((separation_x_pol/2+(n_lines-2)/2*(separation_x_pol+line_width))/np.sqrt(grid_spacing**2+(separation_x_pol/2+(n_lines-2)/2*(separation_x_pol+line_width))**2))
    angle_to_cut_short_inside_2 = 180/np.pi*np.arcsin((3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt(grid_spacing**2+(3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))**2))
    angle_to_cut_short_inside_3 = 180/np.pi*np.arcsin((separation_y_pol/2+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt(grid_spacing**2+(separation_y_pol/2+(n_lines-2)/2*(separation_y_pol+line_width))**2))
    #draw arc horizontal pol bottom
    cf.draw_arc(f,ic,grid_spacing,arc_width,180+angle_to_cut_short_inside_1, # near x_pol
                    270-angle_to_cut_short_inside_2,layer = arc_layer,scale_num = 1, # near y_pol
                    name= 'arc_horizontal_bottom')
    #draw arc horizontal pol top
    cf.draw_arc(f,ic,grid_spacing,arc_width,90+angle_to_cut_short_inside_2,180-angle_to_cut_short_inside_1,
                    layer = arc_layer,scale_num = 1,name= 'arc_horizontal_top')  #
    #draw arc vertical pol bottom
    cf.draw_arc(f,ic,grid_spacing,arc_width_right,270+angle_to_cut_short_inside_3,90-angle_to_cut_short_inside_3,
                    layer = arc_layer,scale_num = 1,name= 'arc_vertical_bottom')  #

    #####################################################################################
    #                           outside arcs
    #####################################################################################
    angle_to_cut_short_outside_1 = 180/np.pi*np.arcsin((arc_gap/2)/np.sqrt((grid_spacing+arc_gap+arc_width)**2+(arc_gap/2)**2))
    angle_to_cut_short_outside_2 = 180/np.pi*np.arcsin((3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt((grid_spacing+arc_gap+arc_width)**2+(3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))**2))
    angle_to_cut_short_outside_3 = 180/np.pi*np.arcsin((separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt((grid_spacing+arc_gap+arc_width)**2+(separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))**2))
    print("arc_width",arc_width)
    print("arc_width_right",arc_width_right)

    #draw outside arc horizontal pol bottom
    cf.draw_arc(f,ic,grid_spacing+arc_width+arc_gap,arc_width*1,180+angle_to_cut_short_outside_1,
                    270+pol_angle-angle_to_cut_short_outside_2,layer = arc_layer,scale_num = 1, #near y_pol
                    scale_denom = 1,name= 'arc_outer_horizontal_bottom',num_of_points = 100)
    #draw outside arc horizontal pol top
    cf.draw_arc(f,ic,grid_spacing+arc_width+arc_gap,arc_width,90+pol_angle+angle_to_cut_short_outside_2,
                    180-angle_to_cut_short_outside_1,layer = arc_layer,
                    scale_num = 1,name= 'arc_outer_horizontal_top')

    if n_arcs>2:
        for i in range(2,n_arcs):
                cf.draw_arc(f,ic,grid_spacing+arc_width*i+arc_gap*i,arc_width*1,180+angle_to_cut_short_outside_1,
                    270+pol_angle-angle_to_cut_short_outside_2,layer = arc_layer,scale_num = 1, #near y_pol
                    scale_denom = 1,name= 'arc_outer_horizontal_bottom_'+str(i),num_of_points = 100)
        #draw outside arc horizontal pol top
                cf.draw_arc(f,ic,grid_spacing+arc_width*i+arc_gap*i,arc_width,90+pol_angle+angle_to_cut_short_outside_2,
                    180-angle_to_cut_short_outside_1,layer = arc_layer,
                    scale_num = 1,name= 'arc_outer_horizontal_top_'+str(i))


    
    #draw outside arc vertical pol bottom    
    cf.draw_arc(f,ic,grid_spacing+arc_width_right+arc_gap,arc_width_right,270+pol_angle-angle_to_cut_short_outside_3,
                    360-angle_to_cut_short_outside_1,layer = arc_layer,scale_num = 1,name= 'arc_outer_vertical_bottom')
    #draw outside arc vertical pol top
    cf.draw_arc(f,ic,grid_spacing+arc_width_right+arc_gap,arc_width_right,0+angle_to_cut_short_outside_1,
                    90+pol_angle+angle_to_cut_short_outside_3,layer = arc_layer,scale_num = 1,name= 'arc_outer_vertical_top')

    if n_arcs>2:
        for i in range(2,n_arcs):
    
            #draw outside arc vertical pol top
            cf.draw_arc(f,ic,grid_spacing+arc_width_right*i+arc_gap*i,arc_width_right,0+angle_to_cut_short_outside_1,
                    90+pol_angle+angle_to_cut_short_outside_3,layer = arc_layer,scale_num = 1,name= 'arc_outer_vertical_top_'+str(i))

            #draw outside arc vertical pol bottom    
            cf.draw_arc(f,ic,grid_spacing+arc_width_right*i+arc_gap*i,arc_width_right,270+pol_angle-angle_to_cut_short_outside_3,
                    360-angle_to_cut_short_outside_1,layer = arc_layer,scale_num = 1,name= 'arc_outer_vertical_bottom_'+str(i))


    #####################################################################################
    #                           arc connectors
    #####################################################################################

    cf.draw_rectangle(f,ic,arc_width,arc_width*2+arc_gap,layer = arc_layer,scale_num = 1,name= 'vertical_arc_connector') #
 
    cf.draw_rectangle(f,ic,arc_width*2+absorber_extension_length,arc_width,layer = arc_layer,scale_num = 1,name= 'horizontal_arc_connector')
    cf.draw_rectangle(f,ic,arc_width_right*2+absorber_extension_length,arc_width_right,layer = arc_layer,scale_num = 1,name= 'horizontal_arc_connector_right')

    cf.draw_rectangle(f,ic,arc_width_right*2+arc_gap,arc_width_right,layer = arc_layer,scale_num = 1,name= 'double_arc_connector')
    cf.draw_rectangle(f,ic,arc_width_right,arc_width_right*2+arc_gap,layer = arc_layer,scale_num = 1,name= 'double_arc_connector_vertical')

    #####################################################################################
    #                           liftoff aluminum
    #####################################################################################
    
    #liftoff aluminum
    liftoff_length = capacitor_rail_width*2+liftoff_gap_size
    cf.draw_rectangle(f,ic,capacitor_rail_width,liftoff_length,layer = liftoff_layer,scale_num = 1,name= 'liftoff_aluminum')

    #liftoff pad
    cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_rail_width,layer = arc_layer,scale_num = 1,name= 'liftoff_aluminum_pad')



    #####################################################################################
    #                            draw capacitor shapes
    #####################################################################################

    # draw capacitor rail
    #cf.draw_rectangle(f,ic,capacitor_length+capacitor_rail_width-int(30*microns),capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'capacitor_rail') #
    #cf.draw_rectangle(f,ic,capacitor_length_right+capacitor_rail_width-int(30*microns),capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'capacitor_rail_right') #
    cf.draw_rectangle(f,ic,capacitor_length+capacitor_rail_width,capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'capacitor_rail') #
    cf.draw_rectangle(f,ic,capacitor_length_right+capacitor_rail_width,capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'capacitor_rail_right') #
    # capacitor end connector
    cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_finger_overlap+capacitor_finger_end_gap*2+capacitor_rail_width*2,layer = capacitor_layer,scale_num = 1,name= 'capacitor_end_connector') #
    
    # draw capacitor connector
    capacitor_connector_length = int(capacitor_finger_overlap/2+capacitor_finger_end_gap-arc_gap/2-liftoff_gap_size)
    cf.draw_rectangle(f,ic,arc_width,capacitor_connector_length+capacitor_offset_y,layer = arc_layer,scale_num = 1,name= 'capacitor_connector_top') #
    cf.draw_rectangle(f,ic,arc_width,capacitor_connector_length-capacitor_offset_y,layer = arc_layer,scale_num = 1,name= 'capacitor_connector_bottom') #
    cf.draw_rectangle(f,ic,arc_width_right,capacitor_connector_length+capacitor_offset_y,layer = arc_layer,scale_num = 1,name= 'capacitor_connector_top_right') #
    cf.draw_rectangle(f,ic,arc_width_right,capacitor_connector_length-capacitor_offset_y,layer = arc_layer,scale_num = 1,name= 'capacitor_connector_bottom_right') #
    #capacitor_finger
    capacitor_finger_length = int(capacitor_finger_overlap+capacitor_finger_end_gap)
    cf.draw_rectangle(f,ic,capacitor_finger_width,capacitor_finger_length,layer = capacitor_layer,scale_num = 1,name= 'capacitor_finger') #
    #capacitor_finger_right
    capacitor_finger_length_right = int(capacitor_finger_overlap+capacitor_finger_end_gap)
    cf.draw_rectangle(f,ic,capacitor_finger_width_right,capacitor_finger_length_right,layer = capacitor_layer,scale_num = 1,name= 'capacitor_finger_right') #
    #coupling capacitor_finger
    cf.draw_rectangle(f,ic,coupling_capacitor_finger_width,length_of_coupling_fingers,layer = capacitor_layer,scale_num = 1,name= 'coupling_capacitor_finger') #
    #coupling capacitor_finger
    cf.draw_rectangle(f,ic,coupling_capacitor_finger_width_right,length_of_coupling_fingers,layer = capacitor_layer,scale_num = 1,name= 'coupling_capacitor_finger_right') #
    #coupling connector
    coupler_connector_width = int(number_of_coupling_fingers*coupling_capacitor_finger_width*2-coupling_capacitor_finger_width)
    cf.draw_rectangle(f,ic,coupler_connector_width,coupling_capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'coupling_capacitor_connector') #
    #coupling connector right
    coupler_connector_width_right = int(number_of_coupling_fingers_right*coupling_capacitor_finger_width_right*2-coupling_capacitor_finger_width_right)
    cf.draw_rectangle(f,ic,coupler_connector_width_right,coupling_capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'coupling_capacitor_connector_right') #
    # draw capacitor connector_horizontal
    coupling_connector_length_vertical = int((feedline_y_location-feedline_width/2)-(capacitor_finger_overlap/2+capacitor_finger_end_gap+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+capacitor_rail_width*1+coupling_capacitor_rail_width*2+capacitor_to_coupling_capacitor_gap+capacitor_offset_y))
    print(coupling_connector_length_vertical)
    cf.draw_rectangle(f,ic,capacitor_rail_width,coupling_connector_length_vertical,layer = capacitor_layer,scale_num = 1,name= 'coupling_capacitor_connector_vertical')
    # draw leg to coupling capacitor
    cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_to_coupling_capacitor_gap,layer = capacitor_layer,scale_num = 1,name= 'capacitor_to_coupling_capacitor_connector') #

    #####################################################################################
    #                            feedline shapes
    #####################################################################################
    cf.draw_rectangle(f,ic,pixel_size+4*microns,feedline_width,layer = capacitor_layer,scale_num = 1,name= 'feedline') #


    #####################################################################################
    #                            border
    #####################################################################################

    cf.draw_rectangle(f,ic,pixel_size,int(pixel_size*np.sqrt(3)/2),layer = 3,scale_num = 1,name= 'pixel_size') #
    cf.draw_arc(f,ic,int(220+70)*microns,100*microns,0,360,layer = 10,scale_num = 1,name= 'choke_radius') #
    cf.draw_arc(f,ic,int(225/2*microns*1.1),220*microns-int(225/2*microns*1.1),0,360,layer = 10,scale_num = 1,name= 'choke_inner_radius') #
    cf.draw_circle(f,ic,int(112.5*microns),layer = 11,scale_num = 1,name= 'guide_radius')
    cf.draw_rectangle(f,ic,int(grid_spacing*2+arc_width*2*2+arc_gap*2*2+capacitor_rail_width*2+np.min((capacitor_finger_width,capacitor_finger_width_right))),
                          int(arc_gap+capacitor_connector_length*2+liftoff_gap_size),layer = 1,scale_num = 1,name= 'inductor_border_etch')
    cf.draw_rectangle(f,ic,int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length),
                          int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length),layer = 1,scale_num = 1,name= 'inductor_border_etch_2')
    #cf.draw_polygon(f,ic,wip_x,wip_y,layer = 12,name = 'WIP1')
    #cf.draw_polygon(f,ic,wip_foot_x,wip_foot_y,layer = 13,name = 'WIP1_foot')
    #cf.draw_polygon(f,ic,wip_foot_protect_x,wip_foot_protect_y,layer = 13,name = 'WIP1_foot_protect')

    #####################################################################################
    #                            deep etch trench
    #####################################################################################

    cf.draw_rectangle(f,ic,(grid_spacing+arc_width*2+arc_gap+absorber_extension_length)*2,(grid_spacing+arc_width*2+arc_gap+absorber_extension_length)*2,
                          layer = 6,scale_num = 1,name= 'inductor_trench') #
    capacitor_trench_x = capacitor_length+capacitor_rail_width
    capacitor_trench_x_right = capacitor_length_right+capacitor_rail_width
    capacitor_trench_y = capacitor_width+100*microns+length_of_coupling_fingers+capacitor_rail_width*2+\
      capacitor_to_coupling_capacitor_gap+coupling_capacitor_finger_end_gap
    cf.draw_rectangle(f,ic,capacitor_trench_x,capacitor_trench_y,layer = 6,scale_num = 1,name= 'capacitor_trench') #
    cf.draw_rectangle(f,ic,capacitor_trench_x_right,capacitor_trench_y,layer = 6,scale_num = 1,name= 'capacitor_trench_right') #


    if meander_inside:

        #####################################################################################
        #                            draw meander shapes
        #####################################################################################
        
        #meander horizontal
        cf.draw_rectangle(f,ic,meander_length,line_width,layer = inductor_layer,scale_num = 1,name= 'meander_horizontal') #
        #meander vertical
        cf.draw_rectangle(f,ic,line_width,meander_height,layer = inductor_layer,scale_num = 1,name= 'meander_vertical') #
        #meander vertical_2
        cf.draw_rectangle(f,ic,line_width,int(np.ceil(meander_height/2)+20*nanometers),layer = inductor_layer,scale_num = 1,name= 'meander_vertical_2') #


        print(line_length)
        print(min_end_meander_length)
        number_of_meanders = int(np.floor((line_length-min_end_meander_length*2)/meander_unit_cell_height))
        remainder_length_horizontal = int((grid_spacing-number_of_meanders*meander_unit_cell_height-horizontal_connect_meander_length/2.+arc_width_right))
        print("number of meanders:",number_of_meanders)
        print("remainder length horizontal:",remainder_length_horizontal,"\n")
        remainder_length_vertical = int((grid_spacing-number_of_meanders*meander_unit_cell_height-1*separation_x_pol/2-between_pol_gap-line_width*2-meander_length-3*meander_height/2+arc_width_right))
        remainder_length_vertical_2 = int((grid_spacing-number_of_meanders*meander_unit_cell_height-1*separation_x_pol/2-between_pol_gap-line_width*2-meander_length-3*meander_height/2+arc_width_right*2+arc_gap))

        #meander_remainder
        #meander vertical
        cf.draw_rectangle(f,ic,remainder_length_horizontal,line_width,layer = inductor_layer,scale_num = 1,name= 'remainder_horizantal') #
        cf.draw_rectangle(f,ic,line_width,remainder_length_vertical,layer = inductor_layer,scale_num = 1,name= 'remainder_vertical') #
        cf.draw_rectangle(f,ic,line_width,remainder_length_vertical_2,layer = inductor_layer,scale_num = 1,name= 'remainder_vertical_2') #

        #####################################################################################
        #                            draw unit meander 
        #####################################################################################

        # unit meander
        cf.start_subset(f,ic,subset_name = 'unit_meander')
        cf.translate(f,ic.lookup('meander_horizontal'),0,-meander_height/2-line_width/2)#
        cf.translate(f,ic.lookup('meander_vertical'),meander_length/2-line_width/2,0)#
        cf.translate(f,ic.lookup('meander_horizontal'),0,meander_height/2+line_width/2)#
        cf.translate(f,ic.lookup('meander_vertical_2'),-meander_length/2+line_width/2,+3/4*meander_height+line_width)#
        cf.translate(f,ic.lookup('meander_vertical_2'),-meander_length/2+line_width/2,-3/4*meander_height-line_width)#
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'unit_meander_mirror')
        cf.mirror_x(f,ic.lookup('unit_meander'))
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'unit_meander_both_x_pol')
        cf.translate(f,ic.lookup('unit_meander'),-(-separation_x_pol/2-meander_length/2),0)
        cf.translate(f,ic.lookup('unit_meander_mirror'),(-separation_x_pol/2-meander_length/2),0)
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'unit_meander_both_y_pol')
        cf.translate(f,ic.lookup('unit_meander'),-(-separation_y_pol/2-meander_length/2),0)
        cf.translate(f,ic.lookup('unit_meander_mirror'),(-separation_y_pol/2-meander_length/2),0)
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'unit_meander_rotated_90')
        cf.rotate(f,ic.lookup('unit_meander_both_x_pol'),90)
        cf.end_subset(f)



    #####################################################################################
    #                            draw meander 
    #####################################################################################

        cf.start_subset(f,ic,subset_name = 'meandered_line')

        for i in range(0,number_of_meanders):
            cf.translate(f,ic.lookup('unit_meander'),0,-number_of_meanders/2.*meander_unit_cell_height+meander_unit_cell_height/2+i*meander_unit_cell_height)#bottom

        cf.end_subset(f)

        # horizontal grid meander by rotating
        cf.start_subset(f,ic,subset_name = 'meandered_line_horizontal')
        cf.rotate(f,ic.lookup('meandered_line'),90)
        cf.end_subset(f)

        # right side of vertical by mirroring
        cf.start_subset(f,ic,subset_name = 'meandered_line_mirror')
        cf.mirror_x(f,ic.lookup('meandered_line'))
        cf.end_subset(f)


        # bottom side of horizontal by mirrororing
        cf.start_subset(f,ic,subset_name = 'meandered_line_horizontal_mirror')
        cf.mirror_y(f,ic.lookup('meandered_line_horizontal'))
        cf.end_subset(f)



        #####################################################################################
        #                       end meander
        #####################################################################################

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_x_pol')
        cf.translate(f,ic.lookup('meander_horizontal'),0,-meander_height/2-line_width/2)#
        cf.translate(f,ic.lookup('meander_vertical'),meander_length/2-line_width/2,0)#
        cf.translate(f,ic.lookup('meander_horizontal'),0,meander_height/2+line_width/2)#
        cf.translate(f,ic.lookup('meander_horizontal'),-separation_x_pol/2,meander_height/2+line_width/2)#
        cf.translate(f,ic.lookup('meander_vertical_2'),-meander_length/2+line_width/2,-3/4*meander_height-line_width)#
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_y_pol')
        cf.translate(f,ic.lookup('meander_horizontal'),0,-meander_height/2-line_width/2)#
        cf.translate(f,ic.lookup('meander_vertical'),meander_length/2-line_width/2,0)#
        cf.translate(f,ic.lookup('meander_horizontal'),0,meander_height/2+line_width/2)#
        cf.translate(f,ic.lookup('meander_horizontal'),-separation_y_pol/2,meander_height/2+line_width/2)#
        cf.translate(f,ic.lookup('meander_vertical_2'),-meander_length/2+line_width/2,-3/4*meander_height-line_width)#
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_mirror')
        cf.mirror_x(f,ic.lookup('meander_end_cap_x_pol'))
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_mirror_y_pol')
        cf.mirror_x(f,ic.lookup('meander_end_cap_y_pol'))
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_both_x_pol')
        cf.translate(f,ic.lookup('meander_end_cap_x_pol'),+separation_x_pol/2+meander_length/2,0)
        cf.translate(f,ic.lookup('meander_end_cap_mirror'),-separation_x_pol/2-meander_length/2,0)
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_both_y_pol')
        cf.translate(f,ic.lookup('meander_end_cap_x_pol'),+separation_y_pol/2+meander_length/2,0)
        cf.translate(f,ic.lookup('meander_end_cap_mirror'),-separation_y_pol/2-meander_length/2,0)
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_rotated_180')
        cf.rotate(f,ic.lookup('meander_end_cap_both_y_pol'),180)
        cf.end_subset(f)

        cf.start_subset(f,ic,subset_name = 'meander_end_cap_rotated_270')
        cf.rotate(f,ic.lookup('meander_end_cap_both_x_pol'),270)
        cf.end_subset(f)

    


    #####################################################################################
    #                            place shapes for pixel 
    #####################################################################################



    # put intductor and inner arcs in a subset so we can rotate the whole subset
    cf.start_subset(f,ic,subset_name = 'inductors')

    if meander_inside:
        #horizontal lines
        if draw_left:
            cf.translate(f,ic.lookup('meandered_line_horizontal'),
                             -meander_unit_cell_height*number_of_meanders/2-horizontal_connect_meander_length/2,
                             separation_x_pol/2+meander_length/2)#bottom
            cf.translate(f,ic.lookup('meandered_line_horizontal_mirror'),
                             -meander_unit_cell_height*number_of_meanders/2-horizontal_connect_meander_length/2,
                             -(separation_x_pol/2+meander_length/2))#bottom
            cf.translate(f,ic.lookup('meandered_line_horizontal'),
                             meander_unit_cell_height*number_of_meanders/2+horizontal_connect_meander_length/2,
                             (separation_x_pol/2+meander_length/2))#top
            cf.translate(f,ic.lookup('meandered_line_horizontal_mirror'),
                             meander_unit_cell_height*number_of_meanders/2+horizontal_connect_meander_length/2,
                             -(separation_x_pol/2+meander_length/2))#top

        #vertical lines
        if draw_right:
            cf.translate(f,ic.lookup('meandered_line'),(separation_y_pol/2+meander_length/2),
                             -meander_unit_cell_height*number_of_meanders/2-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2))#left
            cf.translate(f,ic.lookup('meandered_line_mirror'),-(separation_y_pol/2+meander_length/2),
                             -meander_unit_cell_height*number_of_meanders/2-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2))#left
            cf.translate(f,ic.lookup('meandered_line'),(separation_y_pol/2+meander_length/2),
                             meander_unit_cell_height*number_of_meanders/2+1*separation_x_pol/2+between_pol_gap+meander_length+(meander_unit_cell_height-meander_height/2))#right
            cf.translate(f,ic.lookup('meandered_line_mirror'),-(separation_y_pol/2+meander_length/2),
                             meander_unit_cell_height*number_of_meanders/2+1*separation_x_pol/2+between_pol_gap+meander_length+(meander_unit_cell_height-meander_height/2))#right

        #middle connectors
        if draw_left:
            cf.translate(f,ic.lookup('unit_meander_rotated_90'),0,0)
            #cf.translate(f,ic.lookup('unit_meander_rotated_90'),meander_unit_cell_height,0)
            #cf.translate(f,ic.lookup('unit_meander_rotated_90'),-meander_unit_cell_height,0)

        #end caps
        if draw_right:
            cf.translate(f,ic.lookup('meander_end_cap_rotated_180'),0,
                             +1*separation_x_pol/2+between_pol_gap+meander_length+(meander_unit_cell_height-meander_height)/2)#bottom
            cf.translate(f,ic.lookup('meander_end_cap_both_y_pol'),0,
                             -1*separation_x_pol/2-between_pol_gap-meander_length-+(meander_unit_cell_height-meander_height)/2)#bottom
        if draw_left:
            cf.translate(f,ic.lookup('meander_end_cap_rotated_270'),
                             meander_unit_cell_height*number_of_meanders+horizontal_connect_meander_length/2+meander_unit_cell_height/2,0)#bottom

        if draw_left:
            cf.translate(f,ic.lookup('remainder_horizantal'),
                             -meander_unit_cell_height*number_of_meanders-horizontal_connect_meander_length/2-remainder_length_horizontal/2,
                             -(separation_x_pol/2+line_width/2))#bottom
            cf.translate(f,ic.lookup('remainder_horizantal'),
                             -meander_unit_cell_height*number_of_meanders-horizontal_connect_meander_length/2-remainder_length_horizontal/2,
                             (separation_x_pol/2+line_width/2))#bottom

        if draw_right:
            cf.translate(f,ic.lookup('remainder_vertical'),(separation_y_pol/2+line_width/2),
                             -meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical/2)#bottom
            cf.translate(f,ic.lookup('remainder_vertical'),(separation_y_pol/2+line_width/2),
                             -(-meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical/2))#top
            cf.translate(f,ic.lookup('remainder_vertical_2'),-(separation_y_pol/2+line_width/2),
                             -meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical_2/2)#bottom
            cf.translate(f,ic.lookup('remainder_vertical_2'),-(separation_y_pol/2+line_width/2),
                             -(-meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical_2/2))#top

    else:#no meandering

        if draw_left:
            for i in range(0,n_lines):
                # if i == (n_lines/2)-1 or i == (n_lines/2):
                #     cf.translate(f,ic.lookup('horizontal_line'),-line_length/2,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#
                #     cf.translate(f,ic.lookup('horizontal_line'),line_length/2,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#
                #     print(i)
                # else:
                #     cf.translate(f,ic.lookup('horizontal_line'),-1*separation_x_pol/2-line_width-between_pol_gap-line_length/2+(2-n_lines)*(separation_x_pol+line_width)/2,
                #                      (separation_x_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_x_pol))#
                #     cf.translate(f,ic.lookup('horizontal_line'),-(-1*separation_x_pol/2-line_width-between_pol_gap-line_length/2+(-2-n_lines)*(separation_x_pol+line_width)/2+3*between_pol_gap),
                #                      (separation_x_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_x_pol))
                #     #cf.translate(f,ic.lookup('horizontal_line'),-line_length/4,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#
                #     #cf.translate(f,ic.lookup('horizontal_line'),-(line_width/4)*(n_lines/2),separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#line_length/2,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#
                    
                cf.translate(f,ic.lookup('horizontal_line'),-line_length/2,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#
                cf.translate(f,ic.lookup('horizontal_line'),line_length/2,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#
                #print(i - n_lines/2)
                
                if aluminum_left == True:
                    for k in range(0,len(short_centers_x)):
                        cf.translate(f,ic.lookup('short_x_'+str(k)),short_centers_x[k],
                                     separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#

            
                cf.translate(f,ic.lookup('remainder_horizantal'),-line_length-remainder_length_horizontal/2,
                             (separation_x_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_x_pol))#bottom


                if np.mod(i,2) == 0:
                    cf.translate(f,ic.lookup('horizontal_line_end_cap'),line_length-line_width/2,
                                     (-separation_x_pol/2-line_width) + (-separation_x_pol-line_width)*(n_lines-2)/2\
                                     +(separation_x_pol+line_width*2)/2+ (separation_x_pol+line_width)*i )#
                if n_lines>2:
                    if np.mod(i,2) == 1 and i != n_lines -1:
                        cf.translate(f,ic.lookup('horizontal_line_end_cap'),-(line_length-line_width/2)-remainder_length_horizontal,
                                     (-separation_x_pol/2-line_width) + (-separation_x_pol-line_width)*(n_lines-2)/2\
                                     +(separation_x_pol+line_width*2)/2+ (separation_x_pol+line_width)*i )#
                        
                    

        #veritcal lines
        if draw_right:
            for i in range(0,n_lines):
                cf.translate(f,ic.lookup('vertical_line'),(separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol),
                                 -1*separation_x_pol/2-line_width-between_pol_gap-line_length/2+(2-n_lines)*(separation_x_pol+line_width)/2)#left
                cf.translate(f,ic.lookup('vertical_line'),(separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol),
                                 -(-1*separation_x_pol/2-line_width-between_pol_gap-line_length/2+(2-n_lines)*(separation_x_pol+line_width)/2))

                if aluminum_right == True:
                    for k in range(0,len(short_centers_y)):
                        cf.translate(f,ic.lookup('short_y_'+str(k)),(separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol),
                                 short_centers_y[k])#left
                    #cf.translate(f,ic.lookup('vertical_line'),(separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol),
                    #             -(-1*separation_x_pol/2-line_width-between_pol_gap-line_length/2+(2-n_lines)*(separation_x_pol+line_width)/2))


                cf.translate(f,ic.lookup('remainder_vertical'),(separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol),
                                -line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical/2)#bottom
                cf.translate(f,ic.lookup('remainder_vertical'),(separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol),
                             -(-line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical/2))#top

                if np.mod(i,2) == 0:

                    cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2\
                                     +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                     separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2)#
                    cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2\
                                     +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                     -(separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2))#

                if n_lines>2:
                    if np.mod(i,2) == 1 and i != n_lines -1:
                        cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2\
                                     +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                     separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2+line_length)#
                        cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2\
                                     +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                     -(separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2+line_length))#



                             
            cf.translate(f,ic.lookup('remainder_vertical_2'),-(separation_y_pol/2+line_width/2)+(2-n_lines)/2*(separation_y_pol+line_width),
                             -line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical_2/2)#bottom
            cf.translate(f,ic.lookup('remainder_vertical_2'),-(separation_y_pol/2+line_width/2)+(2-n_lines)/2*(separation_y_pol+line_width),
                             -(-line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical_2/2))#top

            

        


        for i in range(1,n_arcs//2):
            
                cf.translate(f,ic.lookup('double_arc_connector_vertical'),
                         -(separation_y_pol/2+line_width/2)-(n_lines-2)/2*(separation_y_pol+line_width),
                         (-grid_spacing-arc_width_right*i*2-arc_gap*i*2-(arc_width_right*2+arc_gap)/2))#bottom
                cf.translate(f,ic.lookup('double_arc_connector_vertical'),
                         -(separation_y_pol/2+line_width/2)-(n_lines-2)/2*(separation_y_pol+line_width),
                         -(-grid_spacing-arc_width_right*i*2-arc_gap*i*2-(arc_width_right*2+arc_gap)/2))#top

    #arc connectors
    if draw_left:
        #h^2 = x^2+y^2
        #y^2 = h^2-x^2
        for i in range(1,n_arcs,2):
            # there are some non idealities to this when n_lines/ n_arcs get really big
            # probably need to be drawn at 0 in x then +/- ~grid_spacing in y and then rotated
            cf.translate(f,ic.lookup('vertical_arc_connector'),-3*separation_y_pol/2-line_width-arc_width/2-(n_lines-2)/2*(separation_y_pol+line_width),
                         np.sqrt((grid_spacing+arc_width*i+arc_gap/2+arc_gap*(i-1))**2-(-(n_lines+1)*separation_x_pol/2-line_width-arc_width/2)**2))#
        
            cf.translate(f,ic.lookup('vertical_arc_connector'),-3*separation_y_pol/2-line_width-arc_width/2-(n_lines-2)/2*(separation_y_pol+line_width),
                         -(np.sqrt((grid_spacing+arc_width*i+arc_gap/2+arc_gap*(i-1))**2-(-(n_lines+1)*separation_x_pol/2-line_width-arc_width/2)**2)))#

        # arcs
        #horizontal pol inside
        cf.translate(f,ic.lookup('arc_horizontal_bottom'),0,0)#bottom
        cf.translate(f,ic.lookup('arc_horizontal_top'),0,0)#top

    if draw_right:
        #veritcal pol inside
        cf.translate(f,ic.lookup('arc_vertical_bottom'),0,0)#both

    cf.end_subset(f)

    if ic.appendix_name != '':
        ic.appendix_name = '' #dont want pixel name to have appendix
        cf.start_subset(f,ic,subset_name = pixel_name)
        ic.appendix_name = pixel_name #dont want pixel name to have appendix
    else:
        cf.start_subset(f,ic,subset_name = pixel_name)

    cf.translate(f,ic.lookup('pixel_size'),0,0)
    #cf.translate(f,ic.lookup('WIP1'),0,0)
    #cf.translate(f,ic.lookup('WIP1_foot'),0,0)
    #cf.translate(f,ic.lookup('WIP1_foot_protect'),0,0)
    
    if pol_angle == 0:
        cf.translate(f,ic.lookup('inductors'),0,0)
    else:
        cf.rotate(f,ic.lookup('inductors'),pol_angle)


    
    # outer arcs
    if draw_left:
        cf.translate(f,ic.lookup('arc_outer_horizontal_bottom'),0,0)#bottom
        cf.translate(f,ic.lookup('arc_outer_horizontal_top'),0,0)#top
        if n_arcs >2:
            for i in range(2,n_arcs):
                cf.translate(f,ic.lookup('arc_outer_horizontal_bottom_'+str(i)),0,0)#bottom
                cf.translate(f,ic.lookup('arc_outer_horizontal_top_'+str(i)),0,0)#top

    if draw_right:
        #vertical pol outside
        cf.translate(f,ic.lookup('arc_outer_vertical_bottom'),0,0)#top
        cf.translate(f,ic.lookup('arc_outer_vertical_top'),0,0)#top
        if n_arcs >2:
            for i in range(2,n_arcs):
                cf.translate(f,ic.lookup('arc_outer_vertical_bottom_'+str(i)),0,0)#top
                cf.translate(f,ic.lookup('arc_outer_vertical_top_'+str(i)),0,0)#top

        

  
    # bottom left
    if draw_left:
        for i in range(1,n_arcs,2):
            cf.translate(f,ic.lookup('double_arc_connector'),
                             (-grid_spacing-arc_width_right*i-arc_gap*i-(arc_width_right*2+arc_gap)/2),
                             arc_gap/2+arc_width_right/2)#left
            cf.translate(f,ic.lookup('double_arc_connector'),
                             (-grid_spacing-arc_width_right*i-arc_gap*i-(arc_width_right*2+arc_gap)/2),
                             -(arc_gap/2+arc_width_right/2))#l

        
        cf.translate(f,ic.lookup('horizontal_arc_connector'),
                         -grid_spacing-arc_width-arc_gap-(arc_width*2+absorber_extension_length)/2+(2-n_arcs)*(arc_width+arc_gap),
                         arc_gap/2+arc_width/2)#left
        #top left
        cf.translate(f,ic.lookup('horizontal_arc_connector'),
                         -grid_spacing-arc_width-arc_gap-(arc_width*2+absorber_extension_length)/2+(2-n_arcs)*(arc_width+arc_gap),
                         -(arc_gap/2+arc_width/2))#left
    #right side
    if draw_right:
        for i in range(1,n_arcs,2):
            cf.translate(f,ic.lookup('double_arc_connector'),
                             -(-grid_spacing-arc_width_right*i-arc_gap*i-(arc_width_right*2+arc_gap)/2),
                             arc_gap/2+arc_width_right/2)#left
            cf.translate(f,ic.lookup('double_arc_connector'),
                             -(-grid_spacing-arc_width_right*i-arc_gap*i-(arc_width_right*2+arc_gap)/2),
                             -(arc_gap/2+arc_width_right/2))#l
                             
        cf.translate(f,ic.lookup('horizontal_arc_connector_right'),
                         -(-grid_spacing-arc_width-arc_gap-(arc_width*2+absorber_extension_length)/2+(2-n_arcs)*(arc_width+arc_gap)),
                         arc_gap/2+arc_width/2)#left
        #top  
        cf.translate(f,ic.lookup('horizontal_arc_connector_right'),
                         -(-grid_spacing-arc_width-arc_gap-(arc_width*2+absorber_extension_length)/2+(2-n_arcs)*(arc_width+arc_gap)),
                         -(arc_gap/2+arc_width/2))#left
    
    
    #inductor boarder etch
    #cf.translate(f,ic.lookup('inductor_border_etch'),0,0)#top left


    #####################################################################################
    #                            capacitor
    #####################################################################################
    if draw_entire_pixel:       
        if draw_left:
            cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('capacitor_end_connector'),-grid_spacing-capacitor_length-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                            +capacitor_offset_y)
            
        # right side
        if draw_right:
            cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('capacitor_end_connector'),-(-grid_spacing-capacitor_length_right-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                            +capacitor_offset_y)
            
            
            
        # if draw_left:
        #     cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
        #                      -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
        #     cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
        #                      +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
        #     cf.translate(f,ic.lookup('capacitor_end_connector'),-grid_spacing-capacitor_length-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
        #                     +capacitor_offset_y)
            
        # # right side
        # if draw_right:
        #     cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
        #                      -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
        #     cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
        #                      +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
        #     cf.translate(f,ic.lookup('capacitor_end_connector'),-(-grid_spacing-capacitor_length_right-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
        #                     +capacitor_offset_y)
            
            
        if draw_left:
            cf.translate(f,ic.lookup('capacitor_connector_top'),-grid_spacing-arc_width*2-arc_gap-arc_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             (capacitor_connector_length+capacitor_offset_y)/2+arc_gap/2)
            cf.translate(f,ic.lookup('capacitor_connector_bottom'),-grid_spacing-arc_width*2-arc_gap-arc_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             -(capacitor_connector_length-capacitor_offset_y)/2-arc_gap/2)
        #right side
        if draw_right:
            cf.translate(f,ic.lookup('capacitor_connector_top_right'),-(-grid_spacing-arc_width*2-arc_gap-arc_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             (capacitor_connector_length+capacitor_offset_y)/2+arc_gap/2)
            cf.translate(f,ic.lookup('capacitor_connector_bottom_right'),-(-grid_spacing-arc_width*2-arc_gap-arc_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             -(capacitor_connector_length-capacitor_offset_y)/2-arc_gap/2)

        #liftoff
        if draw_left:
            cf.translate(f,ic.lookup('liftoff_aluminum'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             capacitor_connector_length+arc_gap/2+liftoff_gap_size/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('liftoff_aluminum'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             -capacitor_connector_length-arc_gap/2-liftoff_gap_size/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             capacitor_connector_length+arc_gap/2-capacitor_rail_width/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                             -capacitor_connector_length-arc_gap/2+capacitor_rail_width/2+capacitor_offset_y)
        #right
        if draw_right:
            cf.translate(f,ic.lookup('liftoff_aluminum'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             capacitor_connector_length+arc_gap/2+liftoff_gap_size/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('liftoff_aluminum'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             -capacitor_connector_length-arc_gap/2-liftoff_gap_size/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             capacitor_connector_length+arc_gap/2-capacitor_rail_width/2+capacitor_offset_y)
            cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                             -capacitor_connector_length-arc_gap/2+capacitor_rail_width/2+capacitor_offset_y)
        

        # minus one finger width for start and plus one finger width for last were no gap is needed
        #number_of_fingers = int((capacitor_length-capacitor_finger_start_gap)*(1-remove_capacitor_finger_fraction)/(capacitor_finger_width*2))-remove_finger_number
        #number_of_fingers_right = int((capacitor_length-capacitor_finger_start_gap)*(1-remove_capacitor_finger_fraction_right)/(capacitor_finger_width_right*2))-remove_finger_number_right
        '''
        print("number of fingers:",number_of_fingers)
        cap = 5.5E-17*number_of_fingers*(capacitor_finger_length-capacitor_finger_width)/microns
        print("capacitance: %.2f pF" % (cap*10**12))
        L = 14.3 # nH
        freq = 1/2./np.pi/np.sqrt(L*10**-9*cap)
        print("frequency: %.2f MHz" % (freq/10**6))
        L = 12.1 # nH
        freq = 1/2./np.pi/np.sqrt(L*10**-9*cap)
        print("frequency: %.2f MHz" % (freq/10**6))
        Q = 40000
        n_coupling_fingers = np.round(np.sqrt(50000*number_of_fingers**1.5/Q))
        print("number of coupling fingers for Q %.0f: %.1f" % (Q,n_coupling_fingers))
        '''
 
        if draw_left:
            for i in range(0,number_of_fingers//2):
                cf.translate(f,ic.lookup('capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width*1/2-capacitor_finger_width*4*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap),
                                 -capacitor_finger_end_gap/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width*1/2-capacitor_finger_width*4*i-capacitor_finger_width*2-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap),
                                 +capacitor_finger_end_gap/2+capacitor_offset_y)
            if  np.mod(number_of_fingers,2) == 1:
                i = i+1
                cf.translate(f,ic.lookup('capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width*1/2-capacitor_finger_width*4*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap),
                                 -capacitor_finger_end_gap/2+capacitor_offset_y)

        #right side
        if draw_right:
            for i in range(0,number_of_fingers_right//2):
                cf.translate(f,ic.lookup('capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width_right*1/2-capacitor_finger_width_right*4*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap)),
                                 -capacitor_finger_end_gap/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width_right*1/2-capacitor_finger_width_right*4*i-capacitor_finger_width_right*2-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap)),
                                 +capacitor_finger_end_gap/2+capacitor_offset_y)
            if  np.mod(number_of_fingers_right,2) == 1:
                i = i+1
                cf.translate(f,ic.lookup('capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width_right*1/2-capacitor_finger_width_right*4*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap)),
                                 -capacitor_finger_end_gap/2+capacitor_offset_y)

    #####################################################################################
    #                        coupling capacitor
    #####################################################################################
        print("**********************",number_of_coupling_fingers//2,"**********************")
        print("**********************",number_of_coupling_fingers_right//2,"**********************")
        # left
        if draw_left:
            for i in range(0,number_of_coupling_fingers//2):
                cf.translate(f,ic.lookup('coupling_capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width*5/2-coupling_capacitor_finger_width*4*i+(2-n_arcs)*(arc_width+arc_gap),
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2+coupling_capacitor_finger_end_gap)
                cf.translate(f,ic.lookup('coupling_capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width*5/2-coupling_capacitor_finger_width*4*i+coupling_capacitor_finger_width*2+(2-n_arcs)*(arc_width+arc_gap),
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)
            if  np.mod(number_of_coupling_fingers,2) == 1:
                print('odd')
                i = i+1
                cf.translate(f,ic.lookup('coupling_capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width*5/2-coupling_capacitor_finger_width*4*i+coupling_capacitor_finger_width*2+(2-n_arcs)*(arc_width+arc_gap),
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)
        if draw_right:
            for i in range(0,number_of_coupling_fingers_right//2):
                cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width_right*5/2-coupling_capacitor_finger_width_right*4*i+(2-n_arcs)*(arc_width+arc_gap)),
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2+coupling_capacitor_finger_end_gap)
                cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width_right*5/2-coupling_capacitor_finger_width_right*4*i+coupling_capacitor_finger_width_right*2+(2-n_arcs)*(arc_width+arc_gap)),
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)
            if  np.mod(number_of_coupling_fingers_right,2) == 1:
                print('odd')
                i = i+1
                cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width_right*5/2-coupling_capacitor_finger_width_right*4*i+coupling_capacitor_finger_width_right*2+(2-n_arcs)*(arc_width+arc_gap)),
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)

        # left
        if draw_left:
            cf.translate(f,ic.lookup('capacitor_to_coupling_capacitor_connector'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width/2+(2-n_arcs)*(arc_width+arc_gap),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap/2)
            cf.translate(f,ic.lookup('coupling_capacitor_connector'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width/2+(2-n_arcs)*(arc_width+arc_gap),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width/2)
            cf.translate(f,ic.lookup('coupling_capacitor_connector'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width/2+(2-n_arcs)*(arc_width+arc_gap),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+3*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap)
            cf.translate(f,ic.lookup('coupling_capacitor_connector_vertical'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width/2+(2-n_arcs)*(arc_width+arc_gap),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+4*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+coupling_connector_length_vertical/2)
        # right
        if draw_right:
            cf.translate(f,ic.lookup('capacitor_to_coupling_capacitor_connector'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width/2+(2-n_arcs)*(arc_width+arc_gap)),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap/2)
            cf.translate(f,ic.lookup('coupling_capacitor_connector_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width_right/2+(2-n_arcs)*(arc_width+arc_gap)),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width/2)
            cf.translate(f,ic.lookup('coupling_capacitor_connector_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width_right/2+(2-n_arcs)*(arc_width+arc_gap)),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+3*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap)
            cf.translate(f,ic.lookup('coupling_capacitor_connector_vertical'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width/2+(2-n_arcs)*(arc_width+arc_gap)),
                             capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+4*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+coupling_connector_length_vertical/2)


            


    #####################################################################################
    #                        deep etch and other stuff
    #####################################################################################


        cf.translate(f,ic.lookup('inductor_trench'),0,0)
        if draw_left:
            cf.translate(f,ic.lookup('capacitor_trench'),
                             -(grid_spacing+arc_width*2+arc_gap+absorber_extension_length)-capacitor_trench_x/2,
                             +length_of_coupling_fingers/2+capacitor_rail_width+capacitor_offset_y+\
                             coupling_capacitor_finger_end_gap/2+capacitor_to_coupling_capacitor_gap/2)
        if draw_right:
            cf.translate(f,ic.lookup('capacitor_trench_right'),
                             -(-(grid_spacing+arc_width*2+arc_gap+absorber_extension_length)-capacitor_trench_x_right/2),
                             +length_of_coupling_fingers/2+capacitor_rail_width+capacitor_offset_y+\
                             coupling_capacitor_finger_end_gap+capacitor_to_coupling_capacitor_gap/2)

        cf.translate(f,ic.lookup('choke_radius'),0,0)
        cf.translate(f,ic.lookup('choke_inner_radius'),0,0)
        cf.translate(f,ic.lookup('guide_radius'),0,0)
        cf.translate(f,ic.lookup('inductor_border_etch'),0,capacitor_offset_y)
        cf.translate(f,ic.lookup('inductor_border_etch_2'),0,5*microns)

        cf.translate(f,ic.lookup('feedline'),0,feedline_y_location)

        



    cf.end_subset(f)
    if file_write_mode == "w":
        cf.end_file(f)
    f.close()

    # for key in ic.id:
    #     print(ic.id[key],key)

    if ic != None:
        ic.appendix_name = ''
        return ic


if __name__ == "__main__":
    #filename = "8-arc_1_1um-2-line_0_8um-al_1_3-unshorted.cif"
    filename = "polekid.cif"
    main(filename)




