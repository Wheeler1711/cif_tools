import numpy as np
import matplotlib.pyplot as plt
#from cif_tools import cif_functions as cf
#from cif_tools import draw_polekid
from datetime import date
import cif_functions as cf
import os
#import draw_polekid_two_octave
import draw_polekid

today = date.today()
formatted_date = today.strftime('%y-%m-%d')

ic = cf.index_dictionary()
microns = 100
nanometers = 0.1
capacitor_layer = [4,5]

shorted = True

Trial = "low_volume_Qc_20000"


#if shorted: label = formatted_date+"_"+Trial+"_Shorted"
#else: label = formatted_date+"_"+Trial+"_Unshorted"
label = "low volume\nQc = 20,000"
filename = Trial + ".cif"


if filename in os.listdir():
    os.remove(filename)
f = open(filename, "a")

#ic.appendix_name = chip_name

#Mod by AH
'''
for i in range(11):
    if shorted:
        draw_polekid_two_octave.main(filename,
            file_write_mode ="a", #w is new file, a is append to file
            pixel_name = "polekid_"+str(i),
            index_offset = 0,
            draw_entire_pixel = True,
            draw_left = True,
            draw_right = True,
            meander_inside = False,
            n_lines = 4,#, #must be multiple of 4
            arc_width = int(1100*nanometers),#int(800*nanometers),
            arc_width_right = int(1100*nanometers),#int(800*nanometers),
            arc_gap = int(1.1*microns),
            n_arcs = 4,#6,# default = 4 must be multiple of 4
            absorber_extension_length = 3*microns,
            grid_spacing = int(250*microns), #ums ABSLength in excel
            line_width = int(800*nanometers),#int(800*nanometers), # 0.8 um
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
            pol_angle = (i % 2)*45,#-15,
            short_width = int(1000*nanometers),#int(1200*nanometers),
            short_centers_x = np.linspace(-110,110,55)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
            short_lengths_x = np.round(np.ones(55,dtype = int)*3*microns),#np.round(np.ones(41,dtype = int)*5*microns),
            short_centers_y = np.hstack((np.linspace(-110,-10,25),np.linspace(10,110,25)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
            short_lengths_y = np.round(np.ones(50,dtype = int)*3*microns),#np.round(np.ones(36,dtype = int)*5*microns),
            aluminum_left = True,
            aluminum_right = True,
            ic = ic)#[], # leave as [] for no shorts):
            
    else:
        draw_polekid.main(filename,
            file_write_mode ="w", #w is new file, a is append to file
            pixel_name = "polekid_"+str(i),
            index_offset = 0,
            draw_entire_pixel = True,
            draw_left = True,
            draw_right = True,
            meander_inside = False,
            n_lines = 4,#, #must be multiple of 4
            arc_width = int(1100*nanometers),#int(800*nanometers),
            arc_width_right = int(1100*nanometers),#int(800*nanometers),
            arc_gap = int(1.1*microns),
            n_arcs = 4,#6,# default = 4 must be multiple of 4
            absorber_extension_length = 3*microns,
            grid_spacing = int(250*microns), #ums ABSLength in excel
            line_width = int(800*nanometers),#int(800*nanometers), # 0.8 um
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
            pol_angle = (i % 2)*45,#-15,
            short_width = int(1000*nanometers),#int(1200*nanometers),
            short_centers_x = np.linspace(-110,110,55)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
            short_lengths_x = np.round(np.ones(55,dtype = int)*3*microns),#np.round(np.ones(41,dtype = int)*5*microns),
            short_centers_y = np.hstack((np.linspace(-110,-10,25),np.linspace(10,110,25)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
            short_lengths_y = np.round(np.ones(50,dtype = int)*3*microns),#np.round(np.ones(36,dtype = int)*5*microns),
            aluminum_left = True,
            aluminum_right = True,
            ic = ic)#[], # leave as [] for no shorts):  
            

'''

