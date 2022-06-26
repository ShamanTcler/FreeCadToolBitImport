# -*- coding: utf-8 -*-
# ***************************************************************************
# *   Copyright (c) 2022 CandLWorkshop <candlworkshopllc@gmail.com>         *
# *                                                                         *  
# *    CandLWorkshop also known as ShamanTcler on Github                    *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENSE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import csv
import itertools
import sys
import os



def lower_first_line(iterator):
    ''' The function lower_first_line, lowercases the first line of a file
    '''
    return itertools.chain([next(iterator).lower()], iterator)

def convert_real_to_safe_string(val):
    ''' The function converts a number like 1.234 to 1_dp_234 that way it can be used in file names
    '''
    lcl_str=str(val)
    return lcl_str.replace(".", "_dp_")


def row_clean_up(row):
    ''' The function row_clean_up, replaces synonyms with well known values.
    '''
    if row['material'] == "SC":
        row['material']="HSS"
#        row['material']="CARBIDE"

    shape=row['shape'].lower()
    if shape == "ball nose spiral":
        row['shape']="ballend"
    return row


def write_endmill(row):
    ''' The function write_endmill writes an endmill JSON file
    '''
    bit_file_name= row['diameter'] + "_endmill_" \
        + row['vendor'] + "_"  +row['part number']

    #avoid decimal pts in filename
    bit_file_name=bit_file_name.replace("0.","zero_pt")

    bit_file_name=bit_file_name  + ".fctb"

    bit_file = open(bit_file_name,  mode="w", encoding="utf-8")
    bit_file.write("{\n")
    bit_file.write("  \"version\": 2,\n")
    bit_file.write("  \"name\": \""  +  row['diameter'] + " Endmill "  + row['vendor'] + " "  + row['part number'] + "\",\n" )
    bit_file.write("  \"shape\": \"endmill.fcstd\",\n")
    bit_file.write("  \"parameter\": {\n")
    bit_file.write("    \"Chipload\": \"" + row['chipload per flute'] +  " " + row['chipload per flute units'] + "\",\n")
    bit_file.write("    \"CuttingEdgeHeight\": \"" + row['cutting edge height'] + " \",\n")
    bit_file.write("    \"Diameter\": \"" + row['diameter'] + " " + row['diameter units'] + " \",\n")
    bit_file.write("    \"Flutes\": \"" + row['flutes'] + "\",\n")
    bit_file.write("    \"Length\": \"" + row['length'] + " " + row['length units'] + " \",\n")
    bit_file.write("    \"Material\": \"" + row['material'] + "\",\n")
    bit_file.write("    \"ShankDiameter\": \"" + row['shank diameter'] + " " + row['shank diameter units'] + " \"\n")
    bit_file.write("  },\n")
    bit_file.write("  \"attribute\": {\n")
    bit_file.write("    \"vendor\": \"" + row['vendor'] + "\"\n")
    bit_file.write("  }\n")
    bit_file.write("}\n")
    bit_file.close()
    return bit_file_name

def write_ballend(row):
    ''' The function write_ballend writes an ballend JSON file
    '''
    bit_file_name=row['diameter'] + "_ballend_" \
        + row['vendor'] + "_"  +row['part number']

    #avoid decimal pts in filename
    bit_file_name=bit_file_name.replace("0.","zero_pt")
            
    bit_file_name=bit_file_name  + ".fctb"
            


    bit_file = open(bit_file_name,  mode="w", encoding="utf-8")
    bit_file.write("{\n")
    bit_file.write("  \"version\": 2,\n")
    bit_file.write("  \"name\": \""    + row['diameter'] +  " Ball endmill " + row['vendor'] + " " + row['part number'] + "\",\n" )
    bit_file.write("  \"shape\": \"ballend.fcstd\",\n" )
    bit_file.write("  \"parameter\": {\n")
    bit_file.write("    \"Chipload\": \"" + row['chipload per flute'] +  " " + row['chipload per flute units'] + "\",\n")
    bit_file.write("    \"CuttingEdgeHeight\": \"" + row['cutting edge height'] +  " " + row['cutting edge height units'] + "\",\n")
    bit_file.write("    \"Diameter\": \"" + row['diameter'] + " " + row['diameter units'] + "\",\n")
    bit_file.write("    \"Flutes\": \"" + row['flutes'] + "\",\n")
    bit_file.write("    \"Length\": \"" + row['length'] + " " + row['length units'] + "\",\n")
    bit_file.write("    \"Material\": \"" + row['material'] + "\",\n")
    bit_file.write("    \"ShankDiameter\": \"" + row['shank diameter'] + " " + row['shank diameter units'] + "\"\n")
    bit_file.write("  },\n")
    bit_file.write("  \"attribute\": {\n")
    bit_file.write("    \"vendor\": \"" + row['vendor'] + "\"\n")
    bit_file.write("  }\n")
    bit_file.write("}\n")
    bit_file.close()
    return bit_file_name

