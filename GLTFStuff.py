# this code will be removed later on as we progress
# all this code is from https://pypi.org/project/pygltflib/, this is merely for testing and seeing what it actually does
from pygltflib import GLTF2
from pygltflib.utils import glb2gltf, gltf2glb

# convert glb to gltf
glb2gltf("Finger-Flex-Test/glTF-Sample-Models/2.0/Box/glTF-Binary/Box.glb")

# convert gltf to glb
gltf2glb("Finger-Flex-Test/glTF-Sample-Models/2.0/Box/glTF/Box.gltf", "something.glb", override=True)

# from pygltflib import GLTF2, Scene

# filename = "Finger-Flex-Test/glTF-Sample-Models/2.0/AnimatedCube/glTF/AnimatedCube.gltf"
# gltf = GLTF2().load(filename)
# gltf.scene
# gltf.scenes
# gltf.nodes[0]
# gltf.nodes[0].name
# gltf.meshes
# gltf.meshes[0].primitives[0].attributes

# filename2 = "test2.gltf"
# gltf.save(filename2)

# glb_filename = "Finger-Flex-Test/glTF-Sample-Models/2.0/Box/glTF-Binary/Box.glb"
# glb = GLTF2().load(glb_filename)
# glb.scene
# glb.scenes
# glb.nodes[0]
# glb.meshes[0].primitives[0].attributes
# glb.save("test2.glb")
# glb.binary_blob()

# from pygltflib import GLTF2

# # convert glb to gltf
# glb = GLTF2.load("Finger-Flex-Test/glTF-Sample-Models/2.0/Box/glTF-Binary/Box.glb")
# glb.save("test.gltf")

# # convert gltf to glb
# gltf = GLTF2.load("Finger-Flex-Test/glTF-Sample-Models/2.0/Box/glTF/Box.gltf")
# gltf.save("Finger-Flex-Test/test.glb")


# import numpy as np
# import pygltflib

# gltf = pygltflib.GLTF2(
#     scene=0,
#     scenes=[pygltflib.Scene(nodes=[0])],
#     nodes=[pygltflib.Node(mesh=0)],
#     meshes=[
#         pygltflib.Mesh(
#             primitives=[
#                 pygltflib.Primitive(
#                     attributes=pygltflib.Attributes(POSITION=1), indices=0
#                 )
#             ]
#         )
#     ],
#     accessors=[
#         pygltflib.Accessor(
#             bufferView=0,
#             componentType=pygltflib.UNSIGNED_BYTE,
#             count=36,
#             type=pygltflib.SCALAR,
#             max=[7],
#             min=[0],
#         ),
#         pygltflib.Accessor(
#             bufferView=1,
#             componentType=pygltflib.FLOAT,
#             count=8,
#             type=pygltflib.VEC3,
#             max=[0.5, 0.5, 0.5],
#             min=[-0.5, -0.5, -0.5],
#         ),
#     ],
#     bufferViews=[
#         pygltflib.BufferView(
#             buffer=0, byteLength=36, target=pygltflib.ELEMENT_ARRAY_BUFFER
#         ),
#         pygltflib.BufferView(
#             buffer=0, byteOffset=36, byteLength=96, target=pygltflib.ARRAY_BUFFER
#         ),
#     ],
#     buffers=[pygltflib.Buffer(byteLength=132)],
# )
# gltf.set_binary_blob(
#     b"\x00\x01\x02\x03\x02\x01\x01\x00\x04\x05\x04\x00\x03\x01\x06\x04\x06\x01"
#     b"\x02\x03\x07\x06\x07\x03\x00\x02\x05\x07\x05\x02\x05\x07\x04\x06\x04\x07"
#     b"\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00\x00\x00"
#     b"\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?"
#     b"\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf"
#     b"\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00"
#     b"\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf"
# )

# points = np.array(
#     [
#         [-0.5, -0.5, 0.5],
#         [0.5, -0.5, 0.5],
#         [-0.5, 0.5, 0.5],
#         [0.5, 0.5, 0.5],
#         [0.5, -0.5, -0.5],
#         [-0.5, -0.5, -0.5],
#         [0.5, 0.5, -0.5],
#         [-0.5, 0.5, -0.5],
#     ],
#     dtype = "float32",
# )
# triangles = np.array(
#     [
#         [0, 1, 2],
#         [3, 2, 1],
#         [1, 0, 4],
#         [5, 4, 0],
#         [3, 1, 6],
#         [4, 6, 1],
#         [2, 3, 7],
#         [6, 7, 3],
#         [0, 2, 5],
#         [7, 5, 2],
#         [5, 7, 4],
#         [6, 4, 2],
#     ],
#     dtype = "uint8",
# )

