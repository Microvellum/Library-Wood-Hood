"""
Microvellum 
Appliances 
Stores all of the Logic, Product, and Insert Class definitions for appliances
"""

import os
from mv import fd_types, unit
from . import appliance_classes

RANGE_HOOD_COVERS_PATH = os.path.join(os.path.dirname(__file__),"Range Hood Covers")

#---------PRODUCT: RANGE HOOD COVERS
        
class PRODUCT_ARA_6336(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "ARA-6336"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"ARA-6336.blend")
        self.height_above_floor = unit.inch (75)
class PRODUCT_B_6042(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "B-6042"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"B-6042.blend")
        self.height_above_floor = unit.inch (75)
class PRODUCT_BDP1_5442(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "BDP1-5442"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"BDP1-5442.blend")
        self.height_above_floor = unit.inch (75)        
class PRODUCT_E_3642(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "E-3642"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"E-3642.blend")
        self.height_above_floor = unit.inch (75)
                
class PRODUCT_ERA_4842(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "ERA-4842"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"ERA-4842.blend")
        self.height_above_floor = unit.inch (75)
                
class PRODUCT_G_3630(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "G-3630"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"G-3630.blend")
        self.height_above_floor = unit.inch (75)
                
class PRODUCT_G_4230(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "G-4230"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"G-4230.blend")
        self.height_above_floor = unit.inch (75)                                                                
        
        
class PRODUCT_GBT_6030(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "GBT-6030"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"GBT-6030.blend")
        self.height_above_floor = unit.inch (75)                                                                
        
class PRODUCT_H2RA_6032SHS(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "H2RA-6032SHS"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"H2RA-6032SHS.blend")
        self.height_above_floor = unit.inch (35.50)                                                                
        
class PRODUCT_M_4242(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "M-4242"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"M-4242.blend")
        self.height_above_floor = (75)                                                                
        
class PRODUCT_O_9060(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "O-9060"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"O-9060.blend")
        self.height_above_floor = unit.inch (35.50)                                                                
        
class PRODUCT_QART_5436(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "QART-5436"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"QART-5436.blend")
        self.height_above_floor = unit.inch (75)                                                                
        
class PRODUCT_U_9044(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "U-9044"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"U-9044.blend")
        self.height_above_floor = unit.inch (75)                                                                
        
class PRODUCT_U_9044SHS(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "U-9044SHS"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"U-9044SHS.blend")
        self.height_above_floor = unit.inch (75)                                                                
        
class PRODUCT_VCHIM_4842(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "VCHIM-4842"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"VCHIM-4842.blend")
        self.height_above_floor = unit.inch (75)                                                                
        
class PRODUCT_W_9072(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "W-9072"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"W-9072.blend")
        self.height_above_floor = unit.inch (35.50)                                                                
        
class PRODUCT_WRA_8484(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "WRA-8484"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"WRA-8484.blend")
        self.height_above_floor = unit.inch (35.50)                                                                
        
class PRODUCT_XRA_4224(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "XRA-4224"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"XRA-4224.blend")
        self.height_above_floor = unit.inch (75)                                                                
        
class PRODUCT_XRA_6024(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hood Covers"
        self.assembly_name = "XRA-6024"
        self.appliance_path = os.path.join(RANGE_HOOD_COVERS_PATH,"XRA-6024.blend") 
        self.height_above_floor = unit.inch (75)                                                               
        
                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                  