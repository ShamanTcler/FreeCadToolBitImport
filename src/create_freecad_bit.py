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



def lower_first_line(iterator):
    ''' The function lower_first_line, lowercases the first line of a file
    '''
    return itertools.chain([next(iterator).lower()], iterator)

def row_clean_up(row):
    ''' The function row_clean_up, replaces synonyms with well known values.
    '''
    if row['material'] == "SC":
        row['material']="CARBIDE"

    shape=row['shape'].lower()
    if shape == "ball nose spiral":
        row['shape']="ballend"
    return row


def write_endmill(row):
    ''' The function write_endmill writes an endmill JSON file
    '''
    bit_file_name=row['part number'] + "_endmill.ftcb"
    bit_file = open(bit_file_name,  mode="w", encoding="utf-8")
    bit_file.write("{\n")
    bit_file.write("  \"version\": 2,\",\n")
    bit_file.write("  \"name\": \""  + row['part number'] + "\",\n" )
    bit_file.write("  \"shape\": \"endmill.fcstd\",\n")
    bit_file.write("  \"parameter\": {\n")
    bit_file.write("    \"Chipload\": \"" + row['chipload per flute'] + " in\",\n")
    bit_file.write("    \"CuttingEdgeHeight\": \"" + row['cutting edge height'] + " \\\"\",\n")
    bit_file.write("    \"Diameter\": \"" + row['diameter'] + " \\\"\",\n")
    bit_file.write("    \"Flutes\": \"" + row['flutes'] + "\",\n")
    bit_file.write("    \"Length\": \"" + row['length'] + " \\\"\",\n")
    bit_file.write("    \"Material\": \"" + row['material'] + "\",\n")
    bit_file.write("    \"ShankDiameter\": \"" + row['shank diameter'] + " \\\"\",\n")
    bit_file.write("  }\n")
    bit_file.write("  \"attribute\": {\n")
    bit_file.write("    \"vendor\": \"" + row['vendor'] + "\",\n")
    bit_file.write("  }\n")
    bit_file.write("}\n")
    bit_file.close()

def write_ballend(row):
    ''' The function write_ballend writes an ballend JSON file
    '''
    bit_file_name=row['part number'] + "_ballend.ftcb"
    bit_file = open(bit_file_name,  mode="w", encoding="utf-8")
    bit_file.write("{\n")
    bit_file.write("  \"version\": 2,\",\n")
    bit_file.write("  \"name\": \""  + row['part number'] + "\",\n" )
    bit_file.write("  \"shape\": \"ballend.fcstd\",\n" )
    bit_file.write("  \"parameter\": {\n")
    bit_file.write("    \"Chipload\": \"" + row['chipload per flute'] + " in\",\n")
    bit_file.write("    \"CuttingEdgeHeight\": \"" + row['cutting edge height'] + " \\\"\",\n")
    bit_file.write("    \"Diameter\": \"" + row['diameter'] + " \\\"\",\n")
    bit_file.write("    \"Flutes\": \"" + row['flutes'] + "\",\n")
    bit_file.write("    \"Length\": \"" + row['length'] + " \\\"\",\n")
    bit_file.write("    \"Material\": \"" + row['material'] + "\",\n")
    bit_file.write("    \"ShankDiameter\": \"" + row['shank diameter'] + " \\\"\",\n")
    bit_file.write("  }\n")
    bit_file.write("  \"attribute\": {\n")
    bit_file.write("    \"vendor\": \"" + row['vendor'] + "\",\n")
    bit_file.write("  }\n")
    bit_file.write("}\n")
    bit_file.close()


def write_v_bit(row):
    ''' The function write_v_bit writes an Vbit JSON file
    '''
    bit_file_name=row['part number'] + "_v_bit.ftcb"
    bit_file = open(bit_file_name,  mode="w", encoding="utf-8")
    bit_file.write("{\n")
    bit_file.write("  \"version\": 2,\",\n")
    bit_file.write("  \"name\": \""  + row['part number'] + "\",\n" )
    bit_file.write("  \"shape\": \"v-bit.fcstd\",\n" )
    bit_file.write("  \"parameter\": {\n")
    bit_file.write("    \"Chipload\": \"" + row['chipload per flute'] + " in\",\n")
    bit_file.write("    \"CuttingEdgeHeight\": \"" + row['cutting edge height'] + " \\\"\",\n")
    bit_file.write("    \"CuttingEdgeAngle\": \"" + row['cutting edge angle'] + " \\u00b0\",\n")
    bit_file.write("    \"Diameter\": \"" + row['diameter'] + " \\\"\",\n")
    bit_file.write("    \"Flutes\": \"" + row['flutes'] + "\",\n")
    bit_file.write("    \"Length\": \"" + row['length'] + " \\\"\",\n")
    bit_file.write("    \"Material\": \"" + row['material'] + "\",\n")
    bit_file.write("    \"ShankDiameter\": \"" + row['shank diameter'] + " \\\"\",\n")
    bit_file.write("  }\n")
    bit_file.write("  \"attribute\": {\n")
    bit_file.write("    \"vendor\": \"" + row['vendor'] + "\",\n")
    bit_file.write("  }\n")
    bit_file.write("}\n")
    bit_file.close()


def make_toolbit(csv_file_path):
    ''' The function make_toolbit takes in a filename for a CSV file describing
    tool bits. It parses each row a a single toolbit, writing each toolbit to a
    JSON file
    '''
    with open(csv_file_path,  mode="r") as csv_file:
        # reading the csv file using DictReader,
        # get rid of case sensitive column names
        csv_reader = csv.DictReader(lower_first_line(csv_file)) 

        for row in csv_reader:
            # Map some names to standard names            
            row=row_clean_up(row)
            shape=row['shape'].lower()
            if shape == "endmill":
                write_endmill(row)
            elif shape == "ballend":
                write_ballend(row)
            elif shape == "v-bit":
                write_v_bit(row)
            else:
                print("Unable to process:\n")
                print(row)
                print("\n\n")

# Driver Code
''' This application reads a CSV file containing tool bit information for the 
FreeCad Path workbench. Please reference web page: 
for file details.

Each row defines a single bit and will create a single JSON file.
'''
# For command line operation, un-comment "command line block"
# Start command line block

if len(sys.argv) != 2 :
    print("usage: python python create_freecad_bit.py file_name.csv")
    print("where file_name.csv is the name of the file to be converted")
    sys.exit()
csv_file_path = sys.argv[1]

# End command line block



#csv_file_path="test2.csv"

# Call the make_toolbit function
make_toolbit(csv_file_path)
