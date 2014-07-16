# -*- coding: utf-8 -*-
"""
#------------------------------------------------------------------------------
# Revised: 2014-07-04
# Authors: Mike Lowry
# Prerequiste: ArcGIS 10.1 and Python 2.7
# Copyright: 2012, Mike Lowry, mlowry@uidaho.edu
# Please cite: 
#   McDaniel, S., Lowry, M., and Dixon, M. (2014) “Using Origin-Destination Centrality 
#   to Estimate Directional Bicycle Volumes.” Transportation Research Record: Journal of the Transportation Research Board
# -----------------------------------------------------------------------------
"""

###################################
# Import Standard Libraries and Other Scripts
###################################
# Import arcpy and set environments
import arcpy
arcpy.env.overwriteOutput=True
# Import Standard Libraries
import sys, os, math
from collections import defaultdict

version = sys.version_info
pythonversion = str(version[0]) + "." + str(version[1])
if pythonversion <> '2.7': # This also means ArcGIS 10.1
    arcpy.AddError("This tool requires ArcGIS 10.1 with Python 2.7")
    sys.exit()




###############################################################################
# Get Relative Paths and Import Special Libraries
###############################################################################
ScriptPath = sys.path[0]
ToolDataPath = os.path.dirname(ScriptPath)
ScratchPath = os.path.join(ToolDataPath, "Scratch")
LibDataPath = os.path.join(ToolDataPath, "LibData")
FilesPath = os.path.join(ToolDataPath, "Files")
SymbologyPath = os.path.join(ToolDataPath, "Symbology")



###############################################################################
# Functions
###############################################################################


    

###############################################################################
# Start Algorithm
###############################################################################


if __name__ == '__main__':
    ###########################################################################
    # Get Input
    ###########################################################################
    inputNetwork = arcpy.GetParameterAsText(0) # Topologically correct network
    fieldattribute = arcpy.GetParameterAsText(1) # Must say exactly either "two_way" or "one_way"
    GUI=True
    if inputNetwork == "":
        GUI =False
        ToolFolderPath = "C:\\Users\\mlowry\\Dropbox\\Volume_Estimation_Tools"
        inputNetwork = ToolFolderPath + "\\ExampleData\\Input\\Testing\\smallstreets.shp" # Topologically correct network

        direction = "Direction"  

    ###########################################################################
    # Prepare Input
    ###########################################################################

    
    ## Check that points were correctly obtained through the GUI
    if GUI:
        arcpy.SelectLayerByAttribute_management(inputNetwork, "CLEAR_SELECTION", "")

    totalvalue = 0
    with arcpy.da.SearchCursor(inputNetwork, (fieldattribute)) as cursor:
        for row in cursor:
            totalvalue = totalvalue + row[0]
 
            
    arcpy.AddMessage(" ")        
    arcpy.AddMessage(totalvalue)
    arcpy.AddMessage(" ")   


