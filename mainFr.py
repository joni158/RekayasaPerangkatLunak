#Boa:Frame:mainFr

import wx, karyawanFr, gajiFr, hitungGajiFr

def create(parent):
    return mainFr(parent)

[wxID_MAINFR, wxID_MAINFRBTNHITUNGGAJI, wxID_MAINFRIMGMAIN, wxID_MAINFRPANEL1, 
 wxID_MAINFRSTATICTEXT1, wxID_MAINFRSTATICTEXT2, wxID_MAINFRTMBEXIT, 
 wxID_MAINFRTMBKARYAWAN, wxID_MAINFRTMBPOSISI, 
] = [wx.NewId() for _init_ctrls in range(9)]

class mainFr(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFR, name='mainFr', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1320, 780),
              style=wx.DEFAULT_FRAME_STYLE, title='Main Menu')
        self.SetClientSize(wx.Size(1304, 742))
        self.SetBackgroundColour(wx.Colour(253, 172, 206))

        self.panel1 = wx.Panel(id=wxID_MAINFRPANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1304, 742),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetAutoLayout(False)
        self.panel1.SetBackgroundColour(wx.Colour(230, 230, 255))
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))
        self.panel1.SetHelpText('')

        self.staticText1 = wx.StaticText(id=wxID_MAINFRSTATICTEXT1,
              label='Sistem Informasi Penggajian Karyawan', name='staticText1',
              parent=self.panel1, pos=wx.Point(472, 168), size=wx.Size(388, 29),
              style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))
        self.staticText1.Enable(True)

        self.staticText2 = wx.StaticText(id=wxID_MAINFRSTATICTEXT2,
              label='PERUSAHAAN PENERBIT MAJALAH AR-RISALLAH ',
              name='staticText2', parent=self.panel1, pos=wx.Point(472, 208),
              size=wx.Size(491, 29), style=0)
        self.staticText2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.tmbKaryawan = wx.Button(id=wxID_MAINFRTMBKARYAWAN,
              label='Karyawan', name='tmbKaryawan', parent=self.panel1,
              pos=wx.Point(512, 296), size=wx.Size(112, 80), style=0)
        self.tmbKaryawan.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))
        self.tmbKaryawan.SetHelpText('')
        self.tmbKaryawan.SetBackgroundColour(wx.Colour(255, 128, 128))
        self.tmbKaryawan.Bind(wx.EVT_BUTTON, self.OnTmbKaryawanButton,
              id=wxID_MAINFRTMBKARYAWAN)

        self.tmbPosisi = wx.Button(id=wxID_MAINFRTMBPOSISI, label='Posisi',
              name='tmbPosisi', parent=self.panel1, pos=wx.Point(672, 296),
              size=wx.Size(112, 80), style=0)
        self.tmbPosisi.SetBackgroundColour(wx.Colour(128, 128, 255))
        self.tmbPosisi.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Calibri'))
        self.tmbPosisi.Bind(wx.EVT_BUTTON, self.OnTmbPosisiButton,
              id=wxID_MAINFRTMBPOSISI)

        self.tmbExit = wx.Button(id=wxID_MAINFRTMBEXIT, label='Exit',
              name='tmbExit', parent=self.panel1, pos=wx.Point(672, 416),
              size=wx.Size(112, 80), style=0)
        self.tmbExit.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Calibri'))
        self.tmbExit.SetBackgroundColour(wx.Colour(255, 128, 64))
        self.tmbExit.Bind(wx.EVT_BUTTON, self.OnTmbExitButton,
              id=wxID_MAINFRTMBEXIT)

        self.btnHitungGaji = wx.Button(id=wxID_MAINFRBTNHITUNGGAJI,
              label='Hitung Gaji', name='btnHitungGaji', parent=self.panel1,
              pos=wx.Point(512, 416), size=wx.Size(112, 80), style=0)
        self.btnHitungGaji.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))
        self.btnHitungGaji.SetBackgroundColour(wx.Colour(52, 203, 162))
        self.btnHitungGaji.Bind(wx.EVT_BUTTON, self.OnBtnHitungGajiButton,
              id=wxID_MAINFRBTNHITUNGGAJI)

        self.imgMain = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_MAINFRIMGMAIN, name='imgMain', parent=self.panel1,
              pos=wx.Point(280, 136), size=wx.Size(16, 16), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        #Displaying image
        filepath = 'C:\\SI Ar-Risallah\Images\karyawan.jpg'
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        self.imgMain.SetBitmap(wx.BitmapFromImage(img))

    def OnTmbPosisiButton(self, event):
        self.main = gajiFr.create(None)
        self.main.Show()
        self.Close()

    def OnTmbKaryawanButton(self, event):
        self.main = karyawanFr.create(None)
        self.main.Show()
        self.Close()

    def OnTmbExitButton(self, event):
        self.Close()

    def OnBtnHitungGajiButton(self, event):
        self.main = hitungGajiFr.create(None)
        self.main.Show()
        self.Close()


        
