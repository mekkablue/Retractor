# encoding: utf-8

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
	
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Retractor',
			'de': u'Retraktor',
			'fr': u'Retracteur',
		})
		self.keyboardShortcut = None # With Cmd+Shift

	def filter(self, layer, inEditView, customParameters):
		selection = layer.selection
		selectionCounts = inEditView and bool(selection)

		for thisPath in layer.paths:
			for x in reversed( range( len( thisPath.nodes ))):
				thisNode = thisPath.nodes[x]
				if not selectionCounts:
					if thisNode.type == OFFCURVE: # GSOFFCURVE
						del thisPath.nodes[x]
					else:
						thisNode.type = LINE # GSLINE
				elif selectionCounts:
					if thisNode.type != OFFCURVE:
						if thisNode.prevNode.type == OFFCURVE and thisNode.prevNode in selection:
							thisNode.type = LINE # GSLINE
					elif thisNode.type == OFFCURVE:
						if thisNode in selection:
							if thisNode.nextNode.type == OFFCURVE:
								del thisPath.nodes[x+1]
							del thisPath.nodes[x]
							thisPath.nodes[x].type = LINE
						elif thisNode.prevNode.type != OFFCURVE and thisNode.nextNode.type != OFFCURVE:
							del thisPath.nodes[x]
					
			thisPath.checkConnections()
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	