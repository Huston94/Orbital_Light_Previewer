# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Huston_Student/Library/Preferences/Autodesk/maya/scripts/Orbital_Light_Previewer/orbitLights_interfaceCreation.ui'
#
# Created: Mon Oct  5 20:22:37 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_window_obj(object):
    def setupUi(self, window_obj):
        window_obj.setObjectName("window_obj")
        window_obj.resize(400, 309)
        window_obj.setMinimumSize(QtCore.QSize(360, 309))
        window_obj.setMaximumSize(QtCore.QSize(16777215, 309))
        window_obj.setWindowOpacity(1.0)
        self.verticalLayout = QtGui.QVBoxLayout(window_obj)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.website_label = QtGui.QLabel(window_obj)
        self.website_label.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.website_label.sizePolicy().hasHeightForWidth())
        self.website_label.setSizePolicy(sizePolicy)
        self.website_label.setMaximumSize(QtCore.QSize(16777215, 44))
        self.website_label.setText("")
        self.website_label.setTextFormat(QtCore.Qt.RichText)
        self.website_label.setPixmap(QtGui.QPixmap("../render_notification/icons/tool_brand_icon.png"))
        self.website_label.setScaledContents(False)
        self.website_label.setOpenExternalLinks(True)
        self.website_label.setObjectName("website_label")
        self.horizontalLayout_10.addWidget(self.website_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.how_to = QtGui.QPushButton(window_obj)
        self.how_to.setStyleSheet("background-color: #35555a; color: #E6FEFF; selection-background-color: #64A1A8;")
        self.how_to.setObjectName("how_to")
        self.horizontalLayout_10.addWidget(self.how_to)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.mainTab = QtGui.QTabWidget(window_obj)
        self.mainTab.setEnabled(True)
        self.mainTab.setObjectName("mainTab")
        self.lightRig_tab = QtGui.QWidget()
        self.lightRig_tab.setObjectName("lightRig_tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.lightRig_tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lightType_menu = QtGui.QComboBox(self.lightRig_tab)
        self.lightType_menu.setMinimumSize(QtCore.QSize(0, 24))
        self.lightType_menu.setStyleSheet("background-color: #35555a")
        self.lightType_menu.setObjectName("lightType_menu")
        self.lightType_menu.addItem("")
        self.lightType_menu.setItemText(0, "Light Type")
        self.lightType_menu.addItem("")
        self.lightType_menu.addItem("")
        self.lightType_menu.addItem("")
        self.lightType_menu.addItem("")
        self.horizontalLayout_3.addWidget(self.lightType_menu)
        self.createRig_btn = QtGui.QPushButton(self.lightRig_tab)
        self.createRig_btn.setEnabled(False)
        self.createRig_btn.setStyleSheet("background-color: #4f6061")
        self.createRig_btn.setObjectName("createRig_btn")
        self.horizontalLayout_3.addWidget(self.createRig_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtGui.QLabel(self.lightRig_tab)
        self.label_2.setEnabled(False)
        self.label_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.line_2 = QtGui.QFrame(self.lightRig_tab)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_9.addWidget(self.line_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtGui.QLabel(self.lightRig_tab)
        self.label.setMinimumSize(QtCore.QSize(130, 0))
        self.label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.showVis_ckbx = QtGui.QCheckBox(self.lightRig_tab)
        self.showVis_ckbx.setEnabled(False)
        self.showVis_ckbx.setObjectName("showVis_ckbx")
        self.horizontalLayout_8.addWidget(self.showVis_ckbx)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.distance_label = QtGui.QLabel(self.lightRig_tab)
        self.distance_label.setEnabled(False)
        self.distance_label.setMinimumSize(QtCore.QSize(130, 0))
        self.distance_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.distance_label.setObjectName("distance_label")
        self.horizontalLayout_2.addWidget(self.distance_label)
        self.distance_float = QtGui.QDoubleSpinBox(self.lightRig_tab)
        self.distance_float.setEnabled(False)
        self.distance_float.setMaximumSize(QtCore.QSize(60, 16777215))
        self.distance_float.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.distance_float.setDecimals(3)
        self.distance_float.setMinimum(0.001)
        self.distance_float.setMaximum(9999999.99)
        self.distance_float.setProperty("value", 5.0)
        self.distance_float.setObjectName("distance_float")
        self.horizontalLayout_2.addWidget(self.distance_float)
        spacerItem1 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.orbit_label = QtGui.QLabel(self.lightRig_tab)
        self.orbit_label.setEnabled(False)
        self.orbit_label.setMinimumSize(QtCore.QSize(130, 0))
        self.orbit_label.setStyleSheet("")
        self.orbit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.orbit_label.setObjectName("orbit_label")
        self.horizontalLayout_6.addWidget(self.orbit_label)
        self.orbit_int = QtGui.QSpinBox(self.lightRig_tab)
        self.orbit_int.setEnabled(False)
        self.orbit_int.setMinimumSize(QtCore.QSize(60, 0))
        self.orbit_int.setMaximumSize(QtCore.QSize(60, 16777215))
        self.orbit_int.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.orbit_int.setMinimum(2)
        self.orbit_int.setMaximum(64)
        self.orbit_int.setProperty("value", 4)
        self.orbit_int.setObjectName("orbit_int")
        self.horizontalLayout_6.addWidget(self.orbit_int)
        spacerItem2 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.interv_label = QtGui.QLabel(self.lightRig_tab)
        self.interv_label.setEnabled(False)
        self.interv_label.setMinimumSize(QtCore.QSize(130, 0))
        self.interv_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.interv_label.setObjectName("interv_label")
        self.horizontalLayout_5.addWidget(self.interv_label)
        self.interv_int = QtGui.QSpinBox(self.lightRig_tab)
        self.interv_int.setEnabled(False)
        self.interv_int.setMinimumSize(QtCore.QSize(60, 0))
        self.interv_int.setMaximumSize(QtCore.QSize(60, 16777215))
        self.interv_int.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.interv_int.setMinimum(4)
        self.interv_int.setMaximum(64)
        self.interv_int.setProperty("value", 8)
        self.interv_int.setObjectName("interv_int")
        self.horizontalLayout_5.addWidget(self.interv_int)
        spacerItem3 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frames_label = QtGui.QLabel(self.lightRig_tab)
        self.frames_label.setMinimumSize(QtCore.QSize(130, 0))
        self.frames_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.frames_label.setObjectName("frames_label")
        self.horizontalLayout_7.addWidget(self.frames_label)
        self.frames_int = QtGui.QSpinBox(self.lightRig_tab)
        self.frames_int.setEnabled(False)
        self.frames_int.setMinimumSize(QtCore.QSize(60, 0))
        self.frames_int.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frames_int.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.frames_int.setMinimum(16)
        self.frames_int.setMaximum(4096)
        self.frames_int.setSingleStep(1)
        self.frames_int.setProperty("value", 32)
        self.frames_int.setObjectName("frames_int")
        self.horizontalLayout_7.addWidget(self.frames_int)
        spacerItem4 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line = QtGui.QFrame(self.lightRig_tab)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteRig_btn = QtGui.QPushButton(self.lightRig_tab)
        self.deleteRig_btn.setEnabled(False)
        self.deleteRig_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.deleteRig_btn.setFont(font)
        self.deleteRig_btn.setStyleSheet("background-color: #4f6061")
        self.deleteRig_btn.setObjectName("deleteRig_btn")
        self.horizontalLayout.addWidget(self.deleteRig_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.mainTab.addTab(self.lightRig_tab, "")
        self.tools_tab = QtGui.QWidget()
        self.tools_tab.setEnabled(False)
        self.tools_tab.setObjectName("tools_tab")
        self.mainTab.addTab(self.tools_tab, "")
        self.verticalLayout.addWidget(self.mainTab)

        self.retranslateUi(window_obj)
        self.mainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window_obj)
        window_obj.setTabOrder(self.mainTab, self.showVis_ckbx)
        window_obj.setTabOrder(self.showVis_ckbx, self.distance_float)
        window_obj.setTabOrder(self.distance_float, self.interv_int)
        window_obj.setTabOrder(self.interv_int, self.orbit_int)
        window_obj.setTabOrder(self.orbit_int, self.frames_int)
        window_obj.setTabOrder(self.frames_int, self.lightType_menu)
        window_obj.setTabOrder(self.lightType_menu, self.createRig_btn)
        window_obj.setTabOrder(self.createRig_btn, self.deleteRig_btn)

    def retranslateUi(self, window_obj):
        window_obj.setWindowTitle(QtGui.QApplication.translate("window_obj", "HP3D | Orbital Light Previewer", None, QtGui.QApplication.UnicodeUTF8))
        self.website_label.setToolTip(QtGui.QApplication.translate("window_obj", "www.hustonpetty3d.com", None, QtGui.QApplication.UnicodeUTF8))
        self.how_to.setToolTip(QtGui.QApplication.translate("window_obj", "<html><head/><body><p><span style=\" color:#000000; background-color: #ffffdc; border: 1px solid black; \">Go to the &quot;How To Use&quot; video</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.how_to.setText(QtGui.QApplication.translate("window_obj", "How To Use?", None, QtGui.QApplication.UnicodeUTF8))
        self.lightType_menu.setItemText(1, QtGui.QApplication.translate("window_obj", "Area", None, QtGui.QApplication.UnicodeUTF8))
        self.lightType_menu.setItemText(2, QtGui.QApplication.translate("window_obj", "Spot", None, QtGui.QApplication.UnicodeUTF8))
        self.lightType_menu.setItemText(3, QtGui.QApplication.translate("window_obj", "Directional", None, QtGui.QApplication.UnicodeUTF8))
        self.lightType_menu.setItemText(4, QtGui.QApplication.translate("window_obj", "Point", None, QtGui.QApplication.UnicodeUTF8))
        self.createRig_btn.setText(QtGui.QApplication.translate("window_obj", "Create Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("window_obj", "Rig Options", None, QtGui.QApplication.UnicodeUTF8))
        self.showVis_ckbx.setText(QtGui.QApplication.translate("window_obj", "Show Visualization", None, QtGui.QApplication.UnicodeUTF8))
        self.distance_label.setToolTip(QtGui.QApplication.translate("window_obj", "Set the distance that the light should orbit the object from", None, QtGui.QApplication.UnicodeUTF8))
        self.distance_label.setText(QtGui.QApplication.translate("window_obj", "Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.distance_float.setToolTip(QtGui.QApplication.translate("window_obj", "Set the distance that the light should orbit the object from", None, QtGui.QApplication.UnicodeUTF8))
        self.orbit_label.setToolTip(QtGui.QApplication.translate("window_obj", "<html><head/><body><p><span style=\" color:#000000; border: 1px solid black; \">Set how many orbits there should be NOTE: This number should be half of the \"Intervals per Revolution\" attribute for even lighting all the way around</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.orbit_label.setText(QtGui.QApplication.translate("window_obj", "Orbits", None, QtGui.QApplication.UnicodeUTF8))
        self.orbit_int.setToolTip(QtGui.QApplication.translate("window_obj", "<html><head/><body><p><span style=\" color:#000000; border: 1px solid black; \">Set how many revolutions there should be\n"
"\n"
"NOTE: This number should be half of the \"Intervals per Revolution\" \n"
"          attribute for even lighting all the way around</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.interv_label.setToolTip(QtGui.QApplication.translate("window_obj", "<html><head/><body><p><span style=\" color:#000000; border: 1px solid black; \">Set the amount of intervals there should be in each revolution\n"
"\n"
"NOTE: This number should be double the \"Revolutions\" \n"
"          attribute for even lighting all the way around</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.interv_label.setText(QtGui.QApplication.translate("window_obj", "Intervals per Orbit", None, QtGui.QApplication.UnicodeUTF8))
        self.interv_int.setToolTip(QtGui.QApplication.translate("window_obj", "<html><head/><body><p><span style=\" color:#000000; border: 1px solid black; \">Set the amount of intervals there should be in each revolution\n"
"\n"
"NOTE: This number should be double the \"Revolutions\" \n"
"          attribute for even lighting all the way around</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.frames_label.setToolTip(QtGui.QApplication.translate("window_obj", "Total number of frames that will need to be rendered with the current settings", None, QtGui.QApplication.UnicodeUTF8))
        self.frames_label.setText(QtGui.QApplication.translate("window_obj", "Frames to Render", None, QtGui.QApplication.UnicodeUTF8))
        self.frames_int.setToolTip(QtGui.QApplication.translate("window_obj", "Total number of frames that will need to be rendered with the current settings", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteRig_btn.setText(QtGui.QApplication.translate("window_obj", "Delete Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.lightRig_tab), QtGui.QApplication.translate("window_obj", "Light Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabToolTip(self.mainTab.indexOf(self.lightRig_tab), QtGui.QApplication.translate("window_obj", "Create an orbiting light rig for quick lighting options", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tools_tab), QtGui.QApplication.translate("window_obj", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabToolTip(self.mainTab.indexOf(self.tools_tab), QtGui.QApplication.translate("window_obj", "Create a more visual depth of field rig for the Bokeh Lens Shader", None, QtGui.QApplication.UnicodeUTF8))

