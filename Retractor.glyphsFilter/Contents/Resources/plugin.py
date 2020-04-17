# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	Filter without dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class Retractor(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Retractor',
			'de': 'Retraktor',
			'fr': 'Retracteur',
			'es': 'Retractor',
			'zh': '📐直线化',
		})
		self.keyboardShortcut = None # With Cmd+Shift

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		selection = layer.selection
		selectionCounts = inEditView and bool(selection)

		for thisPath in layer.paths:
			for x in reversed( range( len( thisPath.nodes ))):
				thisNode = thisPath.nodes[x]
				if not selectionCounts:
					if thisNode.type == OFFCURVE:
						del thisPath.nodes[x]
					else:
						thisNode.type = LINE
				elif selectionCounts:
					prevNode = thisPath.nodes[x-1]
					nextNode = thisPath.nodes[x+1]
					if thisNode.type != OFFCURVE:
						if prevNode.type == OFFCURVE and prevNode in selection:
							thisNode.type = LINE
					elif thisNode.type == OFFCURVE:
						if thisNode in selection:
							if nextNode.type == OFFCURVE:
								del thisPath.nodes[x+1]
							del thisPath.nodes[x]
							thisPath.nodes[x].type = LINE
						elif prevNode.type != OFFCURVE and nextNode.type != OFFCURVE:
							del thisPath.nodes[x]
					
			thisPath.checkConnections()
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	