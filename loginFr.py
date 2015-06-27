#Boa:Frame:loginFr

import wx, mainFr

def create(parent):
    return loginFr(parent)

[wxID_LOGINFR, wxID_LOGINFRBTNCANCEL, wxID_LOGINFRBTNLOGIN, 
 wxID_LOGINFRPANEL1, wxID_LOGINFRSTATICLINE1, wxID_LOGINFRSTATICLINE2, 
 wxID_LOGINFRSTATICLINE3, wxID_LOGINFRSTATICLINE4, wxID_LOGINFRSTATICTEXT1, 
 wxID_LOGINFRSTATICTEXT2, wxID_LOGINFRSTATICTEXT3, wxID_LOGINFRTXT_PASSWORD, 
 wxID_LOGINFRTXT_USERNAME, 
] = [wx.NewId() for _init_ctrls in range(13)]

class loginFr(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LOGINFR, name='loginFr', parent=prnt,
              pos=wx.Point(501, 162), size=wx.Size(638, 458),
              style=wx.DEFAULT_FRAME_STYLE, title='Login')
        self.SetClientSize(wx.Size(622, 420))
        self.SetBackgroundColour(wx.Colour(253, 172, 206))

        self.panel1 = wx.Panel(id=wxID_LOGINFRPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(622, 420),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(230, 230, 255))
        self.panel1.SetHelpText('')

        self.staticLine1 = wx.StaticLine(id=wxID_LOGINFRSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(49, 80),
              size=wx.Size(519, 2), style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_LOGINFRSTATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(48, 320),
              size=wx.Size(520, 2), style=0)

        self.staticLine3 = wx.StaticLine(id=wxID_LOGINFRSTATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(48, 80),
              size=wx.Size(1, 240), style=0)

        self.staticLine4 = wx.StaticLine(id=wxID_LOGINFRSTATICLINE4,
              name='staticLine4', parent=self.panel1, pos=wx.Point(568, 80),
              size=wx.Size(1, 240), style=0)

        self.staticText1 = wx.StaticText(id=wxID_LOGINFRSTATICTEXT1,
              label='Login', name='staticText1', parent=self.panel1,
              pos=wx.Point(56, 24), size=wx.Size(71, 39), style=0)
        self.staticText1.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.staticText2 = wx.StaticText(id=wxID_LOGINFRSTATICTEXT2,
              label='Username', name='staticText2', parent=self.panel1,
              pos=wx.Point(88, 136), size=wx.Size(79, 23), style=0)
        self.staticText2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText3 = wx.StaticText(id=wxID_LOGINFRSTATICTEXT3,
              label='Password', name='staticText3', parent=self.panel1,
              pos=wx.Point(88, 184), size=wx.Size(76, 23), style=0)
        self.staticText3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_username = wx.TextCtrl(id=wxID_LOGINFRTXT_USERNAME,
              name='txt_username', parent=self.panel1, pos=wx.Point(224, 136),
              size=wx.Size(256, 32), style=0, value='')
        self.txt_username.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.txt_username.SetMaxLength(15)

        self.txt_password = wx.TextCtrl(id=wxID_LOGINFRTXT_PASSWORD,
              name='txt_password', parent=self.panel1, pos=wx.Point(224, 184),
              size=wx.Size(256, 32), style=wx.TE_PASSWORD, value='')
        self.txt_password.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.txt_password.SetMaxLength(20)
        
        self.btnLogin = wx.Button(id=wxID_LOGINFRBTNLOGIN, label='Login',
              name='btnLogin', parent=self.panel1, pos=wx.Point(224, 264),
              size=wx.Size(104, 32), style=0)
        self.btnLogin.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnLogin.Bind(wx.EVT_BUTTON, self.OnBtnLoginButton,
              id=wxID_LOGINFRBTNLOGIN)

        self.btnCancel = wx.Button(id=wxID_LOGINFRBTNCANCEL, label='Cancel',
              name='btnCancel', parent=self.panel1, pos=wx.Point(360, 264),
              size=wx.Size(104, 32), style=0)
        self.btnCancel.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnBtnCancelButton,
              id=wxID_LOGINFRBTNCANCEL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def OnBtnLoginButton(self, event):
        if self.txt_username.GetValue() == "joni" and \
        self.txt_password.GetValue() == "12345" :
            self.main = mainFr.create(None)
            self.main.Show()
            self.Close()
        else :
            msg = "Login gagal, username atau password salah !"
            self.pesan = wx.MessageDialog(self, msg, "PESAN", wx.OK)
            self.pesan.ShowModal()

    def OnBtnCancelButton(self, event):
        self.Close()


            
        
        

