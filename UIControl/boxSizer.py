
"""The mul-image demo."""

import wx

class MyPanel( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__( self, parent, -1 )

		self.image1 = wx.Image( '0.jpg', wx.BITMAP_TYPE_JPEG )
		self.image2 = wx.Image( '00.jpg', wx.BITMAP_TYPE_JPEG )
		tmp1 = self.image.ConvertToBitmap()
		tmp2 = self.image.ConvertToBitmap()
		
		


