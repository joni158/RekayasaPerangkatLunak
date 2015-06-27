#Boa:Frame:gajiFr

import wx, MySQLdb, mainFr, karyawanFr

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="penggajian")
cur = conn.cursor()

def create(parent):
    return gajiFr(parent)

[wxID_GAJIFR, wxID_GAJIFRBTNBACK, wxID_GAJIFRBTNCLEAR, wxID_GAJIFRBTNHAPUS, 
 wxID_GAJIFRBTNKELUAR, wxID_GAJIFRBTNSIMPAN, wxID_GAJIFRBTNVIEWALL, 
 wxID_GAJIFRLC_GAJI, wxID_GAJIFRPANEL1, wxID_GAJIFRSTATICLINE1, 
 wxID_GAJIFRSTATICLINE10, wxID_GAJIFRSTATICLINE11, wxID_GAJIFRSTATICLINE12, 
 wxID_GAJIFRSTATICLINE13, wxID_GAJIFRSTATICLINE2, wxID_GAJIFRSTATICLINE3, 
 wxID_GAJIFRSTATICLINE4, wxID_GAJIFRSTATICLINE5, wxID_GAJIFRSTATICLINE6, 
 wxID_GAJIFRSTATICLINE7, wxID_GAJIFRSTATICLINE8, wxID_GAJIFRSTATICLINE9, 
 wxID_GAJIFRSTATICTEXT1, wxID_GAJIFRSTATICTEXT2, wxID_GAJIFRSTATICTEXT3, 
 wxID_GAJIFRSTATICTEXT4, wxID_GAJIFRSTATICTEXT5, wxID_GAJIFRSTATICTEXT6, 
 wxID_GAJIFRSTATICTEXT7, wxID_GAJIFRSTATICTEXT8, wxID_GAJIFRSTATICTEXT9, 
 wxID_GAJIFRTMBCARI, wxID_GAJIFRTXTCARI, wxID_GAJIFRTXT_ID_POSISI, 
 wxID_GAJIFRTXT_NAMA_POSISI, wxID_GAJIFRTXT_PAR_GAJI, 
 wxID_GAJIFRTXT_PAR_LEMBUR, wxID_GAJIFRTXT_PAR_TUNJANGAN, 
] = [wx.NewId() for _init_ctrls in range(38)]

