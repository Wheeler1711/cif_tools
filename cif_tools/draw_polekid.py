import numpy as np
#import matplotlib.pyplot as plt
from cif_tools import cif_functions as cf
#import cif_functions as cf

# n_arc and n_grids

microns = 100
nanometers = 0.1




def main(filename,
    file_write_mode ="w", #w is new file, a is append to file
    pixel_name = "multi-octave_polekid",
    index_offset = 0,
    L_per_square = 35, #pH
    L_geometric = 0,
    thickness = 0.046, #ums
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    draw_inductors = True,
    draw_only_inductors = False,
    meander_inside = False,
    n_lines = 4,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(1400*nanometers),#int(800*nanometers),
    arc_width_right = int(1400*nanometers),#int(800*nanometers),
    arc_gap = int(1.0*microns),
    arc_gap_two_pols = int(3.0*microns),
    n_arcs = 20,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(1400*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(1400*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 14,#25,
    number_of_fingers_right = 26,#12,#15,
    capacitor_finger_overlap = 900*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -0*microns,
    capacitor_finger_width = 12*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 5*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 12,#20,
    number_of_coupling_fingers_right = 14,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 620*microns,
    feedline_width = 45*microns,
    feedline_layer = 4,
    vertical_feedline = False,
    feedline_delta = 0.1*microns,
    pixel_size = 1400*microns,
    capacitor_end_connector = False,
    capacitor_layer = 4,
    capacitor_connector_layer = 5,
    short_layer = 4,
    liftoff_layer = 2,
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = -15,
    short_width = int(1200*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*0*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*5.25*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    guide_radius = 112.5*microns,
    choke_radius = int(220+70)*microns,
    choke_outer_width = 100*microns,
    guide_flare_factor = 1.1,
    choke_start_radius = 200*microns,
    draw_bottom_coupling_cap = False,
    coupling_cap_loc = 'inner',
    ic = None,
    add_extra = None):#[], # leave as [] for no shorts):
    
    gap_size = separation_x_pol+between_pol_gap*2+line_width*2+(n_lines-2)*(separation_x_pol+line_width)#4*microns, # ums
    line_length = int(grid_spacing-gap_size/2)
    min_end_meander_length = 6*microns#meander_height/2+line_width
    meander_unit_cell_height = line_width*2+meander_height*2
    length_of_coupling_fingers = int(coupling_finger_overlap + coupling_capacitor_finger_end_gap)
    capacitor_width = capacitor_finger_overlap+2*capacitor_finger_end_gap+2*capacitor_rail_width
    capacitor_length = int((np.ceil(number_of_fingers)-0.5)*capacitor_finger_width*2+capacitor_finger_start_gap+capacitor_finger_width)
    capacitor_length_right = int((np.ceil(number_of_fingers_right)-0.5)*capacitor_finger_width_right*2+capacitor_finger_start_gap+capacitor_finger_width_right)

    total_short_length_x = np.sum(short_lengths_x)
    total_short_length_y = np.sum(short_lengths_y)


    f = open(filename, file_write_mode)

    if ic == None:
        ic = cf.index_dictionary()
        ic.index_offset = index_offset
        print("ic = None")
        
    else:
        ic.appendix_name = pixel_name
        
    #print(short_centers_x)
    #print(short_lengths_x)
    print("meander_inside",meander_inside)

    #####################################################################################
    #                            draw basic shapes
    #####################################################################################
    if draw_inductors: #for MLA caps
        if not(meander_inside):
            #draw vertical grid line 
            cf.draw_rectangle(f,ic,line_width,line_length,layer = inductor_layer,scale_num = 1,name= 'vertical_line') #
            #draw horizontal grid line
            cf.draw_rectangle(f,ic,line_length,line_width,layer = inductor_layer,scale_num = 1,name= 'horizontal_line') #
            #draw vertical end cap 
            cf.draw_rectangle(f,ic,line_width*2+separation_y_pol,line_width,layer = inductor_layer,scale_num = 1,name= 'vertical_line_end_cap') #

            cf.draw_rectangle(f,ic,line_width,line_width*2+separation_x_pol,layer = inductor_layer,scale_num = 1,name= 'horizontal_line_end_cap') #

            for i in range(0,len(short_centers_x)):
                cf.draw_rectangle(f,ic,int(short_lengths_x[i]),short_width,layer = short_layer,scale_num = 1,name= 'short_x_'+str(i)) #
            for i in range(0,len(short_centers_y)):
                cf.draw_rectangle(f,ic,short_width,int(short_lengths_y[i]),layer = short_layer,scale_num = 1,name= 'short_y_'+str(i)) #


            remainder_length_horizontal = int(grid_spacing-line_length+arc_width+(n_lines_shorted-1)*(arc_gap+arc_width))

            remainder_length_vertical = int(grid_spacing-line_length-1*separation_x_pol/2-between_pol_gap-line_width+arc_width_right+(n_lines_shorted-1)*(arc_gap+arc_width))
            remainder_length_vertical_2 = int(grid_spacing-line_length-1*separation_x_pol/2-between_pol_gap-line_width+arc_width_right*2+arc_gap+2*(n_lines_shorted-1)*(arc_gap+arc_width))


            #meander_remainder get center lines the rest of the way to the arcs
            #meander vertical
            cf.draw_rectangle(f,ic,remainder_length_horizontal,line_width,layer = inductor_layer,scale_num = 1,name= 'remainder_horizontal') #
            cf.draw_rectangle(f,ic,2*arc_width+arc_gap,arc_width,layer = inductor_layer,scale_num = 1,name= 'horizantal_short') #
            cf.draw_rectangle(f,ic,line_width,remainder_length_vertical,layer = inductor_layer,scale_num = 1,name= 'remainder_vertical_1') #
            cf.draw_rectangle(f,ic,line_width,remainder_length_vertical_2,layer = inductor_layer,scale_num = 1,name= 'remainder_vertical_2') #

        horizontal_connect_meander_length = 1*meander_unit_cell_height


        #####################################################################################
        #                           inside arcs
        #####################################################################################
        # arcs are kind of complicated the idea is to offset the radius of the arc so that it
        # will mate pefectly (squarely and at right radius) with the inductor. This results
        # in an imperfect mate on the other side might use a spiral arc to make match perfect
        # on both sides in the future

        #   |\
        #   | \
        #   |0 \
        #   |__/\ r
        #   |    \
        #   |     \
        #   |______\
        #       x
        # arcsin(x/r)


        angle_to_cut_short_inside_1 = 180/np.pi*np.arcsin((separation_x_pol/2+(n_lines//2-n_lines_shorted)*(line_width+separation_x_pol))/np.sqrt(grid_spacing**2+(separation_x_pol/2+(n_lines//2-n_lines_shorted)*(line_width+separation_x_pol))**2))
        angle_to_cut_short_inside_2 = 180/np.pi*np.arcsin((1*separation_y_pol/2+arc_gap_two_pols+line_width+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt(grid_spacing**2+(3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))**2))
        angle_to_cut_short_inside_3 = 180/np.pi*np.arcsin((separation_y_pol/2+(n_lines-2)/2*(separation_y_pol+line_width)-(n_lines_shorted-1)*line_width-separation_y_pol*(n_lines_shorted-1))/np.sqrt(grid_spacing**2+(separation_y_pol/2+(n_lines-2)/2*(separation_y_pol+line_width)-(n_lines_shorted-1)*line_width-separation_y_pol*(n_lines_shorted-1))**2))


        #draw arc horizontal pol bottom
        for i in range(0,n_lines_shorted):
            cf.draw_arc(f,ic,grid_spacing+i*(arc_width+arc_gap),arc_width,180+angle_to_cut_short_inside_1, # near x_pol
                        270-angle_to_cut_short_inside_2,layer = arc_layer,scale_num = 1, # near y_pol
                        name= 'arc_horizontal_bottom_'+str(i))
        #draw arc horizontal pol top
            cf.draw_arc(f,ic,grid_spacing+i*(arc_width+arc_gap),arc_width,90+angle_to_cut_short_inside_2,180-angle_to_cut_short_inside_1,
                        layer = arc_layer,scale_num = 1,name= 'arc_horizontal_top_'+str(i))  #

        #draw arc vertical pol bottom
        for i in range(0,n_lines_shorted):
            cf.draw_arc(f,ic,grid_spacing+i*(line_width+arc_gap),arc_width_right,270+angle_to_cut_short_inside_3,90-angle_to_cut_short_inside_3,
                        layer = arc_layer,scale_num = 1,name= 'arc_vertical_bottom_'+str(i))  #

        #####################################################################################
        #                           outside arcs
        #####################################################################################
        angle_to_cut_short_outside_1 = 180/np.pi*np.arcsin((arc_gap_two_pols/2)/np.sqrt((grid_spacing+arc_gap_two_pols+arc_width)**2+(arc_gap_two_pols/2)**2))
        angle_to_cut_short_outside_2 = 180/np.pi*np.arcsin((1*separation_y_pol/2+arc_gap_two_pols+line_width+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt((grid_spacing+arc_gap_two_pols+arc_width)**2+(3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))**2))
        angle_to_cut_short_outside_2b = 180/np.pi*np.arcsin((2*arc_gap_two_pols+3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt((grid_spacing+arc_gap_two_pols+arc_width)**2+(3*separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))**2))
        #print(angle_to_cut_short_outside_2,angle_to_cut_short_outside_2b)
        angle_to_cut_short_outside_3 = 180/np.pi*np.arcsin((separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))/np.sqrt((grid_spacing+arc_gap_two_pols+arc_width)**2+(separation_y_pol/2+line_width+(n_lines-2)/2*(separation_y_pol+line_width))**2))



        #draw outside arc vertical pol bottom

        for i in range(n_lines_shorted,n_arcs):
            cf.draw_arc(f,ic,grid_spacing+arc_width_right*i+arc_gap*i,arc_width_right,0+angle_to_cut_short_outside_1,
                            90+pol_angle+angle_to_cut_short_outside_3,layer = arc_layer,scale_num = 1,name= 'arc_outer_vertical_top_'+str(i))
            cf.draw_arc(f,ic,grid_spacing+arc_width_right*i+arc_gap*i,arc_width_right,270+pol_angle-angle_to_cut_short_outside_3,
                            360-angle_to_cut_short_outside_1,layer = arc_layer,scale_num = 1,name= 'arc_outer_vertical_bottom_'+str(i))


            cf.draw_arc(f,ic,grid_spacing+arc_width*i+arc_gap*i,arc_width*1,180+angle_to_cut_short_outside_1,
                            270+pol_angle-angle_to_cut_short_outside_2,layer = arc_layer,scale_num = 1, #near y_pol
                            scale_denom = 1,name= 'arc_outer_horizontal_bottom_'+str(i),num_of_points = 100)
            #draw outside arc horizontal pol top
            cf.draw_arc(f,ic,grid_spacing+arc_width*i+arc_gap*i,arc_width,90+pol_angle+angle_to_cut_short_outside_2,
                            180-angle_to_cut_short_outside_1,layer = arc_layer,
                            scale_num = 1,name= 'arc_outer_horizontal_top_'+str(i))



        #####################################################################################
        #                           arc connectors
        #####################################################################################

        cf.draw_rectangle(f,ic,arc_width,arc_width*4+arc_gap*3,layer = arc_layer,scale_num = 1,name= 'vertical_arc_connector') #

        if not draw_only_inductors:
            horizontal_arc_connector_width = arc_width
            cf.draw_rectangle(f,ic,arc_width+absorber_extension_length+capacitor_rail_width,arc_width,layer = arc_layer,scale_num = 1,name= 'horizontal_arc_connector')
            cf.draw_rectangle(f,ic,arc_width_right+absorber_extension_length+capacitor_rail_width,arc_width_right,layer = arc_layer,scale_num = 1,name= 'horizontal_arc_connector_right')

        else: #bigger for connection to MLA
            horizontal_arc_connector_width = 5*microns
            cf.draw_rectangle(f,ic,arc_width+absorber_extension_length+capacitor_rail_width,
                                  horizontal_arc_connector_width,layer = capacitor_layer,scale_num = 1,name= 'horizontal_arc_connector')
            cf.draw_rectangle(f,ic,arc_width_right+absorber_extension_length+capacitor_rail_width,
                                  horizontal_arc_connector_width,layer = capacitor_layer,scale_num = 1,name= 'horizontal_arc_connector_right')

        l_double_arc_connector = arc_width_right*2*(n_lines_shorted)+arc_gap+2*arc_gap*(n_lines_shorted-1)
        cf.draw_rectangle(f,ic,l_double_arc_connector,arc_width_right,layer = arc_layer,scale_num = 1,name= 'double_arc_connector')
        cf.draw_rectangle(f,ic,line_width,l_double_arc_connector,layer = arc_layer,scale_num = 1,name= 'double_arc_connector_vertical')

    if draw_only_inductors:
        cf.draw_rectangle(f,ic,int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length*2-(2-n_arcs)*(arc_width+arc_gap)*2)+5*microns,
                              int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length*2-(2-n_arcs)*(arc_width+arc_gap)*2)+5*microns
                              ,layer = 2,scale_num = 1,name= 'inductor_inversion')
        cf.draw_rectangle(f,ic,int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length*2-(2-n_arcs)*(arc_width+arc_gap)*2),
                              int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length*2-(2-n_arcs)*(arc_width+arc_gap)*2)
                              ,layer = 1,scale_num = 1,name= 'capacitor_inversion')

    if not draw_only_inductors:

        #####################################################################################
        #                           liftoff aluminum
        #####################################################################################

        #liftoff aluminum
        liftoff_length = capacitor_rail_width*2+liftoff_gap_size
        cf.draw_rectangle(f,ic,capacitor_rail_width,liftoff_length,layer = liftoff_layer,scale_num = 1,name= 'liftoff_aluminum')

        #liftoff pad
        cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_rail_width,layer = capacitor_connector_layer,scale_num = 1,name= 'liftoff_aluminum_pad')


        #####################################################################################
        #                            draw capacitor shapes
        #####################################################################################

        # draw capacitor rail
        cf.draw_rectangle(f,ic,capacitor_length+capacitor_rail_width,capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'capacitor_rail') #
        cf.draw_rectangle(f,ic,capacitor_length_right+capacitor_rail_width,capacitor_rail_width,layer = capacitor_layer,scale_num = 1,name= 'capacitor_rail_right') #

        # capacitor end connector
        if capacitor_end_connector:
            cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_finger_overlap+capacitor_finger_end_gap*2+capacitor_rail_width*2,layer = capacitor_layer,scale_num = 1,name= 'capacitor_end_connector') #

        # draw capacitor connector
        capacitor_connector_length = int(capacitor_finger_overlap/2+capacitor_finger_end_gap-arc_gap_two_pols/2-liftoff_gap_size)
        cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_connector_length+capacitor_offset_y,layer = capacitor_connector_layer,scale_num = 1,name= 'capacitor_connector_top') #
        cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_connector_length-capacitor_offset_y,layer = capacitor_connector_layer,scale_num = 1,name= 'capacitor_connector_bottom') #
        cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_connector_length+capacitor_offset_y,layer = capacitor_connector_layer,scale_num = 1,name= 'capacitor_connector_top_right') #
        cf.draw_rectangle(f,ic,capacitor_rail_width,capacitor_connector_length-capacitor_offset_y,layer = capacitor_connector_layer,scale_num = 1,name= 'capacitor_connector_bottom_right') #
        #capacitor_finger
        capacitor_finger_length = int(capacitor_finger_overlap+capacitor_finger_end_gap)

        if number_of_fingers != int(number_of_fingers):
            partial_finger_size = int((number_of_fingers-np.floor(number_of_fingers))*capacitor_finger_overlap+capacitor_finger_end_gap)
        else:
            partial_finger_size = capacitor_finger_length

        cf.draw_rectangle(f,ic,capacitor_finger_width,capacitor_finger_length,layer = capacitor_layer,scale_num = 1,name= 'capacitor_finger') #
        cf.draw_rectangle(f,ic,capacitor_finger_width,partial_finger_size,layer = capacitor_layer,scale_num = 1,name= 'capacitor_finger_partial') #
        #capacitor_finger_right
        capacitor_finger_length_right = int(capacitor_finger_overlap+capacitor_finger_end_gap)
        if number_of_fingers_right != int(number_of_fingers_right):
            partial_finger_size_right = int((number_of_fingers_right-np.floor(number_of_fingers_right))*capacitor_finger_overlap+capacitor_finger_end_gap)
        else:
            partial_finger_size_right = capacitor_finger_length_right

        cf.draw_rectangle(f,ic,capacitor_finger_width_right,capacitor_finger_length_right,layer = capacitor_layer,scale_num = 1,name= 'capacitor_finger_right') #
        cf.draw_rectangle(f,ic,capacitor_finger_width_right,partial_finger_size_right,layer = capacitor_layer,scale_num = 1,name= 'capacitor_finger_partial_right') #
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
        if coupling_cap_loc == "inner":
            #coupling_capacitor_connector_inner_length = int(grid_spacing-feedline_width)
            coupling_capacitor_connector_inner_length = int(grid_spacing+arc_width*2+arc_gap+coupling_capacitor_rail_width+absorber_extension_length-(2-n_arcs)*(arc_width+arc_gap))-feedline_width
            coupling_capacitor_connector_inner_length_right = int(grid_spacing+arc_width*2+arc_gap+coupling_capacitor_rail_width+absorber_extension_length-(2-n_arcs)*(arc_width+arc_gap))
            print(coupling_capacitor_connector_inner_length)
            cf.draw_rectangle(f,ic,coupling_capacitor_connector_inner_length,
                                  coupling_capacitor_rail_width,
                                  layer = capacitor_layer,
                                  name= 'coupling_capacitor_connector_inner') #
            cf.draw_rectangle(f,ic,coupling_capacitor_connector_inner_length_right,
                                  coupling_capacitor_rail_width,
                                  layer = capacitor_layer,
                                  name= 'coupling_capacitor_connector_inner_right') #
        #coupling_connector_length_vertical = int((feedline_y_location-feedline_width/2)-(capacitor_finger_overlap/2+capacitor_finger_end_gap+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+capacitor_rail_width*1+coupling_capacitor_rail_width*2+capacitor_to_coupling_capacitor_gap+capacitor_offset_y)+feedline_width)
        coupling_connector_length_vertical = int((feedline_y_location-feedline_width/2)-(capacitor_finger_overlap/2+capacitor_finger_end_gap+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+capacitor_rail_width*1+coupling_capacitor_rail_width*2+capacitor_to_coupling_capacitor_gap+capacitor_offset_y)+0.1*microns)

        #print(coupling_connector_length_vertical)
        cf.draw_rectangle(f,ic,coupling_capacitor_rail_width,coupling_connector_length_vertical,layer = capacitor_layer,scale_num = 1,name= 'coupling_capacitor_connector_vertical')
        # draw leg to coupling capacitor
        cf.draw_rectangle(f,ic,capacitor_rail_width,int(np.abs(capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+capacitor_rail_width)),layer = capacitor_layer,scale_num = 1,name= 'capacitor_to_coupling_capacitor_connector') #

        #####################################################################################
        #                            feedline shapes
        #####################################################################################
        cf.draw_rectangle(f,ic,int(pixel_size+feedline_delta*2),feedline_width,layer = feedline_layer,scale_num = 1,name= 'feedline') #
        if vertical_feedline:
            cf.draw_rectangle(f,ic,feedline_width,int(pixel_size*np.sqrt(3)/2+feedline_delta*2),layer = feedline_layer,scale_num = 1,name= 'feedline_vertical') #


        #####################################################################################
        #                            border
        #####################################################################################


        cf.draw_rectangle(f,ic,pixel_size,int(pixel_size*np.sqrt(3)/2),layer = 3,scale_num = 1,name= 'pixel_size') #
        cf.draw_arc(f,ic,choke_radius,choke_outer_width,0,360,layer = 10,scale_num = 1,name= 'choke_radius') #
        cf.draw_arc(f,ic,int(guide_radius*guide_flare_factor),
                        choke_start_radius-int(guide_radius*guide_flare_factor),0,360,layer = 10,scale_num = 1,name= 'choke_inner_radius') #
        cf.draw_circle(f,ic,int(guide_radius),layer = 11,scale_num = 1,name= 'guide_radius')
        #cf.draw_rectangle(f,ic,int(grid_spacing*2+arc_width*2*2+arc_gap*2*2+capacitor_rail_width*2+np.min((capacitor_finger_width,capacitor_finger_width_right))),
        #                      int(arc_gap+capacitor_connector_length*2+liftoff_gap_size),layer = 1,scale_num = 1,name= 'inductor_border_etch')
        cf.draw_rectangle(f,ic,int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length*2-(2-n_arcs)*(arc_width+arc_gap)*2)-5*microns,
                              int(grid_spacing*2+arc_width*2*2+arc_gap*2+absorber_extension_length*2-(2-n_arcs)*(arc_width+arc_gap)*2)-5*microns
                              ,layer = 1,scale_num = 1,name= 'inductor_border_etch')


        #-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)
        #####################################################################################
        #                            deep etch trench
        #####################################################################################
        if coupling_cap_loc == 'inner':
            inductor_trench_y = capacitor_width+coupling_capacitor_rail_width*4+\
          capacitor_to_coupling_capacitor_gap*2+length_of_coupling_fingers*2+coupling_capacitor_finger_end_gap*2
        else:
            inductor_trench_y = 2*choke_radius+ 2*choke_outer_width+20*microns
        cf.draw_rectangle(f,ic,(grid_spacing+arc_width*2+arc_gap+absorber_extension_length+capacitor_rail_width)*2-2*(2-n_arcs)*(arc_width+arc_gap),inductor_trench_y+10*microns,
                              layer = 6,scale_num = 1,name= 'inductor_trench') #
        capacitor_trench_x = capacitor_length+capacitor_rail_width
        capacitor_trench_x_right = capacitor_length_right+capacitor_rail_width
        if coupling_cap_loc == 'inner':
            capacitor_trench_y = capacitor_width
        else:
            capacitor_trench_y = capacitor_width+coupling_capacitor_rail_width*4+\
          capacitor_to_coupling_capacitor_gap*2+length_of_coupling_fingers*2+coupling_capacitor_finger_end_gap*2#+100*microns

        cf.draw_rectangle(f,ic,capacitor_trench_x+10*microns,capacitor_trench_y+10*microns,layer = 6,scale_num = 1,name= 'capacitor_trench') #
        cf.draw_rectangle(f,ic,capacitor_trench_x_right+10*microns,capacitor_trench_y+10*microns,layer = 6,scale_num = 1,name= 'capacitor_trench_right') #

    if draw_inductors:
        if meander_inside: # for meandered aluminum (might be broken now)

            #####################################################################################
            #                            draw meander shapes
            #####################################################################################

            #meander horizontal
            cf.draw_rectangle(f,ic,meander_length,line_width,layer = inductor_layer,scale_num = 1,name= 'meander_horizontal') #
            #meander vertical
            cf.draw_rectangle(f,ic,line_width,meander_height,layer = inductor_layer,scale_num = 1,name= 'meander_vertical') #
            #meander vertical_2
            cf.draw_rectangle(f,ic,line_width,int(np.ceil(meander_height/2)+20*nanometers),layer = inductor_layer,scale_num = 1,name= 'meander_vertical_2') #


            number_of_meanders = int(np.floor((line_length-min_end_meander_length*2)/meander_unit_cell_height))
            remainder_length_horizontal = int((grid_spacing-number_of_meanders*meander_unit_cell_height-horizontal_connect_meander_length/2.+arc_width_right))
            #print("number of meanders:",number_of_meanders)
            #print("remainder length horizontal:",remainder_length_horizontal,"\n")
            remainder_length_vertical = int((grid_spacing-number_of_meanders*meander_unit_cell_height-1*separation_x_pol/2-between_pol_gap-line_width*2-meander_length-3*meander_height/2+arc_width_right))
            remainder_length_vertical_2 = int((grid_spacing-number_of_meanders*meander_unit_cell_height-1*separation_x_pol/2-between_pol_gap-line_width*2-meander_length-3*meander_height/2+arc_width_right*2+arc_gap))

            #meander_remainder
            #meander vertical
            cf.draw_rectangle(f,ic,remainder_length_horizontal,line_width,layer = inductor_layer,scale_num = 1,name= 'remainder_horizontal') #
            cf.draw_rectangle(f,ic,line_width,remainder_length_vertical,layer = inductor_layer,scale_num = 1,name= 'remainder_vertical_1') #
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


    if draw_inductors:
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
                cf.translate(f,ic.lookup('remainder_horizontal'),
                                 -meander_unit_cell_height*number_of_meanders-horizontal_connect_meander_length/2-remainder_length_horizontal/2,
                                 -(separation_x_pol/2+line_width/2))#bottom
                cf.translate(f,ic.lookup('remainder_horizontal'),
                                 -meander_unit_cell_height*number_of_meanders-horizontal_connect_meander_length/2-remainder_length_horizontal/2,
                                 (separation_x_pol/2+line_width/2))#bottom

            if draw_right:
                cf.translate(f,ic.lookup('remainder_vertical_1'),(separation_y_pol/2+line_width/2),
                                 -meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical/2)#bottom
                cf.translate(f,ic.lookup('remainder_vertical_1'),(separation_y_pol/2+line_width/2),
                                 -(-meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical/2))#top
                cf.translate(f,ic.lookup('remainder_vertical_2'),-(separation_y_pol/2+line_width/2),
                                 -meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical_2/2)#bottom
                cf.translate(f,ic.lookup('remainder_vertical_2'),-(separation_y_pol/2+line_width/2),
                                 -(-meander_unit_cell_height*number_of_meanders-1*separation_x_pol/2-between_pol_gap-meander_length-(meander_unit_cell_height-meander_height/2)-remainder_length_vertical_2/2))#top

        else:
            #no meandering
            #Tony Mod
            if draw_left:
                for i in range(0,n_lines):
                    cf.translate(f,ic.lookup('horizontal_line'),-line_length/2,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#
                    cf.translate(f,ic.lookup('horizontal_line'),line_length/2,separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#

                    if aluminum_left == True:
                        for k in range(0,len(short_centers_x)):
                            cf.translate(f,ic.lookup('short_x_'+str(k)),short_centers_x[k],
                                          separation_x_pol/2+line_width/2+(i - n_lines/2)*(line_width+separation_x_pol))#


                    cf.translate(f,ic.lookup('remainder_horizontal'),-line_length-remainder_length_horizontal/2,
                                 (separation_x_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_x_pol))#bottom


                    if np.mod(i,2) == 0:
                        cf.translate(f,ic.lookup('horizontal_line_end_cap'),line_length-line_width/2,
                                         (-separation_x_pol/2-line_width) + (-separation_x_pol-line_width)*(n_lines-2)/2\
                                         +(separation_x_pol+line_width*2)/2+ (separation_x_pol+line_width)*i )#



            #vertical lines
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

                    if np.mod(i,2) == 0:
                        cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2
                                         +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                         separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2)
                        cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2\
                                         +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                     -(separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2))

                for i in range(0,n_lines-1):
                    if n_lines/n_lines_shorted >2:
                        if np.mod(i,2) == 1:
                            cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2
                                         +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                         grid_spacing-line_width/2)
                            cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2\
                                         +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                     -(grid_spacing-line_width/2))

                            cf.translate(f,ic.lookup('horizontal_line_end_cap'),-(line_length-line_width/2)-remainder_length_horizontal,
                                         (-separation_x_pol/2-line_width) + (-separation_x_pol-line_width)*(n_lines-2)/2\
                                         +(separation_x_pol+line_width*2)/2+ (separation_x_pol+line_width)*i )#           

                    for i in range(0,n_lines_shorted):
                        cf.translate(f,ic.lookup('remainder_vertical_1'),-((separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol)),
                                         -line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical/2)#bottom
                        cf.translate(f,ic.lookup('remainder_vertical_1'),-((separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol)),
                                         -(-line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical/2))#top
                        cf.translate(f,ic.lookup('remainder_vertical_2'),+((separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol)),
                                         -line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical_2/2)#bottom
                        cf.translate(f,ic.lookup('remainder_vertical_2'),+((separation_y_pol/2+line_width/2)+(i - n_lines/2)*(line_width+separation_y_pol)),
                                         -(-line_length-1*separation_x_pol/2-line_width-between_pol_gap-remainder_length_vertical_2/2))#top



            if n_lines_shorted>1:              
                for i in range(1,n_lines-1,n_lines_shorted*2):
                    if draw_right:
                        cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2
                                         +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                         separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2)
                        cf.translate(f,ic.lookup('vertical_line_end_cap'),(-separation_y_pol/2-line_width) + (-separation_y_pol-line_width)*(n_lines-2)/2\
                                         +(separation_y_pol+line_width*2)/2+ (separation_y_pol+line_width)*i ,
                                     -(separation_x_pol/2+2*line_width+between_pol_gap-line_width/2-(2-n_lines)*(separation_x_pol+line_width)/2))

                    if draw_left:
                        cf.translate(f,ic.lookup('horizontal_line_end_cap'),line_length-line_width/2,
                                         (-separation_x_pol/2-line_width) + (-separation_x_pol-line_width)*(n_lines-2)/2\
                                         +(separation_x_pol+line_width*2)/2+ (separation_x_pol+line_width)*i )#






            # right connectors at bottom and top arcs
            if draw_right:
                for i in range(0,n_arcs//2,n_lines_shorted):
                    #cf.translate(f,ic.lookup('double_arc_connector_vertical'),
                    #                 -(separation_y_pol/2+line_width/2)-(n_lines-2)/2*(separation_y_pol+line_width),
                    #                 (-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2))#bottom
                    cf.translate_and_rotate(f,ic.lookup('double_arc_connector_vertical'),
                                     line_width/2,#should be line_width/2 but fudging a bit
                                     (-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2),-angle_to_cut_short_outside_3)#bottom
                    #cf.translate(f,ic.lookup('double_arc_connector_vertical'),
                    #                 -(separation_y_pol/2+line_width/2)-(n_lines-2)/2*(separation_y_pol+line_width),
                    #                 -(-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2))#top
                    cf.translate_and_rotate(f,ic.lookup('double_arc_connector_vertical'),
                                     line_width/2,
                                     -(-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2),angle_to_cut_short_outside_3)#top


        #arc connectors
        if draw_left:
            #h^2 = x^2+y^2
            #y^2 = h^2-x^2
            for i in range(0,n_arcs//2,n_lines_shorted):
                #cf.translate(f,ic.lookup('double_arc_connector_vertical'),
                #                 -(separation_y_pol/2+line_width/2)-(n_lines-2)/2*(separation_y_pol+line_width)-arc_width-separation_y_pol,
                #                 (-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2))#bottom
                cf.translate_and_rotate(f,ic.lookup('double_arc_connector_vertical'),
                                -line_width/4,
                                 (-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2),-angle_to_cut_short_outside_2)#bottom
                #cf.translate(f,ic.lookup('double_arc_connector_vertical'),
                #                 -(separation_y_pol/2+line_width/2)-(n_lines-2)/2*(separation_y_pol+line_width)-arc_width-separation_y_pol,
                #                 -(-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2))#top
                cf.translate_and_rotate(f,ic.lookup('double_arc_connector_vertical'),
                                 -line_width/4,
                                 -(-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2),angle_to_cut_short_outside_2)#top           

            # arcs
            #horizontal pol inside
            for i in range(0,n_lines_shorted):
                cf.translate(f,ic.lookup('arc_horizontal_bottom_'+str(i)),0,0)#bottom
                cf.translate(f,ic.lookup('arc_horizontal_top_'+str(i)),0,0)#top

        if draw_right:
            #veritcal pol inside
            for i in range(0,n_lines_shorted):
                cf.translate(f,ic.lookup('arc_vertical_bottom_'+str(i)),0,0)#both

        cf.end_subset(f)

    if ic.appendix_name != '':
        ic.appendix_name = '' #dont want pixel name to have appendix
        cf.start_subset(f,ic,subset_name = pixel_name)
        ic.appendix_name = pixel_name #dont want pixel name to have appendix
    else:
        cf.start_subset(f,ic,subset_name = pixel_name)


    #cf.translate(f,ic.lookup('WIP1'),0,0)
    #cf.translate(f,ic.lookup('WIP1_foot'),0,0)
    #cf.translate(f,ic.lookup('WIP1_foot_protect'),0,0)
    if draw_inductors:
        if pol_angle == 0:
            cf.translate(f,ic.lookup('inductors'),0,0)
        else:
            cf.rotate(f,ic.lookup('inductors'),pol_angle)


        # outer arcs
        if draw_left:
            for i in range(n_lines_shorted,n_arcs):
                cf.translate(f,ic.lookup('arc_outer_horizontal_bottom_'+str(i)),0,0)#top
                cf.translate(f,ic.lookup('arc_outer_horizontal_top_'+str(i)),0,0)#top

        if draw_right:
            for i in range(n_lines_shorted,n_arcs):
                cf.translate(f,ic.lookup('arc_outer_vertical_bottom_'+str(i)),0,0)#top
                cf.translate(f,ic.lookup('arc_outer_vertical_top_'+str(i)),0,0)#top


        # bottom left
        if draw_left:
            for i in range(n_lines_shorted,n_arcs//2+n_lines_shorted,n_lines_shorted):
                cf.translate(f,ic.lookup('double_arc_connector'),
                                 (-grid_spacing-arc_width_right*i*2-arc_gap*i*2-(arc_width_right*2+arc_gap)/2 -(-arc_gap-arc_width_right)),
                                 arc_gap_two_pols/2+arc_width_right/2)#left
                cf.translate(f,ic.lookup('double_arc_connector'),
                                 (-grid_spacing-arc_width_right*i*2-arc_gap*i*2-(arc_width_right*2+arc_gap)/2-(-arc_gap-arc_width_right)),
                                 -(arc_gap_two_pols/2+arc_width_right/2))#l

            cf.translate(f,ic.lookup('horizontal_arc_connector'),
                             -grid_spacing-arc_width-arc_gap-(arc_width+absorber_extension_length+capacitor_rail_width)/2+(2-n_arcs)*(arc_width+arc_gap),
                             arc_gap_two_pols/2+horizontal_arc_connector_width/2)#left
            #top left
            cf.translate(f,ic.lookup('horizontal_arc_connector'),
                             -grid_spacing-arc_width-arc_gap-(arc_width+absorber_extension_length+capacitor_rail_width)/2+(2-n_arcs)*(arc_width+arc_gap),
                             -(arc_gap_two_pols/2+horizontal_arc_connector_width/2))#left
        #right side
        if draw_right:
            for i in range(0,n_arcs//2,n_lines_shorted):
                cf.translate(f,ic.lookup('double_arc_connector'),
                                 -(-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2-(arc_width_right+arc_gap)*n_lines_shorted),
                                 arc_gap_two_pols/2+arc_width_right/2)#bottom
                cf.translate(f,ic.lookup('double_arc_connector'),
                                 -(-grid_spacing-arc_width_right*i*2-arc_gap*i*2-l_double_arc_connector/2-(arc_width_right+arc_gap)*n_lines_shorted),
                                 -(arc_gap_two_pols/2+arc_width_right/2))#bottom

            cf.translate(f,ic.lookup('horizontal_arc_connector_right'),
                             -(-grid_spacing-arc_width-arc_gap-(arc_width+absorber_extension_length+capacitor_rail_width)/2+(2-n_arcs)*(arc_width+arc_gap)),
                             arc_gap_two_pols/2+horizontal_arc_connector_width/2)#left
            #top  

            cf.translate(f,ic.lookup('horizontal_arc_connector_right'),
                             -(-grid_spacing-arc_width-arc_gap-(arc_width+absorber_extension_length+capacitor_rail_width)/2+(2-n_arcs)*(arc_width+arc_gap)),
                             -(arc_gap_two_pols/2+horizontal_arc_connector_width/2))#left


    if draw_only_inductors:
        cf.translate(f,ic.lookup('inductor_inversion'),0,0)
        cf.translate(f,ic.lookup('capacitor_inversion'),0,0)


    #inductor boarder etch
    #cf.translate(f,ic.lookup('inductor_border_etch'),0,0)#top left
    if not draw_only_inductors:

        #####################################################################################capacitor_end_conn
        #                            capacitor
        #####################################################################################



        if draw_entire_pixel:       
            if draw_left:
                cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
                if capacitor_end_connector:
                    cf.translate(f,ic.lookup('capacitor_end_connector'),-grid_spacing-capacitor_length-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                +capacitor_offset_y)

            # right side
            if draw_right:
                cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
                if capacitor_end_connector:
                    cf.translate(f,ic.lookup('capacitor_end_connector'),-(-grid_spacing-capacitor_length_right-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                +capacitor_offset_y)

            #     if draw_left:
            #         cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
            #                          -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
            #         cf.translate(f,ic.lookup('capacitor_rail'),-grid_spacing-capacitor_length/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
            #                          +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
            #         cf.translate(f,ic.lookup('capacitor_end_connector'),-grid_spacing-capacitor_length-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
            #                         +capacitor_offset_y)

            #     # right side
            #     if draw_right:
            #         cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
            #                          -capacitor_finger_overlap/2-capacitor_finger_end_gap-capacitor_rail_width/2+capacitor_offset_y)
            #         cf.translate(f,ic.lookup('capacitor_rail_right'),-(-grid_spacing-capacitor_length_right/2-capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
            #                          +capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width/2+capacitor_offset_y)
            #         cf.translate(f,ic.lookup('capacitor_end_connector'),-(-grid_spacing-capacitor_length_right-3*capacitor_rail_width/2-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
            #                         +capacitor_offset_y)

            if draw_left:
                cf.translate(f,ic.lookup('capacitor_connector_top'),
                                 -grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 (capacitor_connector_length+capacitor_offset_y)/2+arc_gap_two_pols/2)
                cf.translate(f,ic.lookup('capacitor_connector_bottom'),
                                 -grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 -(capacitor_connector_length-capacitor_offset_y)/2-arc_gap_two_pols/2)
            #right side
            if draw_right:
                cf.translate(f,ic.lookup('capacitor_connector_top_right'),
                                 -(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 (capacitor_connector_length+capacitor_offset_y)/2+arc_gap_two_pols/2)
                cf.translate(f,ic.lookup('capacitor_connector_bottom_right'),
                                 -(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 -(capacitor_connector_length-capacitor_offset_y)/2-arc_gap_two_pols/2)

            #liftoff
            if draw_left:
                cf.translate(f,ic.lookup('liftoff_aluminum'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 capacitor_connector_length+arc_gap/2+liftoff_gap_size/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('liftoff_aluminum'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 -capacitor_connector_length-arc_gap/2-liftoff_gap_size/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 capacitor_connector_length+arc_gap_two_pols/2-capacitor_rail_width/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap),
                                 -capacitor_connector_length-arc_gap_two_pols/2+capacitor_rail_width/2+capacitor_offset_y)
            #right
            if draw_right:
                cf.translate(f,ic.lookup('liftoff_aluminum'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 capacitor_connector_length+arc_gap/2+liftoff_gap_size/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('liftoff_aluminum'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 -capacitor_connector_length-arc_gap_two_pols/2-liftoff_gap_size/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 capacitor_connector_length+arc_gap_two_pols/2-capacitor_rail_width/2+capacitor_offset_y)
                cf.translate(f,ic.lookup('liftoff_aluminum_pad'),-(-grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)),
                                 -capacitor_connector_length-arc_gap_two_pols/2+capacitor_rail_width/2+capacitor_offset_y)


            # minus one finger width for start and plus one finger width for last were no gap is needed
            #number_of_fingers = int((capacitor_length-capacitor_finger_start_gap)*(1-remove_capacitor_finger_fraction)/(capacitor_finger_width*2))-remove_finger_number
            #number_of_fingers_right = int((capacitor_length-capacitor_finger_start_gap)*(1-remove_capacitor_finger_fraction_right)/(capacitor_finger_width_right*2))-remove_finger_number_right

            print("###############################################")
            print(pixel_name)
            print("###############################################")
            if draw_left:
                print("Left Resonator:")
                print("number of fingers:",number_of_fingers)
                cap = 5.5E-17*number_of_fingers*capacitor_finger_overlap/microns
                print("capacitance:       %.2f pF" % (cap*10**12))
                #print(L_per_square,grid_spacing,total_short_length_y,line_width,n_lines,n_lines_shorted)
                print(L_per_square,grid_spacing,total_short_length_y,line_width,n_lines,n_lines_shorted)
                L1 = L_per_square*(grid_spacing*2-total_short_length_y)/line_width*n_lines/n_lines_shorted**2*10**-12
                if arc_layer == inductor_layer:
                    L2 = L_per_square*(grid_spacing*2+n_arcs/2*(arc_gap+arc_width))/arc_width*np.pi/2*n_arcs/n_lines_shorted**2*10**-12
                    print(grid_spacing*2,n_arcs/2*(arc_gap*arc_width))
                else:
                    L2 = 0
                # diameter*pi/2*n_arcs
                L = L1+L2+L_geometric*10**-9 # H
                V = (L1/(L_per_square*10**-12)*line_width/microns*line_width/microns*thickness+\
                  L2/(L_per_square*10**-12)*arc_width/microns*arc_width/microns*thickness)*n_lines_shorted**2
                print("inductance center: %.2f nH" % (L1*10**9))
                print("inductance arcs:   %.2f nH" % (L2*10**9))
                print("inductance geo:    %.2f nH" % (L_geometric))
                print("total inductance:  %.2f nH" % (L*10**9))
                print("Volume:            %.2f um^3" % (V))        
                freq = 1/2./np.pi/np.sqrt(L*cap)
                print("frequency:         %.2f MHz" % (freq/10**6))
            if draw_right:
                print("")
                print("Right Resonator:")
                print("number of fingers:",number_of_fingers_right)
                cap = 5.5E-17*number_of_fingers_right*capacitor_finger_overlap/microns
                print("capacitance:       %.2f pF" % (cap*10**12))
                L1 = L_per_square*(grid_spacing*2-total_short_length_y)/line_width*n_lines/n_lines_shorted**2*10**-12
                if arc_layer == inductor_layer:
                    L2 = L_per_square*(grid_spacing*2+n_arcs/2*(arc_gap+arc_width))/arc_width*np.pi/2*n_arcs/n_lines_shorted**2*10**-12
                else:
                    L2 = 0
                # diameter*pi/2*n_arcs
                L = L1+L2+L_geometric*10**-9 # H
                V = (L1/(L_per_square*10**-12)*line_width/microns*line_width/microns*thickness+\
                  L2/(L_per_square*10**-12)*arc_width/microns*arc_width/microns*thickness)*n_lines_shorted**2
                print("inductance center: %.2f nH" % (L1*10**9))
                print("inductance arcs:   %.2f nH" % (L2*10**9))
                print("inductance geo:    %.2f nH" % (L_geometric))
                print("total inductance:  %.2f nH" % (L*10**9))
                print("Volume:            %.2f um^3" % (V))  
                freq = 1/2./np.pi/np.sqrt(L*cap)
                print("frequency:         %.2f MHz" % (freq/10**6))

                #freq = 1/2./np.pi/np.sqrt(L*10**-9*cap)
                #print("frequency: %.2f MHz" % (freq/10**6))
                #Q = 40000
                #n_coupling_fingers = np.round(np.sqrt(50000*number_of_fingers**1.5/Q))
                #print("number of coupling fingers for Q %.0f: %.1f" % (Q,n_coupling_fingers))


            if draw_left:
                if int(int(number_of_fingers)) == number_of_fingers:
                    place_n = int(number_of_fingers) -1
                else:
                    place_n = int(number_of_fingers)
                for i in range(0,place_n):
                    if np.mod(i,2)==0:
                        cf.translate(f,ic.lookup('capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width*1/2-capacitor_finger_width*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap),
                                     -capacitor_finger_end_gap/2+capacitor_offset_y)
                    else:
                        cf.translate(f,ic.lookup('capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width*1/2-capacitor_finger_width*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap),
                                     +capacitor_finger_end_gap/2+capacitor_offset_y)

                i = i + 1
                if np.mod(i,2)==0:
                    cf.translate(f,ic.lookup('capacitor_finger_partial'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width*1/2-capacitor_finger_width*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap),
                                     -capacitor_finger_end_gap/2+capacitor_offset_y-(capacitor_finger_length-partial_finger_size)/2)
                else:
                    cf.translate(f,ic.lookup('capacitor_finger_partial'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width*1/2-capacitor_finger_width*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap),
                                     +capacitor_finger_end_gap/2+capacitor_offset_y+(capacitor_finger_length-partial_finger_size)/2)
            #right side
            if draw_right:
                if int(int(number_of_fingers_right)) == number_of_fingers_right:
                    place_n = int(number_of_fingers_right) -1
                else:
                    place_n = int(number_of_fingers_right)
                for i in range(0,place_n):
                    if np.mod(i,2)==0:
                        cf.translate(f,ic.lookup('capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width_right*1/2-capacitor_finger_width_right*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap)),
                                     -capacitor_finger_end_gap/2+capacitor_offset_y)
                    else:
                        cf.translate(f,ic.lookup('capacitor_finger_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width_right*1/2-capacitor_finger_width_right*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap)),
                                     +capacitor_finger_end_gap/2+capacitor_offset_y)

                i = i+1
                if np.mod(i,2)==0:
                    cf.translate(f,ic.lookup('capacitor_finger_partial_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width_right*1/2-capacitor_finger_width_right*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap)),
                                     -capacitor_finger_end_gap/2+capacitor_offset_y-(capacitor_finger_length_right-partial_finger_size_right)/2)
                else:
                    cf.translate(f,ic.lookup('capacitor_finger_partial_right'),-(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width-capacitor_finger_width_right*1/2-capacitor_finger_width_right*2*i-capacitor_finger_start_gap+(2-n_arcs)*(arc_width+arc_gap)),
                                     +capacitor_finger_end_gap/2+capacitor_offset_y+(capacitor_finger_length_right-partial_finger_size_right)/2)

        #####################################################################################
        #                        coupling capacitor
        #####################################################################################
            #print("**********************",number_of_coupling_fingers//2,"**********************")
            #print("**********************",number_of_coupling_fingers_right//2,"**********************")
            # left
            if coupling_cap_loc == 'inner':
                cap_adjust = 0
                cap_connector_adjust = 0
                cap_finger_adjust = coupling_capacitor_finger_width-capacitor_rail_width*2
                cap_vertical_adjust = coupler_connector_width
                cap_vertical_adjust_right = coupler_connector_width_right
            else:
                cap_adjust = 0
                cap_connector_adjust = 0
                cap_finger_adjust = 0
                cap_vertical_adjust = 0
                cap_vertical_adjust_right = 0
            cf.start_subset(f,ic,subset_name = 'coupling_capacitor')


            if draw_left:
                if coupling_cap_loc == 'inner':
                    start_loc = -feedline_width-coupling_capacitor_finger_width*5/2+coupling_capacitor_rail_width
                    coupling_cap_y_loc = capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+\
                      capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2
                    for i in range(0,number_of_coupling_fingers//2):
                        cf.translate(f,ic.lookup('coupling_capacitor_finger'),
                                         start_loc-coupling_capacitor_finger_width*4*i,
                                         coupling_cap_y_loc)
                        cf.translate(f,ic.lookup('coupling_capacitor_finger'),
                                         start_loc-coupling_capacitor_finger_width*4*i+coupling_capacitor_finger_width*2,
                                         coupling_cap_y_loc+coupling_capacitor_finger_end_gap)
                    if  np.mod(number_of_coupling_fingers,2) == 1:
                        i = i+1
                        cf.translate(f,ic.lookup('coupling_capacitor_finger'),
                                         start_loc-coupling_capacitor_finger_width*4*i+coupling_capacitor_finger_width*2,
                                         coupling_cap_y_loc+coupling_capacitor_finger_end_gap)

                else:
                    for i in range(0,number_of_coupling_fingers//2):
                        cf.translate(f,ic.lookup('coupling_capacitor_finger'),
                                         -grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width*5/2-coupling_capacitor_finger_width*4*i+(2-n_arcs)*(arc_width+arc_gap)-cap_adjust-cap_finger_adjust,
                                         capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2+coupling_capacitor_finger_end_gap)
                        cf.translate(f,ic.lookup('coupling_capacitor_finger'),
                                         -grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width*5/2-coupling_capacitor_finger_width*4*i+coupling_capacitor_finger_width*2+(2-n_arcs)*(arc_width+arc_gap)-cap_adjust-cap_finger_adjust,
                                         capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)
                    if  np.mod(number_of_coupling_fingers,2) == 1:
                        #print('odd')
                        i = i+1
                        cf.translate(f,ic.lookup('coupling_capacitor_finger'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width*5/2-coupling_capacitor_finger_width*4*i+coupling_capacitor_finger_width*2+(2-n_arcs)*(arc_width+arc_gap)-cap_adjust-cap_finger_adjust,
                                         capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)




            if draw_right:
                if coupling_cap_loc == 'inner':
                    start_loc = -coupling_capacitor_finger_width_right*5/2+coupling_capacitor_rail_width
                    coupling_cap_y_loc = capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+\
                      capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2
                    for i in range(0,number_of_coupling_fingers_right//2):
                        cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),
                                         -(start_loc-coupling_capacitor_finger_width_right*4*i),
                                         coupling_cap_y_loc)
                        cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),
                                         -(start_loc-coupling_capacitor_finger_width_right*4*i+coupling_capacitor_finger_width*2),
                                         coupling_cap_y_loc+coupling_capacitor_finger_end_gap)
                    if  np.mod(number_of_coupling_fingers_right,2) == 1:
                        #print('odd')
                        i = i+1
                        cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),
                                         -(start_loc-coupling_capacitor_finger_width_right*4*i+coupling_capacitor_finger_width*2),
                                         coupling_cap_y_loc+coupling_capacitor_finger_end_gap)
                else:
                    for i in range(0,number_of_coupling_fingers_right//2):
                        cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),
                                     -(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width_right*5/2-coupling_capacitor_finger_width_right*4*i+(2-n_arcs)*(arc_width+arc_gap))+cap_adjust+cap_finger_adjust,
                                     capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2+coupling_capacitor_finger_end_gap)
                        cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),
                                     -(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width_right*5/2-coupling_capacitor_finger_width_right*4*i+coupling_capacitor_finger_width_right*2+(2-n_arcs)*(arc_width+arc_gap))+cap_adjust+cap_finger_adjust,
                                     capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)
                    if  np.mod(number_of_coupling_fingers_right,2) == 1:
                    #print('odd')
                        i = i+1
                        cf.translate(f,ic.lookup('coupling_capacitor_finger_right'),
                                     -(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupling_capacitor_finger_width_right*5/2-coupling_capacitor_finger_width_right*4*i+coupling_capacitor_finger_width_right*2+(2-n_arcs)*(arc_width+arc_gap))+cap_adjust+cap_finger_adjust,
                                     capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width+length_of_coupling_fingers/2)

            # left
            cap_to_coupling_capacitor_rail_loc = -grid_spacing-arc_width*2-arc_gap-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)+cap_connector_adjust
            bottom_coupling_cap_rail_loc = capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+\
                  capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width/2
            top_coupling_cap_rail_loc = bottom_coupling_cap_rail_loc +length_of_coupling_fingers+coupling_capacitor_finger_end_gap+coupling_capacitor_rail_width

            if draw_left:
                cf.translate(f,ic.lookup('capacitor_to_coupling_capacitor_connector'),
                                 cap_to_coupling_capacitor_rail_loc-capacitor_rail_width/2,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap/2)
                if coupling_cap_loc == 'inner':
                    cf.translate(f,ic.lookup('coupling_capacitor_connector'),
                                     -feedline_width/2-coupler_connector_width/2-feedline_width/2+coupling_capacitor_rail_width-coupling_capacitor_finger_width*2,
                                     bottom_coupling_cap_rail_loc)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector'),
                                     -feedline_width/2-coupler_connector_width/2-feedline_width/2+coupling_capacitor_rail_width,
                                 top_coupling_cap_rail_loc)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_vertical'),-feedline_width/2+coupling_capacitor_rail_width/2-feedline_width/2,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+4*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+coupling_connector_length_vertical/2)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_inner'),
                                     cap_to_coupling_capacitor_rail_loc+coupling_capacitor_connector_inner_length/2-capacitor_rail_width,
                                 bottom_coupling_cap_rail_loc)

                else:
                    cf.translate(f,ic.lookup('coupling_capacitor_connector'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width/2+(2-n_arcs)*(arc_width+arc_gap)+cap_adjust,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width/2)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width/2+(2-n_arcs)*(arc_width+arc_gap)+cap_adjust,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+3*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_vertical'),-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width/2+(2-n_arcs)*(arc_width+arc_gap)+cap_vertical_adjust,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+4*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+coupling_connector_length_vertical/2)



            # right
            if draw_right:
                cf.translate(f,ic.lookup('capacitor_to_coupling_capacitor_connector'),
                                 -(cap_to_coupling_capacitor_rail_loc-capacitor_rail_width/2)+cap_connector_adjust,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap/2)
                if coupling_cap_loc == 'inner':
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_right'),
                                     -coupling_capacitor_rail_width+coupler_connector_width_right/2+coupling_capacitor_finger_width*2,
                                 bottom_coupling_cap_rail_loc)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_right'),
                                     -coupling_capacitor_rail_width+coupler_connector_width_right/2,
                                 top_coupling_cap_rail_loc)

                    cf.translate(f,ic.lookup('coupling_capacitor_connector_vertical'),
                                     feedline_width/2-coupling_capacitor_rail_width/2-feedline_width/2,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+4*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+coupling_connector_length_vertical/2)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_inner_right'),-(cap_to_coupling_capacitor_rail_loc+coupling_capacitor_connector_inner_length_right/2-capacitor_rail_width),
                                 bottom_coupling_cap_rail_loc)

                else:
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_right'),
                                     -(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width_right/2+(2-n_arcs)*(arc_width+arc_gap))-cap_adjust,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+coupling_capacitor_rail_width/2)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_right'),
                                     -(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-coupler_connector_width_right/2+(2-n_arcs)*(arc_width+arc_gap))-cap_adjust,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+3*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap)
                    cf.translate(f,ic.lookup('coupling_capacitor_connector_vertical'),
                                     -(-grid_spacing-arc_width*2-arc_gap-absorber_extension_length-capacitor_rail_width/2+(2-n_arcs)*(arc_width+arc_gap))-cap_vertical_adjust_right,
                                 capacitor_finger_overlap/2+capacitor_finger_end_gap+capacitor_rail_width+capacitor_offset_y+capacitor_to_coupling_capacitor_gap+4*coupling_capacitor_rail_width/2+length_of_coupling_fingers+coupling_capacitor_finger_end_gap+coupling_connector_length_vertical/2)



            cf.end_subset(f)

            if draw_bottom_coupling_cap:
                cf.start_subset(f,ic,subset_name = 'coupling_capacitor_mirror_y')
                cf.mirror_y(f,ic.lookup('coupling_capacitor'))
                cf.end_subset(f)
                cf.translate(f,ic.lookup('coupling_capacitor_mirror_y'),0,capacitor_offset_y*2)    



            cf.translate(f,ic.lookup('coupling_capacitor'),0,0)



        #####################################################################################
        #                        deep etch and other stuff
        #####################################################################################



            if coupling_cap_loc == 'inner':
                cf.translate(f,ic.lookup('inductor_trench'),0,capacitor_offset_y)
            else:
                cf.translate(f,ic.lookup('inductor_trench'),0,0)
            if draw_left:
                #mod by AH
                # cf.translate(f,ic.lookup('capacitor_trench'),
                #                  -(grid_spacing+arc_width*2+arc_gap+absorber_extension_length)-capacitor_trench_x/2,
                #                  +length_of_coupling_fingers/2+capacitor_rail_width+capacitor_offset_y+\
                #                  coupling_capacitor_finger_end_gap/2+capacitor_to_coupling_capacitor_gap/2)
                cf.translate(f,ic.lookup('capacitor_trench'),
                                  -grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap)-capacitor_trench_x/2,capacitor_offset_y)

            if draw_right:
                #mod by AH
                # cf.translate(f,ic.lookup('capacitor_trench_right'),
                #                  -(-(grid_spacing+arc_width*2+arc_gap+absorber_extension_length)-capacitor_trench_x_right/2),
                #                  +length_of_coupling_fingers/2+capacitor_rail_width+capacitor_offset_y+\
                #                  coupling_capacitor_finger_end_gap+capacitor_to_coupling_capacitor_gap/2)
                cf.translate(f,ic.lookup('capacitor_trench_right'),
                                 -( -grid_spacing-arc_width*2-arc_gap-capacitor_rail_width/2-absorber_extension_length+(2-n_arcs)*(arc_width+arc_gap))+capacitor_trench_x_right/2,capacitor_offset_y)

            cf.translate(f,ic.lookup('choke_radius'),0,0)
            cf.translate(f,ic.lookup('choke_inner_radius'),0,0)
            cf.translate(f,ic.lookup('guide_radius'),0,0)
            cf.translate(f,ic.lookup('inductor_border_etch'),0,capacitor_offset_y)
            cf.translate(f,ic.lookup('pixel_size'),0,0)
            #cf.translate(f,ic.lookup('inductor_border_etch_2'),0,5*microns)

            cf.translate(f,ic.lookup('feedline'),0,feedline_y_location)
            if vertical_feedline:
                cf.translate(f,ic.lookup('feedline_vertical'),pixel_size/2-feedline_width/2,0)

            if add_extra is not None:
                for i in range(0,len(add_extra)):
                    print("hello")
                    print(ic.id[add_extra[i]])
                    cf.translate(f,ic.id[add_extra[i]],0,0)





    cf.end_subset(f)
    if file_write_mode == "w":
        cf.end_file(f)
    f.close()

    #for key in ic.id:
        #print(ic.id[key],key)

    if ic != None:
        ic.appendix_name = ''
        return ic



if __name__ == "__main__":
    #filename = "multi-octave_polekid.cif"
    filename = "24-03-11_Random_Shorted_polekid.cif"
    main(filename)