###########################################################
#           2 lines 0.7 ums 75 % aluminum 11.4 nH
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_0p7um_wide_lines",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(5000*nanometers),#int(800*nanometers),
    arc_width_right = int(5000*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(700*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(1400*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 63,#25,
    number_of_fingers_right = 63,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 66,#20,
    number_of_coupling_fingers_right = 66,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 4,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1200*nanometers),#int(1200*nanometers),
    short_centers_x = np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = np.round(np.ones(69,dtype = int)*5.25*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
    short_lengths_y = np.round(np.ones(70,dtype = int)*5.25*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):

###########################################################
#           2 lines 0.7 ums 75 % aluminum 11.4 nH dark
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_0p7um_wide_lines_dark",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(5000*nanometers),#int(800*nanometers),
    arc_width_right = int(5000*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(700*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(1400*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 75,#25,
    number_of_fingers_right = 75,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 57,#20,
    number_of_coupling_fingers_right = 57,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 4,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1200*nanometers),#int(1200*nanometers),
    short_centers_x = np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = np.round(np.ones(69,dtype = int)*5.25*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
    short_lengths_y = np.round(np.ones(70,dtype = int)*5.25*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):



###########################################################
#           2 lines 1.4 ums 50 % aluminum 11.4 nH
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_1p4um_wide_lines",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(5000*nanometers),#int(800*nanometers),
    arc_width_right = int(5000*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
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
    number_of_fingers = 60,#25,
    number_of_fingers_right = 60,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 62,#20,
    number_of_coupling_fingers_right = 62,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 4,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1900*nanometers),#int(1200*nanometers),
    short_centers_x = np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
    short_lengths_y = np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):

###########################################################
#           2 lines 1.4 ums 50 % aluminum 11.4 nH dark
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_1p4um_wide_lines_dark",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(5000*nanometers),#int(800*nanometers),
    arc_width_right = int(5000*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
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
    number_of_fingers = 21,#25,
    number_of_fingers_right = 21,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 21,#20,
    number_of_coupling_fingers_right = 21,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 4,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1900*nanometers),#int(1200*nanometers),
    short_centers_x = np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
    short_lengths_y = np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):

###########################################################
#           2 lines 2.8 ums 0 % aluminum 11.4 nH
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_2p8um_wide_lines",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(5000*nanometers),#int(800*nanometers),
    arc_width_right = int(5000*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(2800*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(1400*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 47,#25,
    number_of_fingers_right = 47,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 49,#20,
    number_of_coupling_fingers_right = 49,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 4,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(3300*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):


###########################################################
#           2 lines 2.8 ums 0 % aluminum 11.4 nH + TiN arcs
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_2p8um_wide_lines_TiN_arcs",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = False,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(2800*nanometers),#int(800*nanometers),
    arc_width_right = int(2800*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(2800*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(2800*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 14,#25,
    number_of_fingers_right = 14,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 25,#20,
    number_of_coupling_fingers_right = 25,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(3300*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):

###########################################################
#           2 lines 2.8 ums 0 % aluminum 11.4 nH + TiN arcs dark
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_2p8um_wide_lines_TiN_arcs_dark",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = False,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(2800*nanometers),#int(800*nanometers),
    arc_width_right = int(2800*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(2800*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(2800*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 45,#25,
    number_of_fingers_right = 45,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 80,#20,
    number_of_coupling_fingers_right = 80,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(3300*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):


###########################################################
#           4 lines 1.4 ums 0 % aluminum 11.4 nH + TiN arcs
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "4_1p4um_wide_lines_TiN_arcs",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = False,
    draw_right = True,
    meander_inside = False,
    n_lines = 4,#, #must be multiple of 4
    n_lines_shorted = 2,#r of 2?
    arc_width = int(1400*nanometers),#int(800*nanometers),
    arc_width_right = int(1400*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 4,#6,# default = 2 must be multiple of n_lines?
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
    number_of_fingers = 13,#25,
    number_of_fingers_right = 13,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 23,#20,
    number_of_coupling_fingers_right = 23,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1900*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):

###########################################################
#           4 lines 1.4 ums 0 % aluminum 11.4 nH + TiN arcs
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "4_1p4um_wide_lines_TiN_arcs_dark",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = False,
    draw_right = True,
    meander_inside = False,
    n_lines = 4,#, #must be multiple of 4
    n_lines_shorted = 2,#r of 2?
    arc_width = int(1400*nanometers),#int(800*nanometers),
    arc_width_right = int(1400*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 4,#6,# default = 2 must be multiple of n_lines?
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
    number_of_fingers = 50,#25,
    number_of_fingers_right = 50,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 88,#20,
    number_of_coupling_fingers_right = 88,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1900*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):



###########################################################
#           4 lines 0.7 ums 50 % aluminum 45 nH
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "4_0p7um_wide_lines",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 4,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(5000*nanometers),#int(800*nanometers),
    arc_width_right = int(5000*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(700*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(1400*nanometers),
    between_pol_gap = int(2000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 14,#25,
    number_of_fingers_right = 14,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
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
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 4,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1200*nanometers),#int(1200*nanometers),
    short_centers_x = np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
    short_lengths_y = np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):


###########################################################
#           4 lines 1.4 ums 0 % aluminum 24 nH
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "4_1p4um_wide_lines",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 4,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = True,
    meander_inside = False,
    n_lines = 4,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(5000*nanometers),#int(800*nanometers),
    arc_width_right = int(5000*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 2,#6,# default = 2 must be multiple of n_lines?
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
    number_of_fingers = 20,#25,
    number_of_fingers_right = 20,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
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
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 4,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1900*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*5.25*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,#np.hstack((np.linspace(-200,-20,18,dtype = int),np.linspace(20,200,18,dtype = int)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*5.25*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):



###########################################################
#           2 lines 2.8 ums 0 % aluminum 11.4 nH + 4 TiN arcs
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_2p8um_wide_lines_4_TiN_arcs",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 6,
    draw_entire_pixel = True,
    draw_left = False,
    draw_right = True,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(2800*nanometers),#int(800*nanometers),
    arc_width_right = int(2800*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 4,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(2800*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(2800*nanometers),
    between_pol_gap = int(3000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 7,#25,
    number_of_fingers_right = 7,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 19,#20,
    number_of_coupling_fingers_right = 19,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(3300*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):

###########################################################
#           2 lines 2.8 ums 0 % aluminum 11.4 nH + 4 TiN arcs
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "2_2p8um_wide_lines_4_TiN_arcs_dark",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 6,
    draw_entire_pixel = True,
    draw_left = False,
    draw_right = True,
    meander_inside = False,
    n_lines = 2,#, #must be multiple of 4
    n_lines_shorted = 1,#r of 2?
    arc_width = int(2800*nanometers),#int(800*nanometers),
    arc_width_right = int(2800*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 4,#6,# default = 2 must be multiple of n_lines?
    absorber_extension_length = 3*microns,
    grid_spacing = int(250*microns), #ums ABSLength in excel
    line_width = int(2800*nanometers),#int(800*nanometers), # 0.8 um
    separation_x_pol = int(1400*nanometers),
    separation_y_pol = int(2800*nanometers),
    between_pol_gap = int(3000*nanometers),
    meander_length = int(7000*nanometers),
    meander_height = int(1200*nanometers), #1200
    capacitor_rail_width = int(10*microns),
    coupling_capacitor_rail_width = int(10*microns),
    number_of_fingers = 35,#25,
    number_of_fingers_right = 35,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 60,#20,
    number_of_coupling_fingers_right = 60,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(3300*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):


###########################################################
#           4 lines 1.4 ums 0 % aluminum 11.4 nH + TiN arcs
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "4_1p4um_wide_lines_8_TiN_arcs",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 6,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = False,
    meander_inside = False,
    n_lines = 4,#, #must be multiple of 4
    n_lines_shorted = 2,#r of 2?
    arc_width = int(1400*nanometers),#int(800*nanometers),
    arc_width_right = int(1400*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 8,#6,# default = 2 must be multiple of n_lines?
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
    number_of_fingers = 6,#25,
    number_of_fingers_right = 6,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 16,#20,
    number_of_coupling_fingers_right = 16,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1900*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):


###########################################################
#           4 lines 1.4 ums 0 % aluminum 11.4 nH + TiN arcs
###########################################################

draw_polekid.main(filename,
    file_write_mode ="a", #w is new file, a is append to file
    pixel_name = "4_1p4um_wide_lines_8_TiN_arcs_dark",
    index_offset = 0,
    L_per_square = 32, #pH
    L_geometric = 6,
    draw_entire_pixel = True,
    draw_left = True,
    draw_right = False,
    meander_inside = False,
    n_lines = 4,#, #must be multiple of 4
    n_lines_shorted = 2,#r of 2?
    arc_width = int(1400*nanometers),#int(800*nanometers),
    arc_width_right = int(1400*nanometers),#int(800*nanometers),
    arc_gap = int(1.4*microns),
    n_arcs = 8,#6,# default = 2 must be multiple of n_lines?
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
    number_of_fingers = 40,#25,
    number_of_fingers_right = 40,#12,#15,
    capacitor_finger_overlap = 1500*microns,
    capacitor_finger_end_gap = 12*microns,#5*microns,
    capacitor_offset_y = -400*microns,
    capacitor_finger_width = 4*microns,#5*microns, #7 microns with meanders 6 without  #now 5 and 4
    capacitor_finger_width_right = 6*microns,#8*microns, #7 microns with meanders 6 without  #now 5 and 4
    coupling_capacitor_finger_width = 5*microns,#5*microns,
    coupling_capacitor_finger_width_right = 5*microns,
    capacitor_to_coupling_capacitor_gap = 25*microns,
    number_of_coupling_fingers = 80,#20,
    number_of_coupling_fingers_right = 80,
    coupling_finger_overlap = 40*microns,
    coupling_capacitor_finger_end_gap = 5*microns,
    capacitor_finger_start_gap = int(50*microns),
    liftoff_gap_size = 20*microns,
    remove_capacitor_finger_fraction = 0.0,
    remove_capacitor_finger_fraction_right = 0.0,
    feedline_y_location = 599*microns,
    feedline_width = 45*microns,
    pixel_size = 1400*microns,
    capacitor_layer = [4,5],
    short_layer = 4,
    liftoff_layer = [4,5],
    inductor_layer = 5,
    arc_layer = 5,
    remove_finger_number = 0,
    remove_finger_number_right = 0,
    pol_angle = 0,
    short_width = int(1900*nanometers),#int(1200*nanometers),
    short_centers_x = [],#np.linspace(-240,240,69)*microns,#np.linspace(-200,200,41,dtype = int)*microns,#[], # leave as [] for no shorts
    short_lengths_x = [],#np.round(np.ones(69,dtype = int)*3.9*microns),#np.round(np.ones(41,dtype = int)*5*microns),
    short_centers_y = [],#np.hstack((np.linspace(-245,-8,35),np.linspace(8,245,35)))*microns,
    short_lengths_y = [],#np.round(np.ones(70,dtype = int)*3.9*microns),#np.round(np.ones(36,dtype = int)*5*microns),
    aluminum_left = True,
    aluminum_right = True,
    ic = ic)#[], # leave as [] for no shorts):





f = open(filename, "a")
offset = int(2800*np.sqrt(3)*microns/2/2)
print(offset)



cf.draw_rectangle(f,ic,10*1000*microns,10*1000*microns,layer = 7,scale_num = 1,name= 'test_chip_border') #

# Modified transmission line thickness and added third line. Microstrips 4 and 5 are pads for wirebonding
transmission_line_thickness = 45
for i in range(0,len(capacitor_layer)):
    cf.draw_wire(f,ic,transmission_line_thickness*microns,[-4020*microns,-4020*microns,-3920*microns,3920*microns,4020*microns],[-1725*microns,499*microns,599*microns,599*microns,699*microns],layer = capacitor_layer[i],scale_num = 1,name= 'microstrip_1_'+str(i)) #
    cf.draw_wire(f,ic,transmission_line_thickness*microns,[-4020*microns,-3920*microns,4020*microns,4740*microns],[-1725*microns,-1825*microns,-1825*microns,-0*microns],layer = capacitor_layer[i],scale_num = 1,name= 'microstrip_2_'+str(i)) #
    cf.draw_wire(f,ic,transmission_line_thickness*microns,[-4740*microns,-4120*microns,-4020*microns,3920*microns,4020*microns,4020*microns],[0*microns,2925*microns,3025*microns,3025*microns,2925*microns,699*microns],layer = capacitor_layer[i],scale_num = 1,name= 'microstrip_3_'+str(i)) #
    cf.draw_wire(f,ic,400*microns,[-4700*microns,-4700*microns],[0*microns,0*microns],layer = capacitor_layer[i],scale_num = 1,name= 'microstrip_4_'+str(i)) #
    cf.draw_wire(f,ic,400*microns,[4700*microns,4700*microns],[0*microns,0*microns],layer = capacitor_layer[i],scale_num = 1,name= 'microstrip_5_'+str(i)) #


#cf.draw_rectangle(f,ic,100*microns,400*microns,layer = 8,scale_num = 1,name= 'indicator_mark') #
cf.draw_rectangle(f,ic,200*microns,600*microns,layer = 8,scale_num = 1,name= 'border_vertical') #
cf.draw_rectangle(f,ic,600*microns,200*microns,layer = 8,scale_num = 1,name= 'border_horizontal') #
cf.draw_rectangle(f,ic,1000*microns,1000*microns,layer = 5,scale_num = 1,name= 'dc_bond_pad') #
cf.draw_rectangle(f,ic,1000*microns,10*microns,layer = 5,scale_num = 1,name= 'dc_test_wire') #
cf.draw_rectangle(f,ic,1000*microns,1000*microns,layer = 13,scale_num = 1,name= 'dc_bond_pad_aluminum_cap') #
cf.draw_rectangle(f,ic,1000*microns,10*microns,layer = 13,scale_num = 1,name= 'dc_test_wire_aluminum_cap') #
#cf.draw_rectangle(f,100008,400*microns,400*microns,layer = 9,scale_num = 1,name= 'via_microstrip') #
#cf.draw_rectangle(f,100009,900*microns,900*microns,layer = 9,scale_num = 1,name= 'via_dc_bond_pad') #


#mod by AH
cf.draw_rectangle(f,ic,2000*microns,1000*microns,layer = 12,scale_num = 1,name= 'gold_pad') #
#cf.draw_rectangle(f,ic,10000*microns,1000*microns,layer = 12,scale_num = 1,name= 'gold_strip') #
#cf.draw_rectangle(f,ic,200*microns,200*microns,layer = 12,scale_num = 1,name= 'gold_for_bonding') #

#modded by AH
cf.draw_text(f, ic, label, pixel_size = 2500, layer = 12,scale_num = 1,name='label')

#Modded by AH, added third microstrip
cf.start_subset(f,ic,subset_name ="TOP")

for i in range(0,len(capacitor_layer)):
    cf.translate(f,ic.id['microstrip_1_'+str(i)],0,0)
    cf.translate(f,ic.id['microstrip_2_'+str(i)],0,0)
    cf.translate(f,ic.id['microstrip_3_'+str(i)],0,0)
    cf.translate(f,ic.id['microstrip_4_'+str(i)],0,0)
    cf.translate(f,ic.id['microstrip_5_'+str(i)],0,0)
cf.translate(f,ic.id['test_chip_border'],0,0)



# border marks
cf.translate(f,ic.id['border_vertical'],(-5000+100)*microns,(5000-300)*microns)
cf.translate(f,ic.id['border_horizontal'],(-5000+300)*microns,(5000-100)*microns)

cf.translate(f,ic.id['border_vertical'],(-5000+100)*microns,-(5000-300)*microns)
cf.translate(f,ic.id['border_horizontal'],(-5000+300)*microns,-(5000-100)*microns)

cf.translate(f,ic.id['border_vertical'],-(-5000+100)*microns,(5000-300)*microns)
cf.translate(f,ic.id['border_horizontal'],-(-5000+300)*microns,(5000-100)*microns)

cf.translate(f,ic.id['border_vertical'],-(-5000+100)*microns,-(5000-300)*microns)
cf.translate(f,ic.id['border_horizontal'],-(-5000+300)*microns,-(5000-100)*microns)


#dc test structure
cf.translate(f,ic.id['dc_bond_pad'],(-1000+0)*microns,4000*microns)
cf.translate(f,ic.id['dc_bond_pad'],(1000+0)*microns,4000*microns)
#cf.translate(f,100009,(-1000+0)*microns,4000*microns)
#cf.translate(f,100009,(1000+0)*microns,4000*microns)
cf.translate(f,ic.id['dc_test_wire'],0*microns,4000*microns)

#mod by AH
cf.translate(f,ic.id['dc_bond_pad'],(-1000+0)*microns,-4400*microns)
cf.translate(f,ic.id['dc_bond_pad'],(1000+0)*microns,-4400*microns)
#cf.translate(f,100009,(-1000+0)*microns,4000*microns)
#cf.translate(f,100009,(1000+0)*microns,4000*microns)
cf.translate(f,ic.id['dc_test_wire'],0*microns,-4400*microns)


#cf.translate(f,ic.id['dc_bond_pad_aluminum_cap'],(-1000+0)*microns,-4000*microns)
#cf.translate(f,ic.id['dc_bond_pad_aluminum_cap'],(1000+0)*microns,-4000*microns)
cf.translate(f,ic.id['dc_test_wire_aluminum_cap'],0*microns,-4400*microns)

#end dc test structure

#mod by AH, gold pads
cf.translate(f,ic.id['gold_pad'],(-3000)*microns,4450*microns)
cf.translate(f,ic.id['gold_pad'],3000*microns,4450*microns)
#cf.translate(f,ic.id['gold_strip'],0*microns,-4500*microns)
cf.translate(f,ic.id['gold_pad'],(-3000)*microns,-4450*microns)
cf.translate(f,ic.id['gold_pad'],3000*microns,-4450*microns)


#optical pixels
cf.translate(f,ic.id['2_1p4um_wide_lines'],-2500*microns,0) #middle left optical
cf.translate(f,ic.id['2_0p7um_wide_lines'],0,0) #middle
cf.translate(f,ic.id['2_2p8um_wide_lines'],2500*microns,0) #middle right optical
cf.translate(f,ic.id['2_2p8um_wide_lines_TiN_arcs'],1250*microns,offset*2) #top middle opticxal
cf.translate(f,ic.id['4_1p4um_wide_lines_TiN_arcs'],1250*microns,offset*2) #top middle opticxal
cf.translate(f,ic.id['4_0p7um_wide_lines'],-1250*microns,offset*2) # top left optical
cf.translate(f,ic.id['4_1p4um_wide_lines'],-1250*microns,-offset*2) # bottom left
cf.translate(f,ic.id['2_2p8um_wide_lines_4_TiN_arcs'],1250*microns,-offset*2) # bottom right
cf.translate(f,ic.id['4_1p4um_wide_lines_8_TiN_arcs'],1250*microns,-offset*2) # bottom right

cf.translate(f,ic.id['2_0p7um_wide_lines_dark'],3000*microns,-offset*2) #middle
cf.translate(f,ic.id['2_1p4um_wide_lines_dark'],-3000*microns,-offset*2) #middle

cf.translate(f,ic.id['2_2p8um_wide_lines_TiN_arcs_dark'],-3000*microns,offset*2) #middle
cf.translate(f,ic.id['4_1p4um_wide_lines_TiN_arcs_dark'],-3000*microns,offset*2) #middle

cf.translate(f,ic.id['2_2p8um_wide_lines_4_TiN_arcs_dark'],3000*microns,offset*2) #middle
cf.translate(f,ic.id['4_1p4um_wide_lines_8_TiN_arcs_dark'],3000*microns,offset*2) #middle



#optical pixels Modded by AH
'''
cf.translate(f,ic.id['polekid_0'],-2800*microns,0) #middle left optical
cf.translate(f,ic.id['polekid_1'],0,0) #middle
cf.translate(f,ic.id['polekid_2'],2800*microns,0) #middle right optical
cf.translate(f,ic.id['polekid_3'],1400*microns,offset*2) #top middle opticxal
cf.translate(f,ic.id['polekid_4'],-1400*microns,offset*2) # top left optical
cf.translate(f,ic.id['polekid_5'],-1400*microns,-offset*2) # bottom left
cf.translate(f,ic.id['polekid_6'],1400*microns,-offset*2) # bottom right

#dark pixels
#dark pixels Modded by AH
cf.translate(f,ic.id['polekid_7'],-3200*microns,offset*2) # top left dark
cf.translate(f,ic.id['polekid_8'],3200*microns,offset*2) # top left dark
cf.translate(f,ic.id['polekid_9'],-3200*microns,-offset*2) # bottom left dark
cf.translate(f,ic.id['polekid_10'],2800*microns,-offset*2) # bottom right dark
'''        
        
cf.translate(f,ic.id['label'],-4000*microns,3700*microns) # input label
        
        
cf.end_subset(f)

cf.end_file(f)

f.close()