def write_v_bit(row):
    ''' The function write_v_bit writes an Vbit JSON file
    '''
    bit_file_name= row['cutting edge angle'] + "deg_v_bit_" + row['vendor'] + "_"  +row['part number']

    #avoid decimal pts in filename
    bit_file_name=bit_file_name.replace("0.","zero_pt")

    bit_file_name=bit_file_name  + ".fctb"

    bit_file = open(bit_file_name,  mode="w", encoding="utf-8")
    bit_file.write("{\n")
    bit_file.write("  \"version\": 2,\n")
    bit_file.write("  \"name\": \"" + row['cutting edge angle'] + " deg v-bit " + row['vendor'] + " " + row['part number'] + "\",\n" )
    bit_file.write("  \"shape\": \"v-bit.fcstd\",\n" )
    bit_file.write("  \"parameter\": {\n")
    bit_file.write("    \"Chipload\": \"" + row['chipload per flute'] +  " " + row['chipload per flute units'] + "\",\n")
    bit_file.write("    \"CuttingEdgeHeight\": \"" + row['cutting edge height']  +  " " + row['cutting edge height units'] + " \",\n")
    bit_file.write("    \"CuttingEdgeAngle\": \"" + row['cutting edge angle'] + " \\u00b0\",\n")
    bit_file.write("    \"Diameter\": \"" + row['diameter'] + " " + row['diameter units'] + " \",\n")
    bit_file.write("    \"Flutes\": \"" + row['flutes'] + "\",\n")
    bit_file.write("    \"Length\": \"" + row['length'] + " " + row['length units'] + " \",\n")
    bit_file.write("    \"Material\": \"" + row['material'] + "\",\n")
    bit_file.write("    \"ShankDiameter\": \"" + row['shank diameter'] + " " + row['shank diameter units'] + " \"\n")
    bit_file.write("  },\n")
    bit_file.write("  \"attribute\": {\n")
    bit_file.write("    \"vendor\": \"" + row['vendor'] + "\"\n")
    bit_file.write("  }\n")
    bit_file.write("}\n")
    bit_file.close()
    return bit_file_name

def make_toolbit_kit(lib_name,csv_file_path):
    ''' The function make_toolbit takes in a filename for a CSV file describing
    tool bits. It parses each row a a single toolbit, writing each toolbit to a
    JSON file
    '''
    # lets create and set our directory structure
    path=os.getcwd()
    os_sep=os.sep
    tool_bits_path=path + os_sep + "ToolBits"
    bit_path=tool_bits_path + os_sep + "Bit"
    library_path=tool_bits_path +os_sep + "Library"
    shape_path=tool_bits_path + os_sep + "Shape"

    if not os.path.exists(tool_bits_path):
        os.makedirs(tool_bits_path)
    if not os.path.exists(bit_path):
        os.makedirs(bit_path)
    if not os.path.exists(library_path):
        os.makedirs(library_path)
    if not os.path.exists(shape_path):
        os.makedirs(shape_path)

    # create empty list of bit names
    bit_name_list=[]

    os.chdir(bit_path)

    with open(csv_file_path,  mode="r") as csv_file:
        # reading the csv file using DictReader,
        # get rid of case sensitive column names
        csv_reader = csv.DictReader(lower_first_line(csv_file))
        
        # Process the tool bits
        for row in csv_reader:
            bit_file_name="null"
            # Map some names to standard names            
            row=row_clean_up(row)
            shape=row['shape'].lower()
            if shape == "endmill":
                bit_file_name=write_endmill(row)
            elif shape == "ballend":
                bit_file_name=write_ballend(row)
            elif shape == "v-bit":
                bit_file_name=write_v_bit(row)
            else:
                print("Unable to process:\n")
                print(row)
                print("\n\n")

            if bit_file_name != "null":
                bit_name_list.append(bit_file_name)

    # Create the library        
    os.chdir(library_path)
    library_file_name=lib_name + ".fctl"
    lib_file = open(library_file_name,  mode="w", encoding="utf-8")
    lib_file.write("{\n")
    lib_file.write("  \"tools\": [\n")
        
    num_bits_written=len(bit_name_list)
    elem_num=1
    for bit_name in bit_name_list:
        lib_file.write("    {\n")
        lib_file.write("      \"nr\": " + str(elem_num) + ",\n")
        lib_file.write("      \"path\": \"" + bit_name + "\"\n")
        if elem_num < num_bits_written:
            lib_file.write("    },\n")
        else:
            lib_file.write("    }\n")
        elem_num=elem_num + 1

    lib_file.write("  ],\n")
    lib_file.write("  \"version\": 1\n")
    lib_file.write("}\n")
    lib_file.close

# Driver Code
''' This application reads a CSV file containing tool bit information for the 
FreeCad Path workbench. Please reference web page: 
for file details.

Each row defines a single bit and will create a single JSON file.
'''
# For command line operation, un-comment "command line block"
# Start command line block

#if len(sys.argv) != 2 :
#    print("usage: python python create_freecad_bit.py file_name.csv")
#    print("where file_name.csv is the name of the file to be converted")
#    sys.exit()
#csv_file_path = sys.argv[1]

# End command line block


lib_name="Whiteside"

lcl_path=os.getcwd()
os_sep=os.sep
csv_file_path=lcl_path + os_sep + "test" + os_sep + "test2.csv"

# Call the make_toolbit function
make_toolbit_kit(lib_name,csv_file_path)
