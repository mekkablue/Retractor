# Retractor.glyphsFilter

This is a plugin for the [Glyphs font editor](http://glyphsapp.com/). It deletes (‘retracts’) all Bézier control points (a.k.a. BCPs, handles), making sure only straight line segments remain. This can be useful if you want to be certain that accidentally added curve segments are removed in designs where this is necessary. 

### Installation

1. In *Window > Plugin Manager,* click the *Install* button next to *Retractor.*
2. Restart Glyphs.

### Usage Instructions

1. Open a glyph in Edit View (with or without a partial path selection), or select any number of glyphs in Font or Edit View.
2. Use *Filter > Retractor* (de: *Retraktor,* fr: *Retracteur*) to remove all curve handles.

Alternatively, you can also use it as a custom parameter on the whole font at export time:

	Property: Filter
	Value: Retractor

### Requirements

The plugin needs Glyphs 2.4, I assume it will not work in previous versions.

### License

Copyright 2015-2018 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
