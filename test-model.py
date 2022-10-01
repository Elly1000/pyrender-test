import sys
import os
import pyglet
pyglet.options['shadow_window'] = False
import numpy as np
import trimesh

#---------- Append packages directory ----------------
sys.path.append('./packages')


#---------- Parse Argument----------------
file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

print("File path : " + file_path)
if(os.path.exists("output") == False):
    os.makedirs("output")
    
outpath = "output/" + os.path.basename(os.path.splitext(file_path)[0]) + ".png"
print("Output file path : " + outpath)

from packages.pyrender import OrthographicCamera, DirectionalLight, PerspectiveCamera, \
                              Mesh, Node, Scene,\
                              Viewer, OffscreenRenderer

#==============================================================================
# Mesh creation
#==============================================================================
model_trimesh = trimesh.load(file_path)
model_mesh = Mesh.from_trimesh(model_trimesh)
maxCorner = np.max(model_trimesh.vertices, axis=0)
minCorner = np.min(model_trimesh.vertices, axis=0)
sizeXYZ = maxCorner - minCorner
centerXYZ = (maxCorner + minCorner) / 2.0
print("Model Size: {}, {}, {}".format(sizeXYZ[0], sizeXYZ[1], sizeXYZ[2]))
print("Center Position: {}, {}, {}".format(centerXYZ[0], centerXYZ[1], centerXYZ[2]))


#==============================================================================
# Light creation
#==============================================================================

direc_l = DirectionalLight(color=np.ones(3), intensity=1.0)

#==============================================================================
# Camera creation
#==============================================================================
# !!! NOTE: Offscreen is not working with orthographic camera.
cam = OrthographicCamera(0.9, 0.9, 0.01, 1000)
cam_pose = np.array([
    [1.0,  0.0,    0.0,     0],
    [0.0,  1.0,    0.0,     0.0],
    [0.0,  0.0,    1.0,     np.max(maxCorner)],
    [0.0,  0.0,    0.0,     1.0]
])


yfov=(np.pi / 3.0) # radian
perCam = PerspectiveCamera(yfov=yfov)

# Calculate proper distance
dist = np.max(sizeXYZ[0:1]) * 1.5 / (2 * np.tan( yfov / 2 ))
perCam_pose = np.array([
    [1.0,  0.0,    0.0,     0],
    [0.0,  1.0,    0.0,     0.0],
    [0.0,  0.0,    1.0,     dist],
    [0.0,  0.0,    0.0,     1.0]
])

#==============================================================================
# Scene creation
#==============================================================================

scene = Scene(ambient_light=np.array([0.2, 0.2, 0.2, 1.0]),
              bg_color=[0, 0, 0])

#==============================================================================
# Adding objects to the scene
#==============================================================================
bunny_node = Node(mesh=model_mesh, translation=centerXYZ*-1.0)
scene.add_node(bunny_node)
direc_l_node = scene.add(direc_l, pose=perCam_pose)
cam_node = scene.add(perCam, pose=perCam_pose)

v = Viewer(scene, viewport_size=np.array([640, 640]))

#==============================================================================
# Rendering offscreen from that camera
#==============================================================================

r = OffscreenRenderer(viewport_width=640, viewport_height=640)
color, depth = r.render(scene)

from packages.PIL import Image
im = Image.fromarray(color)
im.save(outpath)