
"""A single sizer."""

import wx
from BlockWindow import BlockWindow

labels = "one two three four five six seven eight nine".split()

class GridSizerFrame( wx.Frame ):
	def __init__( self ):
		wx.Frame.__init__( self, None, -1, "Basic Grid Sizer" )
		sizer = wx.GridSizer( rows=3, cols=3, hgap=5, vgap=5 )
		for label in labels:
			bw = BlockWindow( self, label=label )
			sizer.Add( bw, 0, 0 )
		self.SetSizer( sizer )
		self.Fit()

app = wx.PySimpleApp()
GridSizerFrame().Show()
app.MainLoop()
