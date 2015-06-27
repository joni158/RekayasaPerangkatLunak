#!/usr/bin/env python
#Boa:App:BoaApp

import wx, loginFr, mainFr, karyawanFr, gajiFr, hitungGajiFr

modules ={u'loginFr': [1, 'Main frame of Application', u'loginFr.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = loginFr.create(None)
        self.main.Show() 
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
