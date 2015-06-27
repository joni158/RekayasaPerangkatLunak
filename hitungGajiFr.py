#Boa:Frame:hitungGajiFr

import wx, MySQLdb, mainFr, os, datetime
from xlwt import *

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="penggajian")
cur = conn.cursor()

def create(parent):
    return hitungGajiFr(parent)

[wxID_HITUNGGAJIFR, wxID_HITUNGGAJIFRBTNCETAK, wxID_HITUNGGAJIFRCMBPOSISI, 
 wxID_HITUNGGAJIFRDATE_TODAY, wxID_HITUNGGAJIFRIMGHITUNG, 
 wxID_HITUNGGAJIFRLC_HITUNG, wxID_HITUNGGAJIFRPANEL1, 
 wxID_HITUNGGAJIFRSTATICLINE1, wxID_HITUNGGAJIFRSTATICLINE2, 
 wxID_HITUNGGAJIFRSTATICLINE3, wxID_HITUNGGAJIFRSTATICLINE4, 
 wxID_HITUNGGAJIFRSTATICTEXT1, wxID_HITUNGGAJIFRSTATICTEXT10, 
 wxID_HITUNGGAJIFRSTATICTEXT11, wxID_HITUNGGAJIFRSTATICTEXT2, 
 wxID_HITUNGGAJIFRSTATICTEXT3, wxID_HITUNGGAJIFRSTATICTEXT4, 
 wxID_HITUNGGAJIFRSTATICTEXT5, wxID_HITUNGGAJIFRSTATICTEXT6, 
 wxID_HITUNGGAJIFRSTATICTEXT7, wxID_HITUNGGAJIFRSTATICTEXT8, 
 wxID_HITUNGGAJIFRSTATICTEXT9, wxID_HITUNGGAJIFRTMBBACK, 
 wxID_HITUNGGAJIFRTMBCLEAR, wxID_HITUNGGAJIFRTMBHAPUS, 
 wxID_HITUNGGAJIFRTMBKELUAR, wxID_HITUNGGAJIFRTMBTAMBAH, 
 wxID_HITUNGGAJIFRTXT_GAJI, wxID_HITUNGGAJIFRTXT_JAM, 
 wxID_HITUNGGAJIFRTXT_LEMBUR, wxID_HITUNGGAJIFRTXT_NAMA, 
 wxID_HITUNGGAJIFRTXT_NIK, wxID_HITUNGGAJIFRTXT_NO_NOTA, 
 wxID_HITUNGGAJIFRTXT_TOTAL, wxID_HITUNGGAJIFRTXT_TUNJANGAN, 
] = [wx.NewId() for _init_ctrls in range(35)]

