##############################
"""
Creator: 
	Huston Petty
	http://www.hustonpetty3d.com

Document: 
	orbitLights_UI.py

Description:
	This is the module that creates the interface

How to Run:

import Orbital_Light_Previewer.orbitLights_UI as hp3d
reload(hp3d)
hp3d.gui()   # Dockable 
# hp3d.gui(False) # Not Dockable 

Video Tutorial:
	______________________________

"""

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide.QtGui import *
from PySide.QtCore import *

import pymel.core as pm
import webbrowser as web
import functools as fun
import maya.utils as utils

import orbitLights_cmds as command
reload(command)
import orbitLights_interfaceCreation
reload(orbitLights_interfaceCreation)

class MainDialog(QDialog, orbitLights_interfaceCreation.Ui_window_obj):
	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)

		brand_icon = command.get_icon_path('tool_brand_icon.png')
		self.website_label.setPixmap(QPixmap(brand_icon))
		self.how_to.clicked.connect(pm.Callback(web.open, 'https://www.youtube.com'))
		self.connect(self.website_label, SIGNAL('clicked()'), pm.Callback(web.open, 'http://www.hustonpetty3d.com'))

		self.distance_float.valueChanged.connect(self.change_distance)
		self.interv_int.valueChanged.connect(self.change_orbitInterv)
		self.orbit_int.valueChanged.connect(self.change_orbitInterv)

		self.lightType_menu.currentIndexChanged.connect(pm.Callback(self.enableDisable_component, self.createRig_btn))
		self.createRig_btn.clicked.connect(self.createRig)
		self.deleteRig_btn.clicked.connect(self.deleteRig)
		self.showVis_ckbx.stateChanged.connect(self.showVis)

	def change_distance(self):
		intervValue = self.interv_int.value()
		value = self.distance_float.value()

		pm.setAttr(rigLight+'.translateZ', value)
		pm.xform(vis_mainGrp, s=[value, value, value])
		vis_mainGrp

	def change_orbitInterv(self):
		self.set_framesField()
		self.setExpression()

		if self.sender().objectName() == 'orbit_int' and self.showVis_ckbx.isChecked():
			pm.delete(vis_orbGrp)
			pm.delete(vis_intervGrp)
			self.vis_orbits()
			self.vis_intervals()
		elif self.sender().objectName() == 'interv_int' and self.showVis_ckbx.isChecked():
			pm.delete(vis_intervGrp)
			self.vis_intervals()

	def set_framesField(self):
		interv_int = self.interv_int.value()
		orbit_int = self.orbit_int.value()
		value = interv_int * orbit_int

		self.frames_int.setValue(value)
		pm.setAttr("defaultRenderGlobals.endFrame", value)
		pm.playbackOptions(maxTime=value, e=True)

	def createRig(self):
		pm.currentTime(0, e=True)

		global sel_objects
		sel_objects = pm.ls(sl=True, tr=True)
		if sel_objects == []:
			print '\n# Error: Please select an object first'
			pm.confirmDialog(title = 'Error: Nothing Selected', 
					m = 'Please select an object to create the light rig around.', 
					button = 'Ok', 
					db = 'Ok')
			self.close()
			gui(dock=False)
		else:
			global light_name
			light_name = 'light1'
			name_request = pm.promptDialog(
				t='Light Name', 
				m='Enter Your New Light\'s Name', 
				ma='left',
				tx='Ex: key_light',
				st='text', 
				b=['Ok', 'Cancel'], 
				db='Ok', 
				cb='Cancel',
				ds='Cancel')
			if name_request == 'Ok':
				light_name = pm.promptDialog(query=True, text=True)

			global sel_center
			sel_center = command.averageCoords(sel_objects)

			global rigOrbit, rigInterv, rigLight
			rigOrbit = pm.group(n='olp_orbitsGrp1', em=True)
			rigInterv = pm.group(n='olp_intervalsGrp1', em=True)
			rigLight = self.createLight(sel_center)
			self.setExpression()
			pm.createRenderLayer([sel_objects, rigOrbit, rigInterv, rigLight], noRecurse=True, name='{0}_layer'.format(light_name))
			self.createVis()

			pm.xform(rigOrbit, a=True, t=sel_center)
			pm.xform(rigInterv, a=True, t=sel_center)

			pm.parent(rigLight, rigInterv)
			pm.parent(rigInterv, rigOrbit)

			pm.select(sel_objects, r=True)

			# GUI Components enable/disable
			self.enableDisable_component(self.createRig_btn, enabled=False)
			self.enableDisable_component(self.deleteRig_btn, enabled=True)
			self.enableDisable_component(self.distance_label, enabled=True)
			self.enableDisable_component(self.distance_float, enabled=True)
			self.enableDisable_component(self.orbit_label, enabled=True)
			self.enableDisable_component(self.orbit_int, enabled=True)
			self.enableDisable_component(self.interv_label, enabled=True)
			self.enableDisable_component(self.interv_int, enabled=True)
			self.enableDisable_component(self.showVis_ckbx, enabled=True)

	def createLight(self, position):
		value = self.distance_float.value()
		if self.lightType_menu.currentIndex() == 1:
			light = pm.shadingNode('areaLight', asLight=True)
			
			pm.setAttr(light + '.intensity', 500)
			pm.setAttr(light + '.decayRate', 2)
			pm.setAttr(light + '.areaLight', 1)

		elif self.lightType_menu.currentIndex() == 2:
			light = pm.shadingNode('spotLight', asLight=True)

			pm.setAttr(light + '.intensity', 500)
			pm.setAttr(light + '.decayRate', 2)

		elif self.lightType_menu.currentIndex() == 3:
			light = pm.shadingNode('directionalLight', asLight=True)

		elif self.lightType_menu.currentIndex() == 4:
			light = pm.shadingNode('pointLight', asLight=True)

			pm.setAttr(light + '.intensity', 500)
			pm.setAttr(light + '.decayRate', 2)

		pm.rename(light, light_name)
		pm.xform(light, a=True, t=position)
		pm.xform(light, r=True, t=(0, 0, value))

		return light

	def deleteRig(self):
		pm.parent(rigLight, w=True)
		pm.delete([rigInterv, rigOrbit, vis_mainGrp])

		pm.select(sel_objects, r=True)

		# GUI Components enable/disable
		self.enableDisable_component(self.createRig_btn, enabled=True)
		self.enableDisable_component(self.deleteRig_btn, enabled=False)
		self.enableDisable_component(self.distance_label, enabled=False)
		self.enableDisable_component(self.distance_float, enabled=False)
		self.enableDisable_component(self.orbit_label, enabled=False)
		self.enableDisable_component(self.orbit_int, enabled=False)
		self.enableDisable_component(self.interv_label, enabled=False)
		self.enableDisable_component(self.interv_int, enabled=False)
		self.enableDisable_component(self.showVis_ckbx, enabled=False)
		self.orbit_label.setStyleSheet("")
		self.interv_label.setStyleSheet("")

	def enableDisable_component(self, component, enabled=True):
		if enabled == False or self.lightType_menu.currentIndex() == 0:
			component.setEnabled(False)
			if str(type(component)) == "<type 'PySide.QtGui.QPushButton'>":
				component.setStyleSheet("background-color: #4f6061")
		elif enabled == True or self.lightType_menu.currentIndex() != 0:
			component.setEnabled(True)
			if str(type(component)) == "<type 'PySide.QtGui.QPushButton'>":
				component.setStyleSheet("background-color: #35555a")

	def setExpression(self):
		if pm.objExists('olp_intervalsPerOrbits_expression'):
			pm.delete('olp_intervalsPerOrbits_expression')
		if pm.objExists('olp_orbits_expression'):
			pm.delete('olp_orbits_expression')
		
		interv_int = self.interv_int.value()
		orbit_int = self.orbit_int.value()

		intervExpression = pm.expression(o=rigInterv, n='olp_intervalsPerOrbits_expression', s='rx = frame * (360/{0}.000);'.format(interv_int))
		if_block = 'rz = (frame/{0}) * ((360/{1}.000)/2.000);'.format(interv_int, orbit_int)
		orbitExpression = pm.expression(o=rigOrbit, n='olp_orbits_expression', s='if (frame%{0} == 0) {1}'.format(interv_int, if_block))

	def createVis(self):
		if pm.objExists('olp_visualizationGrp'):
			pm.delete('olp_visualizationGrp')

		global vis_mainGrp
		vis_mainGrp = pm.group(n='olp_visualizationGrp', em=True)
		pm.xform(vis_mainGrp, a=True, t=sel_center, s=[5, 5, 5])
		self.showVis()
		self.vis_orbits()
		self.vis_intervals()

	def vis_orbits(self):
		global vis_orbGrp
		vis_orbGrp = pm.group(n='olp_visOrbits', em=True)

		intervValue = self.interv_int.value()
		distValue = self.distance_float.value()
		orbitValue = self.orbit_int.value()

		global all_orbitObjs
		all_orbitObjs = []
		for orbit in range(orbitValue):
			orbitRot = orbit * 360/float(orbitValue*2)
			
			orbit_visObject = pm.circle(n='olp_orbCircle{0}'.format(orbit+1), r=distValue, s=intervValue*2, nr=[1, 0, 0], ch=True)[0]
			pm.parent(orbit_visObject, vis_orbGrp)

			orbit_visObject.overrideEnabled.set(1)
			orbit_visObject.overrideColorRGB.set(0, 1, 1)
			orbit_visObject.overrideRGBColors.set(1)

			pm.xform(orbit_visObject, ro=[0, 0, orbitRot])

			all_orbitObjs.append(orbit_visObject)

		pm.xform(vis_orbGrp, a=True, t=sel_center)
		pm.parent(vis_orbGrp, vis_mainGrp)
		pm.select(sel_objects, r=True)
		return vis_orbGrp

	def vis_intervals(self):
		global vis_intervGrp
		vis_intervGrp = pm.group(n='olp_visIntervals', em=True)
		
		distValue = self.distance_float.value()
		intervValue = self.interv_int.value()
		orbitValue = self.orbit_int.value()

		global all_intervObjs
		all_intervObjs = []
		all_intervGrps = []

		vis_baseInterv = pm.group(n='olp_visIntervals_orbit1', em=True)
		all_intervGrps.append(vis_baseInterv)
		for interv in range(intervValue):
			intervRot = (interv % intervValue) * 360/float(intervValue)
			
			vis_sphereGrp = pm.group(n='olp_spherePivot{0}'.format(interv+1), em=True)
			interv_visObject = command.create_curveSphere(name='olp_interv_visObject{0}'.format(interv+1), radius=distValue/33.333)
			pm.parent(interv_visObject, vis_sphereGrp)
			
			pm.xform(vis_sphereGrp, ro=[intervRot, 0, 0])
			pm.xform(interv_visObject, t=[0, 0, distValue])
			pm.parent(vis_sphereGrp, vis_baseInterv)

			all_intervObjs.append(interv_visObject)

		for each in range(orbitValue-1):
			orbitRot = (each+1) * 360/float(orbitValue*2)

			newintervRing = pm.duplicate(vis_baseInterv, rr=True)
			pm.xform(newintervRing[0], ro=[0, 0, orbitRot])
			pm.makeIdentity(newintervRing[0], a=True, t=True, r=True, s=True, n=False)

			all_intervGrps.append(newintervRing[0])
			all_intervObjs += pm.listRelatives(pm.listRelatives(newintervRing, c=True), c=True)

		pm.parent(all_intervGrps, vis_intervGrp)
		pm.xform(vis_intervGrp, a=True, t=sel_center)
		pm.parent(vis_intervGrp, vis_mainGrp)
		pm.select(sel_objects, r=True)
		
		return vis_intervGrp

	def showVis(self):
		if self.showVis_ckbx.isChecked() == 1:
			vis_mainGrp.v.set(1)
			self.orbit_label.setStyleSheet("color: rgb(0, 255, 255)")
			self.interv_label.setStyleSheet("color: rgb(255, 255, 0)")
		else:
			vis_mainGrp.v.set(0)
			self.orbit_label.setStyleSheet("")
			self.interv_label.setStyleSheet("")

class MyDockableWindow(MayaQWidgetDockableMixin, MainDialog):
    def __init__(self, parent=None):
        super(MyDockableWindow, self).__init__(parent=parent)



def gui(dock=True):
	global window_obj
	try:
		window_obj.close()
		print '\n# Existing windows deleted'
	except:
		print '\n# Window does not yet exist: Creating new window'

	pm.setAttr("defaultRenderGlobals.startFrame", 0)
	pm.setAttr("defaultRenderGlobals.endFrame", 32)
	pm.playbackOptions(minTime=0, e=True)
	pm.playbackOptions(maxTime=32, e=True)
	pm.currentTime(0, e=True)

	parent = command.getMayaWindow()
	window_obj = MyDockableWindow(parent)
	window_obj.show(dockable=dock)    















