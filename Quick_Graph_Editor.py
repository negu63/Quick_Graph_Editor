bl_info = {
    "name": "Quick Graph Editor",
    "blender": (4, 1, 0),
    "category": "Interface",
}

import bpy

class NewWindowOperator(bpy.types.Operator):
    """Open the graph editor in a new window"""
    bl_idname = "wm.new_window_operator"
    bl_label = "Quick Graph Editor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.window_new()
        
        new_window = bpy.context.window_manager.windows[-1]
        new_screen = new_window.screen
        
        for area in new_screen.areas:
            area.type = 'GRAPH_EDITOR'
        
        return {'FINISHED'}

def draw_new_window_icon(self, context):
    layout = self.layout
    if context.region.alignment == 'RIGHT':
        layout.operator("wm.new_window_operator", text="", icon='GRAPH')

def register():
    bpy.utils.register_class(NewWindowOperator)
    bpy.types.TOPBAR_HT_upper_bar.prepend(draw_new_window_icon)

def unregister():
    bpy.utils.unregister_class(NewWindowOperator)
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_new_window_icon)

if __name__ == "__main__":
    register()