class hitungGajiFr(wx.Frame):
    def _init_coll_lc_hitung_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='NIK',
              width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Nama',
              width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Posisi',
              width=150)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Total  Gaji', width=150)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_HITUNGGAJIFR, name='hitungGajiFr',
              parent=prnt, pos=wx.Point(-8, -8), size=wx.Size(1320, 780),
              style=wx.DEFAULT_FRAME_STYLE, title='Hitung Gaji')
        self.SetClientSize(wx.Size(1304, 742))

        self.panel1 = wx.Panel(id=wxID_HITUNGGAJIFRPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1304, 742),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(230, 230, 255))

        self.staticLine1 = wx.StaticLine(id=wxID_HITUNGGAJIFRSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(129, 48),
              size=wx.Size(1039, 2), style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_HITUNGGAJIFRSTATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(128, 48),
              size=wx.Size(1, 624), style=0)

        self.staticLine3 = wx.StaticLine(id=wxID_HITUNGGAJIFRSTATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(128, 672),
              size=wx.Size(1040, 2), style=0)

        self.staticLine4 = wx.StaticLine(id=wxID_HITUNGGAJIFRSTATICLINE4,
              name='staticLine4', parent=self.panel1, pos=wx.Point(1168, 48),
              size=wx.Size(1, 624), style=0)

        self.staticText1 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT1,
              label='No. Nota', name='staticText1', parent=self.panel1,
              pos=wx.Point(160, 88), size=wx.Size(57, 19), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_no_nota = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_NO_NOTA,
              name='txt_no_nota', parent=self.panel1, pos=wx.Point(160, 120),
              size=wx.Size(112, 24), style=0, value='')
        self.txt_no_nota.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText2 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT2,
              label='Tanggal', name='staticText2', parent=self.panel1,
              pos=wx.Point(1016, 88), size=wx.Size(52, 19), style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_NIK = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_NIK, name='txt_NIK',
              parent=self.panel1, pos=wx.Point(160, 208), size=wx.Size(112, 24),
              style=wx.TE_PROCESS_ENTER, value='')
        self.txt_NIK.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.txt_NIK.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_NIKTextEnter,
              id=wxID_HITUNGGAJIFRTXT_NIK)

        self.txt_nama = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_NAMA,
              name='txt_nama', parent=self.panel1, pos=wx.Point(288, 208),
              size=wx.Size(112, 24), style=0, value='')
        self.txt_nama.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))

        self.cmbPosisi = wx.ComboBox(choices=[], id=wxID_HITUNGGAJIFRCMBPOSISI,
              name='cmbPosisi', parent=self.panel1, pos=wx.Point(416, 208),
              size=wx.Size(144, 27), style=0, value='')
        self.cmbPosisi.SetLabel('')
        self.cmbPosisi.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_gaji = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_GAJI,
              name='txt_gaji', parent=self.panel1, pos=wx.Point(576, 208),
              size=wx.Size(112, 24), style=0, value='')
        self.txt_gaji.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))

        self.txt_tunjangan = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_TUNJANGAN,
              name='txt_tunjangan', parent=self.panel1, pos=wx.Point(704, 208),
              size=wx.Size(112, 24), style=0, value='')
        self.txt_tunjangan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_lembur = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_LEMBUR,
              name='txt_lembur', parent=self.panel1, pos=wx.Point(832, 208),
              size=wx.Size(112, 24), style=0, value='')
        self.txt_lembur.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_jam = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_JAM, name='txt_jam',
              parent=self.panel1, pos=wx.Point(960, 208), size=wx.Size(80, 24),
              style=0, value='')
        self.txt_jam.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))

        self.tmbTambah = wx.Button(id=wxID_HITUNGGAJIFRTMBTAMBAH,
              label='Tambah', name='tmbTambah', parent=self.panel1,
              pos=wx.Point(1056, 208), size=wx.Size(75, 26), style=0)
        self.tmbTambah.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.tmbTambah.Bind(wx.EVT_BUTTON, self.OnTmbTambahButton,
              id=wxID_HITUNGGAJIFRTMBTAMBAH)

        self.staticText3 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT3,
              label='NIK   (ENTER)', name='staticText3', parent=self.panel1,
              pos=wx.Point(160, 176), size=wx.Size(87, 19), style=0)
        self.staticText3.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText4 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT4,
              label='Nama', name='staticText4', parent=self.panel1,
              pos=wx.Point(288, 176), size=wx.Size(38, 19), style=0)
        self.staticText4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText5 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT5,
              label='Posisi', name='staticText5', parent=self.panel1,
              pos=wx.Point(416, 176), size=wx.Size(38, 19), style=0)
        self.staticText5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText6 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT6,
              label='Gaji Pokok', name='staticText6', parent=self.panel1,
              pos=wx.Point(576, 176), size=wx.Size(68, 19), style=0)
        self.staticText6.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText7 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT7,
              label='Tunjangan', name='staticText7', parent=self.panel1,
              pos=wx.Point(704, 176), size=wx.Size(68, 19), style=0)
        self.staticText7.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText8 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT8,
              label='Lembur', name='staticText8', parent=self.panel1,
              pos=wx.Point(832, 176), size=wx.Size(49, 19), style=0)
        self.staticText8.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText9 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT9,
              label='Jam', name='staticText9', parent=self.panel1,
              pos=wx.Point(960, 176), size=wx.Size(25, 19), style=0)
        self.staticText9.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.lc_hitung = wx.ListCtrl(id=wxID_HITUNGGAJIFRLC_HITUNG,
              name='lc_hitung', parent=self.panel1, pos=wx.Point(160, 264),
              size=wx.Size(560, 368), style=wx.LC_REPORT)
        self.lc_hitung.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self._init_coll_lc_hitung_Columns(self.lc_hitung)
        self.lc_hitung.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_hitungListItemSelected, id=wxID_HITUNGGAJIFRLC_HITUNG)

        self.tmbClear = wx.Button(id=wxID_HITUNGGAJIFRTMBCLEAR, label='Clear',
              name='tmbClear', parent=self.panel1, pos=wx.Point(768, 304),
              size=wx.Size(88, 26), style=0)
        self.tmbClear.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.tmbClear.Bind(wx.EVT_BUTTON, self.OnTmbClearButton,
              id=wxID_HITUNGGAJIFRTMBCLEAR)

        self.btnCetak = wx.Button(id=wxID_HITUNGGAJIFRBTNCETAK, label='Cetak',
              name='btnCetak', parent=self.panel1, pos=wx.Point(768, 360),
              size=wx.Size(88, 26), style=0)
        self.btnCetak.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnCetak.Bind(wx.EVT_BUTTON, self.OnBtnCetakButton,
              id=wxID_HITUNGGAJIFRBTNCETAK)

        self.tmbHapus = wx.Button(id=wxID_HITUNGGAJIFRTMBHAPUS, label='Hapus',
              name='tmbHapus', parent=self.panel1, pos=wx.Point(768, 416),
              size=wx.Size(88, 26), style=0)
        self.tmbHapus.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.tmbHapus.Bind(wx.EVT_BUTTON, self.OnTmbHapusButton,
              id=wxID_HITUNGGAJIFRTMBHAPUS)

        self.tmbBack = wx.Button(id=wxID_HITUNGGAJIFRTMBBACK, label='Back',
              name='tmbBack', parent=self.panel1, pos=wx.Point(816, 512),
              size=wx.Size(100, 80), style=0)
        self.tmbBack.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.tmbBack.Bind(wx.EVT_BUTTON, self.OnTmbBackButton,
              id=wxID_HITUNGGAJIFRTMBBACK)

        self.tmbKeluar = wx.Button(id=wxID_HITUNGGAJIFRTMBKELUAR,
              label='Keluar', name='tmbKeluar', parent=self.panel1,
              pos=wx.Point(976, 512), size=wx.Size(100, 80), style=0)
        self.tmbKeluar.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.tmbKeluar.Bind(wx.EVT_BUTTON, self.OnTmbKeluarButton,
              id=wxID_HITUNGGAJIFRTMBKELUAR)

        self.staticText10 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT10,
              label='TOTAL', name='staticText10', parent=self.panel1,
              pos=wx.Point(904, 256), size=wx.Size(71, 33), style=0)
        self.staticText10.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_total = wx.TextCtrl(id=wxID_HITUNGGAJIFRTXT_TOTAL,
              name='txt_total', parent=self.panel1, pos=wx.Point(904, 304),
              size=wx.Size(184, 56), style=0, value='')
        self.txt_total.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText11 = wx.StaticText(id=wxID_HITUNGGAJIFRSTATICTEXT11,
              label='GAJI KARYAWAN', name='staticText11', parent=self.panel1,
              pos=wx.Point(528, 56), size=wx.Size(207, 36), style=0)
        self.staticText11.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.date_today = wx.DatePickerCtrl(id=wxID_HITUNGGAJIFRDATE_TODAY,
              name='date_today', parent=self.panel1, pos=wx.Point(1016, 120),
              size=wx.Size(112, 24), style=wx.DP_SHOWCENTURY)
        self.date_today.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.imgHitung = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_HITUNGGAJIFRIMGHITUNG, name='imgHitung',
              parent=self.panel1, pos=wx.Point(144, 40), size=wx.Size(16, 16),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        #Displaying number of Nota
        sqlA = "SELECT * FROM gajikaryawan"
        cur.execute(sqlA)
        numNota = cur.rowcount
        self.txt_no_nota.SetValue(str(numNota + 1))  
        
        #Read all combobox data (posisitions) from database
        sqlB = "SELECT * FROM posisikaryawan"
        cur.execute(sqlB)
        hasilB = cur.fetchall()
        posisiDb = []
        for i in hasilB:
            nama_posisiDb = i[1]
            self.cmbPosisi.Append("%s"%nama_posisiDb)
            posisiDb.append(nama_posisiDb)
        self.cmbPosisi.SetStringSelection(posisiDb[0]) 
        
        #Displaying data in database to ListCtrl
        sqlC = "SELECT datakaryawan.NIK, datakaryawan.nama, posisikaryawan.nama_posisi, \
        gajikaryawan.total_gaji FROM datakaryawan, posisikaryawan, gajikaryawan \
        WHERE datakaryawan.NIK=gajikaryawan.NIKFK AND gajikaryawan.ID_posisiFK=posisikaryawan.ID_posisi"
        cur.execute(sqlC)
        hasilB = cur.fetchall()
        p = self.lc_hitung.GetItemCount()
        for j in hasilB :
            self.lc_hitung.InsertStringItem(p,"%s"%str(j[0]))
            self.lc_hitung.SetStringItem(p,1,"%s"%j[1])
            self.lc_hitung.SetStringItem(p,2,"%s"%str(j[2]))
            self.lc_hitung.SetStringItem(p,3,"%s"%str(j[3]))
            p = p + 1
        
    def bersih(self):
        self.txt_NIK.SetValue("")
        self.txt_nama.SetValue("")
        self.cmbPosisi.SetStringSelection("Manager")
        self.txt_gaji.SetValue("")
        self.txt_tunjangan.SetValue("")
        self.txt_lembur.SetValue("")
        self.txt_jam.SetValue("")
        self.txt_total.SetValue("")
        
        sqlA = "SELECT * FROM gajikaryawan"
        cur.execute(sqlA)
        numNota = cur.rowcount
        self.txt_no_nota.SetValue(str(numNota + 1))
        
    def inputToLc(self):
        #Prepare some variable needed that want to be iputted to LC
        NIK = self.txt_NIK.GetValue()
        nama = self.txt_nama.GetValue()
        posisi = self.cmbPosisi.GetStringSelection()
        total = self.txt_total.GetValue()
        
        #Input data with indeks
        numRow = self.lc_hitung.GetItemCount()
        self.lc_hitung.InsertStringItem(numRow, NIK)
        self.lc_hitung.SetStringItem(numRow,1,nama)
        self.lc_hitung.SetStringItem(numRow,2,posisi)
        self.lc_hitung.SetStringItem(numRow,3,total)
        numRow = numRow + 1
        
    def OnTxt_NIKTextEnter(self, event): 
        #Declaring some variables needed       
        intNIK = int(self.txt_NIK.GetValue())
              
        #When Press Enter on NIK textfield, it will show the other data needed
        sqlA = "SELECT datakaryawan.nama, posisikaryawan.nama_posisi, posisikaryawan.gaji_posisi, \
                posisikaryawan.tunjangan_posisi, posisikaryawan.lembur_posisi \
                FROM datakaryawan, posisikaryawan WHERE datakaryawan.NIK = '%d' AND \
                datakaryawan.ID_posisiFK = posisikaryawan.ID_posisi"%(intNIK)
        cur.execute(sqlA)
        hasilA = cur.fetchall()
        for i in hasilA :
            self.txt_nama.SetValue(i[0])
            self.cmbPosisi.SetStringSelection(i[1])
            self.txt_gaji.SetValue(str(i[2]))
            self.txt_tunjangan.SetValue(str(i[3]))
            self.txt_lembur.SetValue(str(i[4]))

    def OnTmbTambahButton(self, event):
        #Declaring some variable needed to be calculated
        gaji = int(self.txt_gaji.GetValue())
        tunjangan = int(self.txt_tunjangan.GetValue())
        lembur = int(self.txt_lembur.GetValue())
        jam = int(self.txt_jam.GetValue())
        
        #Calculate the variable to get total
        if self.txt_jam.GetValue() == "":
            hasil = gaji + tunjangan
        else:
            hasil = gaji + tunjangan + (lembur * jam)
        
        #Print the result in the textfield of TOTAL
        self.txt_total.SetValue(str(hasil))
        
        #Add the data that already calculated to list ctrl
        self.inputToLc()
        
        #Saving to database
        intNota = int(self.txt_no_nota.GetValue())
        intNIKFK = int(self.txt_NIK.GetValue())
        intTotal = int(self.txt_total.GetValue())
        
        sqlA = "SELECT * FROM datakaryawan WHERE NIK = '%d'"%(intNIKFK)
        cur.execute(sqlA)
        hasilA = cur.fetchall()
        for i in hasilA :
            IDposisiFK = i[8]
                    
        sqlB = "SELECT * FROM gajikaryawan WHERE nota = '%d'" %(intNota)
        cur.execute(sqlB)
        hasilB = cur.fetchone()
        
        if cur.rowcount > 0 :
            sqlC = "UPDATE gajikaryawan\
                    SET total_gaji ='%d', jam = '%d', NIKFK = '%d', , \
                    ID_posisiFK ='%d' WHERE nota ='%d'"\
                    %(intTotal, jam, intNIKFK, IDposisiFK, intNota)
        else:
            sqlC = "INSERT INTO gajikaryawan (nota, total_gaji, jam, NIKFK, ID_posisiFK) \
                    VALUES ('%d','%d','%d','%d','%d')"\
                    %(intNota, intTotal, jam, intNIKFK, IDposisiFK)
                    
        cur.execute(sqlC)
        conn.commit()

    def OnTmbBackButton(self, event):
        self.main = mainFr.create(None)
        self.main.Show()
        self.Close()

    def OnTmbKeluarButton(self, event):
        self.Close()

    def OnTmbClearButton(self, event):
        self.bersih()

    def OnTmbCetakButton(self, event):
        event.Skip()

    def OnTmbHapusButton(self, event):
        #Confirmation of data deletion  
        
        intNota = int(self.txt_no_nota.GetValue())
        
        if self.txt_NIK.GetValue() == "" :
            self.pesan = wx.MessageDialog(self, "ID Posisi Belum Diisi !", "Peringatan",wx.OK)
            self.pesan.ShowModal()
            event.Skip()
        sql = "SELECT * FROM gajikaryawan WHERE nota = '%d'"%(intNota)
        cur.execute(sql)
        hasil = cur.fetchone()
        if cur.rowcount > 0 :
            tanya = wx.MessageDialog(self, message="Anda Yakin Menghapus Posisi Ini ?",\
            style = wx.YES_NO)
            if tanya.ShowModal() == wx.ID_YES :
                sql = "DELETE FROM gajikaryawan WHERE nota = '%s'"%(intNota)
                cur.execute(sql)
                conn.commit()
                
        else :
            self.pesan = wx.MessageDialog(self,"NIK Yang Akan Dihapus Tidak Terdata.",\
            "Konfirmasi",wx.OK)
            self.pesan.ShowModal()
        self.bersih()

    def OnLc_hitungListItemSelected(self, event):
        rowNumLc = event.m_itemIndex
        IDNIKFK = int(self.lc_hitung.GetItem(rowNumLc,0).GetText())
        
        #indexing data that want to take by using intNIK 
        sqlA = "SELECT gajikaryawan.nota, datakaryawan.NIK, datakaryawan.nama, \
        posisikaryawan.nama_posisi, gajikaryawan.jam, gajikaryawan.total_gaji \
        FROM datakaryawan, posisikaryawan, gajikaryawan WHERE gajikaryawan.NIKFK = '%d' \
        AND gajikaryawan.NIKFK = datakaryawan.NIK AND gajikaryawan.ID_posisiFK = \
        posisikaryawan.ID_posisi"%IDNIKFK
        cur.execute(sqlA)
        hasilA = cur.fetchall()
        for i in hasilA :
            self.txt_no_nota.SetValue(str(i[0]))
            self.txt_NIK.SetValue(str(i[1]))
            self.txt_nama.SetValue(i[2])
            self.cmbPosisi.SetStringSelection(i[3])
            self.txt_jam.SetValue(str(i[4]))
            self.txt_total.SetValue(str(i[5]))
            
            if self.cmbPosisi.GetStringSelection() == i[3] :
                sqlB = "SELECT gaji_posisi,tunjangan_posisi,lembur_posisi FROM posisikaryawan \
                WHERE nama_posisi = '%s'"%(i[3])
                cur.execute(sqlB)
                hasilB = cur.fetchall()
                for i in hasilB :
                    self.txt_gaji.SetValue(str(i[0]))
                    self.txt_tunjangan.SetValue(str(i[1]))
                    self.txt_lembur.SetValue(str(i[2]))

    def OnBtnCetakButton(self, event):
        #Making a new workbook
        laporanBook = Workbook()
        
        #Making a new sheet
        nama = self.txt_nama.GetValue()
        
        #Read date become string
        selectedDate = self.date_today.GetValue()
        month_today = str(selectedDate.Month + 1)
        day_today = str(selectedDate.Day)
        year_today = str(selectedDate.Year)
        
        word = ""
        for vowel in range(len(nama)):
            if nama[vowel] == " ":
                break
            word = word + nama[vowel]
        newSheet = month_today + word
        
        sheet1 = laporanBook.add_sheet(newSheet)
        
        #Setting font header
        font_judul = Font()
        font_judul.name = "Arial"
        font_judul.height = 350
        font_judul.bold = True
        
        #Setting font1
        font1 = Font()
        font1.bold = True
        font1.height = 250
        
        #Setting font2
        font2 = Font()
        font2.bold = True
        font2.height = 300
        
        #Setting style_judul
        style_judul = XFStyle()
        style_judul.font = font_judul
        
        #Setting border1
        borders1 = Borders()
        borders1.left = 1; borders1.right = 1
        borders1.top = 1; borders1.bottom = 1
        
        #Setting borders2
        borders2 = Borders()
        borders2.left = 1
        borders2.top = 1; borders2.bottom = 1
        
        #Setting borders3
        borders3 = Borders()
        borders3.right = 1
        borders3.top = 1; borders3.bottom = 1
        
        #Setting borders4
        borders4 = Borders()
        borders4.top = 1; borders4.bottom = 1
        
        #Setting Pattern
        BkgPat1 = Pattern()
        BkgPat1.pattern = Pattern.SOLID_PATTERN
        BkgPat1.pattern_fore_colour = 22
        
        #Setting style1
        style1 = XFStyle()
        style1.borders = borders1
        
        #Setting style2
        style2 = XFStyle()
        style2.borders = borders2
        style2.font = font1
        style2.pattern = BkgPat1
        
        #Setting style3
        style3 = XFStyle()
        style3.borders = borders3
        style3.font = font1
        style3.pattern = BkgPat1
        
        #Setting style4
        style4 = XFStyle()
        style4.borders = borders4
        style4.font = font1
        style4.pattern = BkgPat1
        
        #Setting style_total1
        style_total1 = XFStyle()
        style_total1.borders = borders2
        style_total1.font = font2
        
        #Setting style_total2
        style_total2 = XFStyle()
        style_total2.borders = borders3
        style_total2.font = font2
        
        #Setting style_total3
        style_total3 = XFStyle()
        style_total3.borders = borders4
        style_total3.font = font2
        
        #Setting width of columns
        sheet1.col(0).width = 4700
        sheet1.col(1).width = 1000
        sheet1.col(2).width = 10000
        sheet1.col(3).width = 1000
        sheet1.col(4).width = 4000
        sheet1.col(5).width = 1000
        sheet1.col(6).width = 5000
        
        #Writing Header
        sheet1.write(0,2,"Laporan Gaji Karyawan",style_judul)
        
        i=0
        sheet1.write(3,i,"No.Nota")
        
        sheet1.write(5,i,"Data Karyawan",style2)
        sheet1.write(6,i,"NIK",style1)
        sheet1.write(7,i,"Nama",style1)
        sheet1.write(8,i,"Alamat",style1)
        sheet1.write(9,i,"Handphone",style1)
        sheet1.write(10,i,"Posisi",style1)
        
        j=1
        sheet1.write(3,j,":")
        sheet1.write(5,j,"",style4)
        row = 5
        for a in range(row):
            sheet1.write(a+6,j,":",style1)
        
        k=2
        sheet1.write(3,k,self.txt_no_nota.GetValue())
        
        sheet1.write(5,k,"",style3)
        sheet1.write(6,k,self.txt_NIK.GetValue(),style1)
        sheet1.write(7,k,self.txt_nama.GetValue(),style1)
        sheet1.write(10,k,self.cmbPosisi.GetStringSelection(),style1)
        sqlA = "SELECT alamat, telepon FROM datakaryawan WHERE NIK = '%d'"%(int(self.txt_NIK.GetValue()))
        cur.execute(sqlA)
        hasilA = cur.fetchall()
        for p in hasilA:
            sheet1.write(8,k,p[0],style1)
            sheet1.write(9,k,p[1],style1)
            
        l=4
        sheet1.write(3,l,"Tanggal")
        
        sheet1.write(5,l,"Data Gaji",style2)
        sheet1.write(6,l,"Gaji Pokok",style1)
        sheet1.write(7,l,"Tunjangan",style1)
        sheet1.write(8,l,"Lembur",style1)
        sheet1.write(9,l,"Jam",style1)
        sheet1.write(10,l,"Total",style1)
        sheet1.write(13,l,"TOTAL",style_total1)
        
        m=5
        sheet1.write(3,m,":")
        sheet1.write(5,m,"",style4)
        row = 5
        for b in range(row):
            sheet1.write(b+6,m,":",style1)
        sheet1.write(13,m,"",style_total3)
        
        n=6
        sheet1.write(3,n,day_today+"-"+month_today+"-"+year_today)
        
        sheet1.write(5,n,"",style3)
        sheet1.write(6,n,self.txt_gaji.GetValue(),style1)
        sheet1.write(7,n,self.txt_tunjangan.GetValue(),style1)
        sheet1.write(8,n,self.txt_lembur.GetValue(),style1)
        sheet1.write(9,n,self.txt_jam.GetValue(),style1)
        sheet1.write(10,n,self.txt_total.GetValue(),style1)
        sheet1.write(13,n,self.txt_total.GetValue(),style_total2)
        
        #Making a path of file directory
        path1 = 'C:\\Users\Public\\'+newSheet+'.xls'
        laporanBook.save(path1)
        #os.system("start excel.exe '%s'"%path1)
        self.pesan = wx.MessageDialog(self, "File telah disimpan di "+path1, "Konfirmasi",wx.OK)
        self.pesan.ShowModal()
        self.bersih()
        
