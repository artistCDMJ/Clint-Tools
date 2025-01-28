#new panel fo the N Panel to allow Clint to sculpt and model more efficiently
# will add more as needs arise

import bpy

bl_info = {"name": "Clint_Tool",
           "author": "CDMJ",
           "version": (1, 00, 1),
           "blender": (4, 2, 0),
           "location": "N-Panel > ClintTool",
           "description": "In House Tool for Sculpt and Modeling",
           "warning": "",
           "category": "Object"}

### operators where necessary


### shortcut to correct normals from Object Mode
class CLINT_OT_refresh_normals(bpy.types.Operator):
    """Substitute for Ctrl N """
    bl_idname = "clint.refresh_normals"
    bl_label = "refresh normals"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # new code
        
        mode = bpy.context.mode        
        if mode == 'OBJECT':
            bpy.ops.object.mode_set(mode='EDIT')
        else:
            bpy.ops.object.mode_set(mode='EDIT')
            
        #bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}

### apply all modifiers
class CLINT_OT_apply_mods(bpy.types.Operator):
    """ Apply All Modifiers """
    bl_idname = "clint.apply_mods"
    bl_label = "apply all modifiers"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # new code
        
        mode = bpy.context.mode        
        if mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            
        #convert to mesh
        bpy.ops.object.convert(target='MESH')

        
        #bpy.ops.object.editmode_toggle()

        return {'FINISHED'}

### center the selected object to world center
class CLINT_OT_center_object(bpy.types.Operator):
    """ Center Selected Object to World Origin """
    bl_idname = "clint.center_object"
    bl_label = "center selected to world origin"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #scene = context.scene
        # new code
        
        mode = bpy.context.mode        
        if mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            
    
        # cursor to world origin
        bpy.ops.view3d.snap_cursor_to_center()
        # selected object origin to geometry
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        return {'FINISHED'}

### SET CENTER TO WORLD ORIGIN AND SET NEW MIRROR MODIFIER
class CLINT_OT_new_mirror(bpy.types.Operator):
    """ Set Origin to World and Mirror in Place """
    bl_idname = "clint.center_mirror"
    bl_label = "mirror to world origin"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #scene = context.scene
        # new code
        
        mode = bpy.context.mode        
        if mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            
    
        # cursor to world origin
        bpy.ops.view3d.snap_cursor_to_center()
        # selected object origin to geometry
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

        #add mirror
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        bpy.ops.object.modifier_add(type='MIRROR')
        

        return {'FINISHED'}

### add multires catmull 6x and new displacement modifier
class CLINT_OT_displace_set_smooth(bpy.types.Operator):
    """ Sets Smooth Multires and Displace Modifiers for Displace Texture """
    bl_idname = "clint.smooth_displace_multires"
    bl_label = "multires and displace"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # new code
        
        mode = bpy.context.mode        
        if mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
        
        ### multires linear
        bpy.ops.object.modifier_add(type='MULTIRES')
        # six times divided
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
        



        ### displace set
        bpy.ops.object.modifier_add(type='DISPLACE')
        bpy.ops.texture.new()
        bpy.context.object.modifiers["Displace"].texture_coords = 'UV'
        bpy.context.object.modifiers["Displace"].strength = 0.02   
    
        
        

        return {'FINISHED'}

### add multires linear 6x and new displacement modifier
class CLINT_OT_displace_set_linear(bpy.types.Operator):
    """ Sets Linear Multires and Displace Modifiers for Displace Texture """
    bl_idname = "clint.linear_displace_multires"
    bl_label = "multires and displace"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # new code
        
        mode = bpy.context.mode        
        if mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
        
        ### multires linear
        bpy.ops.object.modifier_add(type='MULTIRES')
        # six times divided
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='LINEAR')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='LINEAR')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='LINEAR')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='LINEAR')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='LINEAR')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='LINEAR')
        



        ### displace set
        bpy.ops.object.modifier_add(type='DISPLACE')
        bpy.ops.texture.new()
        bpy.context.object.modifiers["Displace"].texture_coords = 'UV'
        bpy.context.object.modifiers["Displace"].strength = 0.02   
    
        
        

        return {'FINISHED'}
 
### add dummy shader for UV and reset UV mapping to reset all faces to tiled texture
class CLINT_OT_uv_newmat(bpy.types.Operator):
    """ Set new UV Reset and New Material for Texture Alignment """
    bl_idname = "clint.uv_material"
    bl_label = "UV and Material"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        obj = context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B

    def execute(self, context):
        scene = context.scene
        # new code
        
        mode = bpy.context.mode        
        if mode == 'OBJECT':
            bpy.ops.object.mode_set(mode='EDIT')
        else:
            bpy.ops.object.mode_set(mode='EDIT')
            
        
        ### add new material and  uv map reset
        material_displace = bpy.data.materials.new(name="Displacement Setup")
        material_displace.use_nodes = True

        bpy.context.object.active_material = material_displace

        principled_node = material_displace.node_tree.nodes.get('Principled BSDF')
        
        ###Image Texture Node named Displace Source        
        displace_node = material_displace.node_tree.nodes.new('ShaderNodeTexImage')
        displace_node.location = (-600, 400)
        displace_node.label = ("Displace Source")        

        ###UV Mapping Node
        uv_node = material_displace.node_tree.nodes.new('ShaderNodeUVMap')
        uv_node.location = (-900, 400)
        uv_node.label = ("UV Projection")
        uv_node.uv_map = "UVMap"        

        #####LINKING
        link = material_displace.node_tree.links.new
        link(uv_node.outputs[0], displace_node.inputs[0])        
        link(displace_node.outputs[0], principled_node.inputs[0])
        
        # reset UV for all faces
        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.uv.reset()
                
        #set view to single texture
        bpy.context.space_data.shading.type = 'MATERIAL'
        bpy.context.space_data.shading.color_type = 'TEXTURE'
 
    
        
        return {'FINISHED'}

###


### panel building here
class CLINTTOOL_PT_main_panel(bpy.types.Panel):
    bl_label = "Clint Tools"
    bl_idname = "clinttool_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        box = layout.box()
        col = box.column(align=True)
        #col.label(text="Clint Tools Start Here")
        row = col.row(align=True)
        

        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25
        row1.operator("clint.refresh_normals",
                      text="Refresh Normals",
                      icon='NORMALS_FACE')
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.operator("clint.apply_mods",
                      text="Apply Mods",
                      icon="MODIFIER_ON")
        row=layout.row()
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        row3.operator("clint.center_object",
                      text="Center Object",
                      icon='CURSOR')
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        row3.operator("clint.center_mirror",
                      text="Mirror It",
                      icon='MOD_MIRROR')
        
        row=layout.row()
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        row3.operator("clint.uv_material",
                      text="UV Reset+Material",
                      icon='NODE_TEXTURE')
        row=layout.row()
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        row3.operator("clint.smooth_displace_multires",
                      text="Smooth Multires+Displace",
                      icon='TOOL_SETTINGS')
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        row3.operator("clint.linear_displace_multires",
                      text="Linear Multires+Displace",
                      icon='TOOL_SETTINGS')


### classes and registration of classes
classes = [
    CLINT_OT_refresh_normals,
    CLINT_OT_apply_mods,
    CLINT_OT_center_object,
    CLINT_OT_new_mirror,
    CLINT_OT_displace_set_smooth,
    CLINT_OT_displace_set_linear,
    CLINT_OT_uv_newmat,        
    CLINTTOOL_PT_main_panel
    
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    #bpy.types.Scene.my_tool = bpy.props.PointerProperty(
        #type=CARTONVIZ_PG_add_object_helper)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    #del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()