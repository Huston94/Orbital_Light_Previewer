from PySide.QtGui import *
from PySide.QtCore import *

# When Recompiling, paste this in instead of to QLabel assignment in *_GUI.py file to have clickability
# Also be sure to 'import ExtendedQLabel' at the top of the the file
# self.website_label = ExtendedQLabel.ExtendedQLabel(window_obj)

class ExtendedQLabel(QLabel):
	def __init(self, parent):
		QLabel.__init__(self, parent)

	def mouseReleaseEvent(self, ev):
		self.emit(SIGNAL('clicked()'))
