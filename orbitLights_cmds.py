##############################
"""
Creator: 
	Huston Petty
	http://www.hustonpetty3d.com

Document: 
	orbitLights_cmds.py

Description:
	This module contains all of the non-class commands for the tool

"""
import pymel.core as pm
import os

import shiboken
from PySide import QtGui, QtCore
import maya.OpenMayaUI as mui

def get_icon_path(icon, icon_folder='icons'):
	base_path = os.path.split(__file__)[0]
	return os.path.join(base_path, icon_folder, icon)

def averageCoords(selection):
	all_x = []
	all_y = []
	all_z = []

	for each in selection:
		x, y, z = pm.objectCenter(each, gl=True)
		
		all_x.append(x)
		all_y.append(y)
		all_z.append(z)

	totX = float(sum(all_x))
	totY = float(sum(all_y))
	totZ = float(sum(all_z))

	avg_X = totX/len(all_x)
	avg_Y = totY/len(all_y)
	avg_Z = totZ/len(all_z)

	return [avg_X, avg_Y, avg_Z]

def create_curveSphere(name, radius):
	circGrp = pm.group(n=name, em=True)
	circ1 = pm.circle(nr=[1, 0, 0], ch=True)[0]
	circ2 = pm.circle(nr=[1, 0, 0], ch=True)[0]
	circ3 = pm.circle(nr=[1, 0, 0], ch=True)[0]
	circs = [circ1, circ2, circ3]

	circGrp.overrideEnabled.set(1)
	circGrp.overrideColorRGB.set(1, 1, 0)
	circGrp.overrideRGBColors.set(1)

	pm.xform(circGrp, s=[radius, radius, radius])
	pm.xform(circ2, ro=[0, 90, 0])
	pm.xform(circ3, ro=[0, 0, 90])

	pm.makeIdentity([circ1, circ2, circ3], a=True, t=True, r=True, s=True, n=False)

	circ1_shape = pm.listRelatives(circ1, s=True)[0]
	circ2_shape = pm.listRelatives(circ2, s=True)[0]
	circ3_shape = pm.listRelatives(circ3, s=True)[0]

	pm.parent([circ1_shape, circ2_shape, circ3_shape], circGrp, r=True, s=True)
	pm.delete([circ1, circ2, circ3])

	return circGrp

def getMayaWindow():
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """
    ptr = mui.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken.wrapInstance(long(ptr), QtGui.QWidget)