class gajiFr(wx.Frame):
    def _init_coll_lc_gaji_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='ID Posisi', width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Posisi', width=130)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Gaji Pokok', width=105)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Tunjangan', width=105)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Lembur /Jam', width=110)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_GAJIFR, name='gajiFr', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1320, 784),
              style=wx.DEFAULT_FRAME_STYLE, title='Data Gaji')
        self.SetClientSize(wx.Size(1304, 746))

        self.panel1 = wx.Panel(id=wxID_GAJIFRPANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1304, 746),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(230, 230, 255))

        self.staticText1 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT1,
              label='Formulir Posisi', name='staticText1', parent=self.panel1,
              pos=wx.Point(136, 40), size=wx.Size(126, 26), style=0)
        self.staticText1.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.staticLine1 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(136, 72),
              size=wx.Size(376, 2), style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(136, 72),
              size=wx.Size(1, 568), style=0)

        self.staticLine3 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(136, 640),
              size=wx.Size(376, 2), style=0)

        self.staticLine4 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE4,
              name='staticLine4', parent=self.panel1, pos=wx.Point(512, 72),
              size=wx.Size(1, 568), style=0)

        self.staticText2 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT2,
              label='Pencarian ', name='staticText2', parent=self.panel1,
              pos=wx.Point(536, 40), size=wx.Size(90, 26), style=0)
        self.staticText2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.staticLine5 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE5,
              name='staticLine5', parent=self.panel1, pos=wx.Point(536, 72),
              size=wx.Size(584, 2), style=0)

        self.staticLine6 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE6,
              name='staticLine6', parent=self.panel1, pos=wx.Point(536, 72),
              size=wx.Size(1, 64), style=0)

        self.staticLine7 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE7,
              name='staticLine7', parent=self.panel1, pos=wx.Point(536, 136),
              size=wx.Size(584, 2), style=0)

        self.staticLine8 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE8,
              name='staticLine8', parent=self.panel1, pos=wx.Point(1120, 72),
              size=wx.Size(1, 64), style=0)

        self.staticText3 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT3,
              label='Data', name='staticText3', parent=self.panel1,
              pos=wx.Point(536, 152), size=wx.Size(40, 26), style=0)
        self.staticText3.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.staticText4 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT4,
              label='Posisi', name='staticText4', parent=self.panel1,
              pos=wx.Point(560, 96), size=wx.Size(38, 19), style=0)
        self.staticText4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txtCari = wx.TextCtrl(id=wxID_GAJIFRTXTCARI, name='txtCari',
              parent=self.panel1, pos=wx.Point(648, 96), size=wx.Size(240, 24),
              style=0, value='')
        self.txtCari.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))

        self.staticLine9 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE9,
              name='staticLine9', parent=self.panel1, pos=wx.Point(536, 184),
              size=wx.Size(1, 456), style=0)

        self.staticLine10 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE10,
              name='staticLine10', parent=self.panel1, pos=wx.Point(560, 184),
              size=wx.Size(1, 2), style=0)

        self.staticLine11 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE11,
              name='staticLine11', parent=self.panel1, pos=wx.Point(536, 184),
              size=wx.Size(584, 2), style=0)

        self.staticLine12 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE12,
              name='staticLine12', parent=self.panel1, pos=wx.Point(1120, 184),
              size=wx.Size(1, 456), style=0)

        self.staticLine13 = wx.StaticLine(id=wxID_GAJIFRSTATICLINE13,
              name='staticLine13', parent=self.panel1, pos=wx.Point(536, 640),
              size=wx.Size(584, 2), style=0)

        self.lc_gaji = wx.ListCtrl(id=wxID_GAJIFRLC_GAJI, name='lc_gaji',
              parent=self.panel1, pos=wx.Point(560, 208), size=wx.Size(536,
              408), style=wx.LC_REPORT)
        self.lc_gaji.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self._init_coll_lc_gaji_Columns(self.lc_gaji)
        self.lc_gaji.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_gajiListItemSelected, id=wxID_GAJIFRLC_GAJI)

        self.staticText5 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT5,
              label='ID Posisi', name='staticText5', parent=self.panel1,
              pos=wx.Point(160, 104), size=wx.Size(56, 19), style=0)
        self.staticText5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText6 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT6,
              label='Gaji Pokok', name='staticText6', parent=self.panel1,
              pos=wx.Point(160, 184), size=wx.Size(68, 19), style=0)
        self.staticText6.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText7 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT7,
              label='Tunjangan', name='staticText7', parent=self.panel1,
              pos=wx.Point(160, 224), size=wx.Size(68, 19), style=0)
        self.staticText7.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText8 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT8,
              label='Lembur /Jam', name='staticText8', parent=self.panel1,
              pos=wx.Point(160, 272), size=wx.Size(83, 19), style=0)
        self.staticText8.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_id_posisi = wx.TextCtrl(id=wxID_GAJIFRTXT_ID_POSISI,
              name='txt_id_posisi', parent=self.panel1, pos=wx.Point(288, 104),
              size=wx.Size(200, 26), style=0, value='')
        self.txt_id_posisi.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_nama_posisi = wx.TextCtrl(id=wxID_GAJIFRTXT_NAMA_POSISI,
              name='txt_nama_posisi', parent=self.panel1, pos=wx.Point(288,
              144), size=wx.Size(200, 26), style=0, value='')
        self.txt_nama_posisi.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_par_gaji = wx.TextCtrl(id=wxID_GAJIFRTXT_PAR_GAJI,
              name='txt_par_gaji', parent=self.panel1, pos=wx.Point(288, 184),
              size=wx.Size(200, 26), style=0, value='')
        self.txt_par_gaji.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_par_tunjangan = wx.TextCtrl(id=wxID_GAJIFRTXT_PAR_TUNJANGAN,
              name='txt_par_tunjangan', parent=self.panel1, pos=wx.Point(288,
              224), size=wx.Size(200, 26), style=0, value='')
        self.txt_par_tunjangan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Calibri'))

        self.txt_par_lembur = wx.TextCtrl(id=wxID_GAJIFRTXT_PAR_LEMBUR,
              name='txt_par_lembur', parent=self.panel1, pos=wx.Point(288, 264),
              size=wx.Size(200, 26), style=0, value='')
        self.txt_par_lembur.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.btnClear = wx.Button(id=wxID_GAJIFRBTNCLEAR, label='Clear',
              name='btnClear', parent=self.panel1, pos=wx.Point(168, 336),
              size=wx.Size(75, 30), style=0)
        self.btnClear.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnClear.Bind(wx.EVT_BUTTON, self.OnBtnClearButton,
              id=wxID_GAJIFRBTNCLEAR)

        self.btnSimpan = wx.Button(id=wxID_GAJIFRBTNSIMPAN, label='Simpan',
              name='btnSimpan', parent=self.panel1, pos=wx.Point(280, 336),
              size=wx.Size(75, 30), style=0)
        self.btnSimpan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.btnSimpan.Bind(wx.EVT_BUTTON, self.OnBtnSimpanButton,
              id=wxID_GAJIFRBTNSIMPAN)

        self.btnHapus = wx.Button(id=wxID_GAJIFRBTNHAPUS, label='Hapus',
              name='btnHapus', parent=self.panel1, pos=wx.Point(392, 336),
              size=wx.Size(75, 30), style=0)
        self.btnHapus.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnHapus.Bind(wx.EVT_BUTTON, self.OnBtnHapusButton,
              id=wxID_GAJIFRBTNHAPUS)

        self.btnBack = wx.Button(id=wxID_GAJIFRBTNBACK, label='Back',
              name='btnBack', parent=self.panel1, pos=wx.Point(192, 448),
              size=wx.Size(100, 80), style=0)
        self.btnBack.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnBack.Bind(wx.EVT_BUTTON, self.OnBtnBackButton,
              id=wxID_GAJIFRBTNBACK)

        self.btnKeluar = wx.Button(id=wxID_GAJIFRBTNKELUAR, label='Keluar',
              name='btnKeluar', parent=self.panel1, pos=wx.Point(352, 448),
              size=wx.Size(100, 80), style=0)
        self.btnKeluar.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.btnKeluar.Bind(wx.EVT_BUTTON, self.OnBtnKeluarButton,
              id=wxID_GAJIFRBTNKELUAR)

        self.staticText9 = wx.StaticText(id=wxID_GAJIFRSTATICTEXT9,
              label='Nama Posisi', name='staticText9', parent=self.panel1,
              pos=wx.Point(160, 144), size=wx.Size(80, 19), style=0)
        self.staticText9.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.tmbCari = wx.Button(id=wxID_GAJIFRTMBCARI, label='Cari',
              name='tmbCari', parent=self.panel1, pos=wx.Point(912, 96),
              size=wx.Size(75, 30), style=0)
        self.tmbCari.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.tmbCari.Bind(wx.EVT_BUTTON, self.OnTmbCariButton,
              id=wxID_GAJIFRTMBCARI)

        self.btnViewAll = wx.Button(id=wxID_GAJIFRBTNVIEWALL, label='View All',
              name='btnViewAll', parent=self.panel1, pos=wx.Point(1008, 96),
              size=wx.Size(80, 30), style=0)
        self.btnViewAll.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.btnViewAll.Bind(wx.EVT_BUTTON, self.OnBtnViewAllButton,
              id=wxID_GAJIFRBTNVIEWALL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        #Read all data that saved in database
        sql = "SELECT * FROM posisikaryawan ORDER BY nama_posisi ASC"
        cur.execute(sql)
        hasil = cur.fetchall()
        p = self.lc_gaji.GetItemCount()
        for j in hasil :
            self.lc_gaji.InsertStringItem(p,"%s"%j[0])
            self.lc_gaji.SetStringItem(p,1,"%s"%j[1])
            self.lc_gaji.SetStringItem(p,2,"%s"%j[2])
            self.lc_gaji.SetStringItem(p,3,"%s"%j[3])
            self.lc_gaji.SetStringItem(p,4,"%s"%j[4])
            p = p + 1
        
    def bersih(self):
        self.txt_id_posisi.SetValue("")
        self.txt_nama_posisi.SetValue("")
        self.txt_par_gaji.SetValue("")
        self.txt_par_tunjangan.SetValue("")
        self.txt_par_lembur.SetValue("")
    
    def inputToLc(self):
        #Prepare some variable needed that want to be iputted to LC
        idPosisi = self.txt_id_posisi.GetValue()
        namaPosisi = self.txt_nama_posisi.GetValue()
        gajiPosisi = self.txt_par_gaji.GetValue()
        tunjanganPosisi = self.txt_par_tunjangan.GetValue()
        lemburPosisi = self.txt_par_lembur.GetValue()
        
        #Input data with indeks
        numRow = self.lc_gaji.GetItemCount()
        self.lc_gaji.InsertStringItem(numRow, idPosisi)
        self.lc_gaji.SetStringItem(numRow,1,namaPosisi)
        self.lc_gaji.SetStringItem(numRow,2,gajiPosisi)
        self.lc_gaji.SetStringItem(numRow,3,tunjanganPosisi)
        self.lc_gaji.SetStringItem(numRow,4,lemburPosisi)
        numRow = numRow + 1

    def OnBtnBackButton(self, event):
        self.main = mainFr.create(None)
        self.main.Show()
        self.Close()

    def OnBtnKeluarButton(self, event):
        self.Close()

    def OnBtnClearButton(self, event):
        self.bersih()

    def OnBtnSimpanButton(self, event):
        
        #Convert String Ke Integer
        intID_posisi = int(self.txt_id_posisi.GetValue())
        intgaji_posisi = int(self.txt_par_gaji.GetValue())
        inttunjangan_posisi = int(self.txt_par_tunjangan.GetValue())
        intlembur_posisi = int(self.txt_par_lembur.GetValue())
        
        sqlA = "SELECT * FROM posisikaryawan WHERE ID_posisi = '%d'" %(intID_posisi)
        cur.execute(sqlA)
        hasil = cur.fetchone()
        
        if cur.rowcount > 0 :
            sqlB = "UPDATE posisikaryawan\
                    SET nama_posisi='%s', gaji_posisi='%d', tunjangan_posisi='%d', \
                    lembur_posisi='%d' WHERE ID_posisi='%d'"\
                    %(self.txt_nama_posisi.GetValue(), intgaji_posisi, \
                    inttunjangan_posisi,intlembur_posisi,intID_posisi)
        else:
            sqlB = "INSERT INTO posisikaryawan (ID_posisi,nama_posisi,gaji_posisi, \
                    tunjangan_posisi,lembur_posisi) \
                    VALUES ('%d','%s','%d','%d','%d')"\
                    %(intID_posisi,self.txt_nama_posisi.GetValue(), intgaji_posisi, \
                    inttunjangan_posisi,intlembur_posisi)
                    
        cur.execute(sqlB)
        conn.commit()
        self.inputToLc()
        self.bersih()

    def OnLc_gajiListItemSelected(self, event):
        rowNumLc = event.m_itemIndex
        lcID = int(self.lc_gaji.GetItem(rowNumLc,0).GetText())
        
        #indexing data that want to take by using intNIK 
        sql = "SELECT * FROM posisikaryawan WHERE ID_posisi = '%d'"%lcID
        cur.execute(sql)
        hasil = cur.fetchall()
        for i in hasil :
            self.txt_id_posisi.SetValue(str(i[0]))
            self.txt_nama_posisi.SetValue(i[1])
            self.txt_par_gaji.SetValue(str(i[2]))
            self.txt_par_tunjangan.SetValue(str(i[3]))
            self.txt_par_lembur.SetValue(str(i[4]))

    def OnBtnHapusButton(self, event):
        #Confirmation of data deletion  
        
        intID_posisi = int(self.txt_id_posisi.GetValue())
        
        if self.txt_id_posisi.GetValue() == "" :
            self.pesan = wx.MessageDialog(self, "ID Posisi Belum Diisi !", "Peringatan",wx.OK)
            self.pesan.ShowModal()
            event.Skip()
        sql = "SELECT * FROM posisikaryawan WHERE ID_posisi = '%d'"%(intID_posisi)
        cur.execute(sql)
        hasil = cur.fetchone()
        if cur.rowcount > 0 :
            tanya = wx.MessageDialog(self, message="Anda Yakin Menghapus Posisi Ini ?",\
            style = wx.YES_NO)
            if tanya.ShowModal() == wx.ID_YES :
                sql = "DELETE FROM posisikaryawan WHERE ID_posisi = '%s'"%(intID_posisi)
                cur.execute(sql)
                conn.commit()
                
        else :
            self.pesan = wx.MessageDialog(self,"NIK Yang Akan Dihapus Tidak Terdata.",\
            "Konfirmasi",wx.OK)
            self.pesan.ShowModal()
        self.bersih()

    def OnTmbCariButton(self, event):
        self.lc_gaji.DeleteAllItems()
        sql = "SELECT ID_posisi,nama_posisi,gaji_posisi,tunjangan_posisi,lembur_posisi \
        FROM posisikaryawan WHERE nama_posisi LIKE '%%%s%%' GROUP BY nama_posisi ASC"\
        %(self.txtCari.GetValue())
        cur.execute(sql)
        hasil = cur.fetchall()
        p = self.lc_gaji.GetItemCount()
        for i in hasil:
            self.lc_gaji.InsertStringItem(p,"%s"%i[0])
            self.lc_gaji.SetStringItem(p,1,"%s"%i[1])
            self.lc_gaji.SetStringItem(p,2,"%s"%i[2])
            self.lc_gaji.SetStringItem(p,3,"%s"%i[3])
            self.lc_gaji.SetStringItem(p,4,"%s"%i[4])
            p = p + 1

    def OnBtnViewAllButton(self, event):
        self.lc_gaji.DeleteAllItems()
        sql = "SELECT ID_posisi,nama_posisi,gaji_posisi,tunjangan_posisi,lembur_posisi \
        FROM posisikaryawan GROUP BY nama_posisi ASC"
        cur.execute(sql)
        hasil = cur.fetchall()
        p = self.lc_gaji.GetItemCount()
        for i in hasil:
            self.lc_gaji.InsertStringItem(p,"%s"%i[0])
            self.lc_gaji.SetStringItem(p,1,"%s"%i[1])
            self.lc_gaji.SetStringItem(p,2,"%s"%i[2])
            self.lc_gaji.SetStringItem(p,3,"%s"%i[3])
            self.lc_gaji.SetStringItem(p,4,"%s"%i[4])
            p = p + 1
        self.txtCari.SetValue("")
        
