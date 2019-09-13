from PCV.geometry import camera
from numpy import *
from PIL import Image

im1 = array(Image.open('images/001.jpg'))
im2 = array(Image.open('images/002.jpg'))

point2D = [loadtxt('2D/00'+str(i+1)+'.corners').T for i in range(3)]

point3D = loadtxt('3D/p3d').T

corr = genfromtxt('2D/nview-corners', dtype='int', missing_values='*')

P = [camera.Camera(loadtxt('2D/00' + str(i+1) + '.P')) for i in range(3)]

