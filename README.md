# Retractor.glyphsFilter

This is a plugin for the [Glyphs font editor](http://glyphsapp.com/) by Georg Seifert.
It deletes (‘retracts’) all Bézier control points (a.k.a. BCPs, handles), making sure only straight line segments remain. This can be useful if you want to be certain that accidentally added curve segments are removed in designs where this is necessary. Careful: it does *not* respect your node selection. If you want to only retract selected BCPs, simply press Delete.

### Installation

1. Download the complete ZIP file and unpack it, or clone the repository.
2. Double click the .glyphsFilter file. Confirm the dialog that appears in Glyphs.
3. Restart Glyphs.

### Usage Instructions

1. Open a glyph in Edit View, or select any number of glyphs in Font or Edit View.
2. Use *Filter > Retractor* to remove all curve handles.

Alternatively, you can also use it as a custom parameter on the whole font at export time:

	Property: Filter
	Value: Retractor

### Requirements

The plugin needs Glyphs 1.4.3 or higher, running on OS X 10.7 or later. I can only test it in current OS versions, and I assume it will not work in versions of Mac OS X older than 10.7.

### License

Copyright 2015 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
