import bpy
from math import radians

# adds a premade cube
bpy.ops.mesh.primitive_cube_add()

# stores an object into a variable
so = bpy.context.active_object

# move object
so.location[0] = 5

# rotation of an object, creates a cube that is rotated by 45 degrees
# degrees = 45
# rad = degrees * math.pi / 180
# radians(45)
so.rotation_euler[0] += radians(45)

# create modifiers
mod_subsurf = so.modifiers.new("New Modifiers", "SUBSURF")
# so.modifiers["New Modifers"].levels = 3
mod_subsurf.levels = 3

# smmooth the object
bpy.ops.object.shade_smooth()

# below is the same thing as the one line above
#mesh = so.data
#for face in mesh.polygons:
#    face.use_smooth = True
    
# create displacement modifier
# https://docs.blender.org/api/current/bpy.types.Texture.html
mod_displace = so.modifiers.new("My Displacement", "DISPLACE")

# create texture
new_tex = bpy.data.textures.new("My Textures", "DISTORTED_NOISE")

# change the texture settings
new_tex.noise_scale = 2.0

# assign the texture to displacement modifier:
mod_displace.texture = new_tex


# create the material
new_mat = bpy.data.material.new(name = "My Material")
so.data.materials.append(new_mat)
new_mat.use_nodes = True
nodes = new_mat.nodes_tree.nodes
material_output = nodes.get("Material Output")
node_emission = nodes.new(type = "ShaderNodeEmission")