# triangles_binary_blob = triangles.flatten().tobytes()
# points_binary_blob = points.tobytes()
# gltf = pygltflib.GLTF2(
#     scene = 0,
#     scenes = [pygltflib.Scene(nodes = [0])],
#     nodes = [pygltflib.Node(mesh = 0)],
#     meshes = [
#         pygltflib.Mesh(
#             primitives = [
#                 pygltflib.Primitive(
#                     attributes = pygltflib.Attributes(POSITION = 1), indices = 0

#                 )
#             ]
#         )
#     ],
#     accessors = [
#         pygltflib.Accessor(
#             bufferView = 0,
#             componentType = pygltflib.UNSIGNED_BYTE,
#             count = triangles.size,
#             type = pygltflib.SCALAR,
#             max = [int(triangles.max())],
#             min = [int(triangles.min())],
#         ),
#         pygltflib.Accessor(
#             bufferView = 0,
#             componentType = pygltflib.FLOAT,
#             count = len(points),
#             type = pygltflib.VEC3,
#             max = points.max(axis = 0).tolist(),
#             min = points.min(axis = 0).tolist(),
#         ),
#     ],
#     bufferViews = [
#         pygltflib.BufferView(
#             buffer = 0,
#             byteLength = len(triangles_binary_blob),
#             target = pygltflib.ELEMENT_ARRAY_BUFFER
#         ),
#         pygltflib.BufferView(
#             buffer = 0,
#             byteOffset = len(triangles_binary_blob),
#             byteLength = len(points_binary_blob),
#             target = pygltflib.ARRAY_BUFFER,
#         ),
#     ],
#     buffers = [
#         pygltflib.Buffer(
#             byteLength = len(triangles_binary_blob) + len(points_binary_blob)
#         )
#     ],
# )
# gltf.set_binary_blob(triangles_binary_blob + points_binary_blob)

# glb = b"".join(gltf.save_to_bytes())
# gltf = pygltflib.GLTF2.load_from_bytes(glb)

# binary_blob = gltf.binary_blob()

# triangles_accessor = gltf.accessors[gltf.meshes[0].primitives[0].indices]
# triangles_buffer_view = gltf.bufferViews[triangles_accessor.bufferView]
# triangles = np.frombuffer(
#     binary_blob[
#         triangles_buffer_view.byteOffset
#         + triangles_accessor.byteOffset : triangles_buffer_view.byteOffset
#         + triangles_buffer_view.byteLength
#     ],
#     dtype = "uint8",
#     count = triangles_accessor.count,
# ).reshape((-1, 3))

# # create gltf objects for a scene with a primitive triangle with indexed geometry
# gltf = GLTF2()
# scene = Scene()
# mesh = Mesh()
# primitive = Primitive()
# node = Node()
# buffer = Buffer()
# bufferView1 = BufferView()
# bufferView2 = BufferView()
# acessor1 = Accessor()
# acessor2 = Accessor()

# # add data
# buffer.uri = "data:application/octet-stream;base64,AAABAAIAAAAAAAAAAAAAAAAAAAAAAIA/AAAAAAAAAAAAAAAAAACAPwAAAAA="
# buffer.byteLength = 44

# bufferView1.buffer = 0
# bufferView1.byteOffset = 0
# bufferView1.byteLength = 6
# bufferView1.target = ELEMENT_ARRAY_BUFFER

# bufferView2.buffer = 0
# bufferView2.byteOffset = 8
# bufferView2.byteLength = 36
# bufferView2.target = ARRAY_BUFFER

# acessor1.bufferView = 0
# acessor1.byteOffset = 0
# acessor1.componentType = UNSIGNED_SHORT
# acessor1.count = 3
# acessor1.type = SCALAR
# acessor1.max = [2]
# acessor1.min = [0]

# acessor2.bufferView = 1
# acessor2.byteOffset = 0
# acessor2.componentType = FLOAT
# acessor2.count = 3
# acessor2.type = VEC3
# acessor2.max = [1.0, 1.0, 0.0]
# acessor2.min = [0.0, 0.0, 0.0]

# primitive.attributes.POSITION = 1
# node.mesh = 0
# scene.nodes = [0]

# # assemble into a gltf structures
# gltf.scenes.append(scene)
# gltf.meshes.append(mesh)
# gltf.meshes[0].primitives.append(primitive)
# gltf.nodes.append(node)
# gltf.buffers.append(buffer)
# gltf.bufferViews.append(bufferView1)
# gltf.bufferViews.append(bufferView2)
# gltf.accessors.append(acessor1)
# gltf.accessors.append(acessor2)

# # save to file
# gltf.save("triangle.gltf")