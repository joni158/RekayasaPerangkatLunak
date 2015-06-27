#Boa:Frame:karyawanFr

import wx, mainFr, MySQLdb, datetime

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="penggajian")
cur = conn.cursor()

def create(parent):
    return karyawanFr(parent)

[wxID_KARYAWANFR, wxID_KARYAWANFRBTNCARI, wxID_KARYAWANFRBTNCLEAR, 
 wxID_KARYAWANFRBTNHAPUS, wxID_KARYAWANFRBTNSIMPAN, wxID_KARYAWANFRBTNVIEWALL, 
 wxID_KARYAWANFRCMBPOSISI, wxID_KARYAWANFRDATE_LAHIR, 
 wxID_KARYAWANFRDATE_MASUK, wxID_KARYAWANFRLC_DATA, wxID_KARYAWANFRPANEL1, 
 wxID_KARYAWANFRRLAKI, wxID_KARYAWANFRRPEREMPUAN, wxID_KARYAWANFRSTATICLINE1, 
 wxID_KARYAWANFRSTATICLINE10, wxID_KARYAWANFRSTATICLINE11, 
 wxID_KARYAWANFRSTATICLINE12, wxID_KARYAWANFRSTATICLINE13, 
 wxID_KARYAWANFRSTATICLINE14, wxID_KARYAWANFRSTATICLINE15, 
 wxID_KARYAWANFRSTATICLINE2, wxID_KARYAWANFRSTATICLINE3, 
 wxID_KARYAWANFRSTATICLINE4, wxID_KARYAWANFRSTATICLINE5, 
 wxID_KARYAWANFRSTATICLINE6, wxID_KARYAWANFRSTATICLINE7, 
 wxID_KARYAWANFRSTATICLINE8, wxID_KARYAWANFRSTATICLINE9, 
 wxID_KARYAWANFRSTATICTEXT1, wxID_KARYAWANFRSTATICTEXT10, 
 wxID_KARYAWANFRSTATICTEXT11, wxID_KARYAWANFRSTATICTEXT12, 
 wxID_KARYAWANFRSTATICTEXT13, wxID_KARYAWANFRSTATICTEXT14, 
 wxID_KARYAWANFRSTATICTEXT15, wxID_KARYAWANFRSTATICTEXT16, 
 wxID_KARYAWANFRSTATICTEXT2, wxID_KARYAWANFRSTATICTEXT3, 
 wxID_KARYAWANFRSTATICTEXT4, wxID_KARYAWANFRSTATICTEXT5, 
 wxID_KARYAWANFRSTATICTEXT6, wxID_KARYAWANFRSTATICTEXT7, 
 wxID_KARYAWANFRSTATICTEXT8, wxID_KARYAWANFRSTATICTEXT9, 
 wxID_KARYAWANFRTMBKELUAR, wxID_KARYAWANFRTMNBACK, wxID_KARYAWANFRTXTCARI, 
 wxID_KARYAWANFRTXT_ALAMAT, wxID_KARYAWANFRTXT_GAJI, 
 wxID_KARYAWANFRTXT_LEMBUR, wxID_KARYAWANFRTXT_NAMA, wxID_KARYAWANFRTXT_NIK, 
 wxID_KARYAWANFRTXT_TELEPON, wxID_KARYAWANFRTXT_TEMPAT_LAHIR, 
 wxID_KARYAWANFRTXT_TUNJANGAN, 
] = [wx.NewId() for _init_ctrls in range(55)]

class karyawanFr(wx.Frame):
    def _init_coll_lc_data_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='NIK',
              width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Nama',
              width=180)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Posisi',
              width=170)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_KARYAWANFR, name='karyawanFr',
              parent=prnt, pos=wx.Point(-8, -8), size=wx.Size(1320, 780),
              style=wx.DEFAULT_FRAME_STYLE, title='Data Karyawan')
        self.SetClientSize(wx.Size(1304, 742))

        self.panel1 = wx.Panel(id=wxID_KARYAWANFRPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1304, 742),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(230, 230, 255))
        self.panel1.SetAutoLayout(False)

        self.staticText1 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT1,
              label='Tambah Karyawan', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 32), size=wx.Size(159, 26), style=0)
        self.staticText1.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.staticLine1 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(33, 64),
              size=wx.Size(391, 2), style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(32, 64),
              size=wx.Size(1, 632), style=0)

        self.staticLine3 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(424, 64),
              size=wx.Size(1, 632), style=0)

        self.staticLine4 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE4,
              name='staticLine4', parent=self.panel1, pos=wx.Point(32, 696),
              size=wx.Size(392, 2), style=0)

        self.staticText2 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT2,
              label='Cari Karyawan', name='staticText2', parent=self.panel1,
              pos=wx.Point(448, 32), size=wx.Size(123, 26), style=0)
        self.staticText2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.staticLine5 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE5,
              name='staticLine5', parent=self.panel1, pos=wx.Point(449, 64),
              size=wx.Size(551, 2), style=0)

        self.staticLine6 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE6,
              name='staticLine6', parent=self.panel1, pos=wx.Point(448, 64),
              size=wx.Size(1, 2), style=0)

        self.staticLine7 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE7,
              name='staticLine7', parent=self.panel1, pos=wx.Point(448, 64),
              size=wx.Size(1, 2), style=0)

        self.staticLine8 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE8,
              name='staticLine8', parent=self.panel1, pos=wx.Point(449, 128),
              size=wx.Size(551, 2), style=0)

        self.staticLine9 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE9,
              name='staticLine9', parent=self.panel1, pos=wx.Point(448, 64),
              size=wx.Size(1, 64), style=0)

        self.staticLine10 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE10,
              name='staticLine10', parent=self.panel1, pos=wx.Point(1000, 64),
              size=wx.Size(1, 64), style=0)

        self.staticText3 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT3,
              label='Data', name='staticText3', parent=self.panel1,
              pos=wx.Point(448, 144), size=wx.Size(40, 26), style=0)
        self.staticText3.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Calibri'))

        self.staticLine11 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE11,
              name='staticLine11', parent=self.panel1, pos=wx.Point(448, 176),
              size=wx.Size(552, 2), style=0)

        self.staticLine12 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE12,
              name='staticLine12', parent=self.panel1, pos=wx.Point(448, 176),
              size=wx.Size(1, 520), style=0)

        self.staticLine13 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE13,
              name='staticLine13', parent=self.panel1, pos=wx.Point(1000, 176),
              size=wx.Size(1, 520), style=0)

        self.staticLine14 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE14,
              name='staticLine14', parent=self.panel1, pos=wx.Point(448, 696),
              size=wx.Size(552, 2), style=0)

        self.txtCari = wx.TextCtrl(id=wxID_KARYAWANFRTXTCARI, name='txtCari',
              parent=self.panel1, pos=wx.Point(592, 80), size=wx.Size(176, 26),
              style=0, value='')
        self.txtCari.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))

        self.txt_NIK = wx.TextCtrl(id=wxID_KARYAWANFRTXT_NIK, name='txt_NIK',
              parent=self.panel1, pos=wx.Point(216, 80), size=wx.Size(184, 26),
              style=0, value='')
        self.txt_NIK.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.txt_NIK.SetMaxLength(10)
        self.txt_NIK.SetHelpText('')

        self.txt_nama = wx.TextCtrl(id=wxID_KARYAWANFRTXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(216, 112), size=wx.Size(184, 26),
              style=0, value='')
        self.txt_nama.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.txt_nama.SetMaxLength(45)

        self.txt_tempat_lahir = wx.TextCtrl(id=wxID_KARYAWANFRTXT_TEMPAT_LAHIR,
              name='txt_tempat_lahir', parent=self.panel1, pos=wx.Point(216,
              144), size=wx.Size(184, 26), style=0, value='')
        self.txt_tempat_lahir.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Calibri'))
        self.txt_tempat_lahir.SetMaxLength(45)

        self.staticText4 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT4,
              label='NIK', name='staticText4', parent=self.panel1,
              pos=wx.Point(48, 80), size=wx.Size(22, 19), style=0)
        self.staticText4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText5 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT5,
              label='Nama', name='staticText5', parent=self.panel1,
              pos=wx.Point(48, 112), size=wx.Size(38, 19), style=0)
        self.staticText5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText6 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT6,
              label='Tempat Lahir', name='staticText6', parent=self.panel1,
              pos=wx.Point(48, 144), size=wx.Size(86, 19), style=0)
        self.staticText6.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.date_lahir = wx.DatePickerCtrl(id=wxID_KARYAWANFRDATE_LAHIR,
              name='date_lahir', parent=self.panel1, pos=wx.Point(216, 176),
              size=wx.Size(184, 22), style=wx.DP_SHOWCENTURY)
        self.date_lahir.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.date_masuk = wx.DatePickerCtrl(id=wxID_KARYAWANFRDATE_MASUK,
              name='date_masuk', parent=self.panel1, pos=wx.Point(216, 208),
              size=wx.Size(184, 22), style=wx.DP_SHOWCENTURY)
        self.date_masuk.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.rLaki = wx.RadioButton(id=wxID_KARYAWANFRRLAKI, label='Laki-laki',
              name='rLaki', parent=self.panel1, pos=wx.Point(216, 248),
              size=wx.Size(81, 13), style=0)
        self.rLaki.SetValue(True)
        self.rLaki.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))

        self.rPerempuan = wx.RadioButton(id=wxID_KARYAWANFRRPEREMPUAN,
              label='Perempuan', name='rPerempuan', parent=self.panel1,
              pos=wx.Point(216, 264), size=wx.Size(104, 24), style=0)
        self.rPerempuan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.rPerempuan.SetValue(False)

        self.staticText7 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT7,
              label='Tgl. Lahir', name='staticText7', parent=self.panel1,
              pos=wx.Point(48, 176), size=wx.Size(61, 19), style=0)
        self.staticText7.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText8 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT8,
              label='Tgl. Masuk', name='staticText8', parent=self.panel1,
              pos=wx.Point(48, 208), size=wx.Size(71, 19), style=0)
        self.staticText8.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText9 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT9,
              label='Jenis Kelamin', name='staticText9', parent=self.panel1,
              pos=wx.Point(48, 248), size=wx.Size(88, 19), style=0)
        self.staticText9.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText10 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT10,
              label='Alamat', name='staticText10', parent=self.panel1,
              pos=wx.Point(48, 296), size=wx.Size(46, 19), style=0)
        self.staticText10.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_alamat = wx.TextCtrl(id=wxID_KARYAWANFRTXT_ALAMAT,
              name='txt_alamat', parent=self.panel1, pos=wx.Point(216, 296),
              size=wx.Size(184, 48), style=0, value='')
        self.txt_alamat.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.txt_alamat.SetMaxLength(225)

        self.txt_telepon = wx.TextCtrl(id=wxID_KARYAWANFRTXT_TELEPON,
              name='txt_telepon', parent=self.panel1, pos=wx.Point(216, 352),
              size=wx.Size(184, 26), style=0, value='')
        self.txt_telepon.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.txt_telepon.SetMaxLength(15)

        self.cmbPosisi = wx.ComboBox(choices=[], id=wxID_KARYAWANFRCMBPOSISI,
              name='cmbPosisi', parent=self.panel1, pos=wx.Point(216, 384),
              size=wx.Size(184, 27), style=0, value='')
        self.cmbPosisi.SetLabel('')
        self.cmbPosisi.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.cmbPosisi.SetToolTipString('cmbPosisi')
        self.cmbPosisi.Bind(wx.EVT_COMBOBOX, self.OnCmbPosisiCombobox,
              id=wxID_KARYAWANFRCMBPOSISI)

        self.staticText11 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT11,
              label='Telepon', name='staticText11', parent=self.panel1,
              pos=wx.Point(48, 352), size=wx.Size(52, 19), style=0)
        self.staticText11.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText12 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT12,
              label='Posisi', name='staticText12', parent=self.panel1,
              pos=wx.Point(48, 384), size=wx.Size(38, 19), style=0)
        self.staticText12.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_gaji = wx.TextCtrl(id=wxID_KARYAWANFRTXT_GAJI, name='txt_gaji',
              parent=self.panel1, pos=wx.Point(216, 416), size=wx.Size(184, 26),
              style=0, value='')
        self.txt_gaji.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.txt_gaji.SetMaxLength(11)
        self.txt_gaji.SetHelpText('')

        self.staticText13 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT13,
              label='Gaji Pokok', name='staticText13', parent=self.panel1,
              pos=wx.Point(48, 416), size=wx.Size(68, 19), style=0)
        self.staticText13.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_tunjangan = wx.TextCtrl(id=wxID_KARYAWANFRTXT_TUNJANGAN,
              name='txt_tunjangan', parent=self.panel1, pos=wx.Point(216, 448),
              size=wx.Size(184, 26), style=0, value='')
        self.txt_tunjangan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.txt_tunjangan.SetMaxLength(11)

        self.staticText14 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT14,
              label='Tunj. Posisi', name='staticText14', parent=self.panel1,
              pos=wx.Point(48, 448), size=wx.Size(74, 19), style=0)
        self.staticText14.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.staticText15 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT15,
              label='Lembur /Jam', name='staticText15', parent=self.panel1,
              pos=wx.Point(48, 480), size=wx.Size(83, 19), style=0)
        self.staticText15.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.txt_lembur = wx.TextCtrl(id=wxID_KARYAWANFRTXT_LEMBUR,
              name='txt_lembur', parent=self.panel1, pos=wx.Point(216, 480),
              size=wx.Size(184, 26), style=0, value='')
        self.txt_lembur.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.txt_lembur.SetMaxLength(11)

        self.btnClear = wx.Button(id=wxID_KARYAWANFRBTNCLEAR, label='Clear',
              name='btnClear', parent=self.panel1, pos=wx.Point(56, 544),
              size=wx.Size(75, 30), style=0)
        self.btnClear.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnClear.Bind(wx.EVT_BUTTON, self.OnBtnClearButton,
              id=wxID_KARYAWANFRBTNCLEAR)

        self.btnSimpan = wx.Button(id=wxID_KARYAWANFRBTNSIMPAN, label='Simpan',
              name='btnSimpan', parent=self.panel1, pos=wx.Point(176, 544),
              size=wx.Size(75, 30), style=0)
        self.btnSimpan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.btnSimpan.Bind(wx.EVT_BUTTON, self.OnBtnSimpanButton,
              id=wxID_KARYAWANFRBTNSIMPAN)

        self.btnHapus = wx.Button(id=wxID_KARYAWANFRBTNHAPUS, label='Hapus',
              name='btnHapus', parent=self.panel1, pos=wx.Point(296, 544),
              size=wx.Size(75, 30), style=0)
        self.btnHapus.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnHapus.Bind(wx.EVT_BUTTON, self.OnBtnHapusButton,
              id=wxID_KARYAWANFRBTNHAPUS)

        self.tmnBack = wx.Button(id=wxID_KARYAWANFRTMNBACK, label='Back',
              name='tmnBack', parent=self.panel1, pos=wx.Point(1096, 248),
              size=wx.Size(100, 80), style=0)
        self.tmnBack.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.tmnBack.Bind(wx.EVT_BUTTON, self.OnTmnBackButton,
              id=wxID_KARYAWANFRTMNBACK)

        self.tmbKeluar = wx.Button(id=wxID_KARYAWANFRTMBKELUAR, label='Keluar',
              name='tmbKeluar', parent=self.panel1, pos=wx.Point(1096, 384),
              size=wx.Size(100, 80), style=0)
        self.tmbKeluar.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.tmbKeluar.Bind(wx.EVT_BUTTON, self.OnTmbKeluarButton,
              id=wxID_KARYAWANFRTMBKELUAR)

        self.lc_data = wx.ListCtrl(id=wxID_KARYAWANFRLC_DATA, name='lc_data',
              parent=self.panel1, pos=wx.Point(472, 200), size=wx.Size(504,
              472), style=wx.LC_REPORT)
        self.lc_data.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self._init_coll_lc_data_Columns(self.lc_data)
        self.lc_data.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_dataListItemSelected, id=wxID_KARYAWANFRLC_DATA)

        self.staticLine15 = wx.StaticLine(id=wxID_KARYAWANFRSTATICLINE15,
              name='staticLine15', parent=self.panel1, pos=wx.Point(1064, 120),
              size=wx.Size(1, 2), style=0)

        self.staticText16 = wx.StaticText(id=wxID_KARYAWANFRSTATICTEXT16,
              label='Masukkan Nama', name='staticText16', parent=self.panel1,
              pos=wx.Point(472, 80), size=wx.Size(108, 19), style=0)
        self.staticText16.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))

        self.btnCari = wx.Button(id=wxID_KARYAWANFRBTNCARI, label='Cari',
              name='btnCari', parent=self.panel1, pos=wx.Point(792, 80),
              size=wx.Size(75, 30), style=0)
        self.btnCari.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Calibri'))
        self.btnCari.Bind(wx.EVT_BUTTON, self.OnBtnCariButton,
              id=wxID_KARYAWANFRBTNCARI)

        self.btnViewAll = wx.Button(id=wxID_KARYAWANFRBTNVIEWALL,
              label='View All', name='btnViewAll', parent=self.panel1,
              pos=wx.Point(888, 80), size=wx.Size(80, 30), style=0)
        self.btnViewAll.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.btnViewAll.Bind(wx.EVT_BUTTON, self.OnBtnViewAllButton,
              id=wxID_KARYAWANFRBTNVIEWALL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        #Read all combobox data (posisitions) from database
        sqlA = "SELECT * FROM posisikaryawan"
        cur.execute(sqlA)
        hasilA = cur.fetchall()
        posisiDb = []
        for i in hasilA:
            nama_posisiDb = i[1]
            self.cmbPosisi.Append(nama_posisiDb)
            posisiDb.append(nama_posisiDb)
        self.cmbPosisi.SetStringSelection(posisiDb[0])
        
        #Read all listctrl data that saved in database
        sqlB = "SELECT datakaryawan.NIK, datakaryawan.nama, posisikaryawan.nama_posisi \
        FROM datakaryawan, posisikaryawan WHERE datakaryawan.ID_posisiFK=posisikaryawan.ID_posisi \
        ORDER BY datakaryawan.nama ASC"
        
        cur.execute(sqlB)
        hasilB = cur.fetchall()
        p = self.lc_data.GetItemCount()
        for j in hasilB :
            self.lc_data.InsertStringItem(p,"%s"%j[0])
            self.lc_data.SetStringItem(p,1,"%s"%j[1])
            self.lc_data.SetStringItem(p,2,"%s"%j[2])
            p = p + 1
    
    def dateToday(self):
        skrg = datetime.date.today()
        day = skrg.day
        month = skrg.month
        year = skrg.year
        displayed_today = wx.DateTimeFromDMY(day,month-1,year)
        self.date_lahir.SetValue(displayed_today)
        self.date_masuk.SetValue(displayed_today)
    
    def bersih(self):
        self.txt_NIK.SetValue("")
        self.txt_nama.SetValue("")
        self.txt_tempat_lahir.SetValue("")
        self.dateToday()
        self.rLaki.SetValue(True)
        self.txt_alamat.SetValue("")
        self.txt_telepon.SetValue("")
        self.cmbPosisi.SetStringSelection("Manager")
        self.txt_gaji.SetValue("")
        self.txt_tunjangan.SetValue("")
        self.txt_lembur.SetValue("")
        
    def inputToLc(self):
        #Prepare some variable needed that want to be iputted to LC
        NIK = self.txt_NIK.GetValue()
        posisi = self.cmbPosisi.GetStringSelection()
        nama = self.txt_nama.GetValue()
        
        #Input data with indeks
        numRow = self.lc_data.GetItemCount()
        self.lc_data.InsertStringItem(numRow, NIK)
        self.lc_data.SetStringItem(numRow,1,nama)
        self.lc_data.SetStringItem(numRow,2,posisi)
        numRow = numRow + 1

    def OnTmnBackButton(self, event):
        self.main = mainFr.create(None)
        self.main.Show()
        self.Close()

    def OnTmbKeluarButton(self, event):
        self.Close()

    def OnList_posisiListbox(self, event):
        event.Skip()

    def OnBtnClearButton(self, event):
        self.bersih()

    def OnBtnHapusButton(self, event):
        #Confirmation of data deletion  
        
        intNIK = int(self.txt_NIK.GetValue())
        
        if self.txt_NIK.GetValue() == "" :
            self.pesan = wx.MessageDialog(self, "NIK belum diisi !", "Peringatan",wx.OK)
            self.pesan.ShowModal()
            event.Skip()
        sql = "SELECT * FROM datakaryawan WHERE NIK = '%d'"%(intNIK)
        cur.execute(sql)
        hasil = cur.fetchone()
        if cur.rowcount > 0 :
            tanya = wx.MessageDialog(self, message="Anda Yakin Menghapus Karyawan Ini ?",\
            style = wx.YES_NO)
            if tanya.ShowModal() == wx.ID_YES :
                sql = "DELETE FROM datakaryawan WHERE NIK = '%s'"%(intNIK)
                cur.execute(sql)
                conn.commit()
                
        else :
            self.pesan = wx.MessageDialog(self,"NIK Yang Akan Dihapus Tidak Terdata.",\
            "Konfirmasi",wx.OK)
            self.pesan.ShowModal()
        self.bersih()

    def OnBtnSimpanButton(self, event):
        
        #Convert dari string ke integer
        intNIK = int(self.txt_NIK.GetValue())
        intgaji = int(self.txt_gaji.GetValue())
        inttunjangan = int(self.txt_tunjangan.GetValue())
        intlembur = int(self.txt_lembur.GetValue())
        
        #Read the date_lahir 
        selectedDate1 = self.date_lahir.GetValue()
        month_lahir = selectedDate1.Month + 1
        day_lahir = selectedDate1.Day
        year_lahir = selectedDate1.Year
        
        #Read the date masuk
        selectedDate2 = self.date_masuk.GetValue()
        month_masuk = selectedDate2.Month + 1
        day_masuk = selectedDate2.Day
        year_masuk = selectedDate2.Year
        
        #Save date in variable
        tgl_lahir = datetime.date(year_lahir,month_lahir,day_lahir)
        tgl_masuk = datetime.date(year_masuk,month_masuk,day_masuk)
        
        #Taking and saving radio data (gender)
        if self.rLaki.GetValue() == True :
            jenis_kelamin = "Laki-laki"
        else :
            jenis_kelamin = "Perempuan"
        
        #Take and save combobox data (posisi)
        posisi = self.cmbPosisi.GetStringSelection()
        sqlPos = "SELECT * FROM posisikaryawan"
        cur.execute(sqlPos)
        hasilPos = cur.fetchall()
        for i in hasilPos :
            if posisi == i[1] :
                indeksPos = i[0]
        
        sql1 = "SELECT * FROM datakaryawan WHERE NIK = '%d'" %(intNIK)
        cur.execute(sql1)
        hasil = cur.fetchone()
        
        if cur.rowcount > 0 :
            sql2 = "UPDATE datakaryawan\
                    SET nama='%s', tempat_lahir='%s', tgl_lahir='%s', tgl_masuk='%s',\
                    jenis_kelamin='%s', alamat='%s', telepon='%s', ID_posisiFK='%d' \
                    WHERE NIK='%d'"\
                    %(self.txt_nama.GetValue(), self.txt_tempat_lahir.GetValue(), \
                    tgl_lahir , tgl_masuk, jenis_kelamin, self.txt_alamat.GetValue(), \
                    self.txt_telepon.GetValue(), indeksPos, intNIK)
        else:
            sql2 = "INSERT INTO datakaryawan (NIK,nama,tempat_lahir,tgl_lahir,tgl_masuk,\
                    jenis_kelamin,alamat,telepon,ID_posisiFK) \
                    VALUES ('%d','%s','%s','%s','%s','%s','%s','%s','%d')"\
                    %(intNIK, self.txt_nama.GetValue(), self.txt_tempat_lahir.GetValue(), \
                    tgl_lahir, tgl_masuk, jenis_kelamin, self.txt_alamat.GetValue(),  \
                    self.txt_telepon.GetValue(), indeksPos)
                    
        cur.execute(sql2)
        conn.commit()
        self.inputToLc()
        self.bersih()
        self.txt_NIK.SetFocus()        

    def OnCmbPosisiCombobox(self, event):
        pilih = self.cmbPosisi.GetStringSelection()
        sql = "SELECT gaji_posisi,tunjangan_posisi,lembur_posisi FROM posisikaryawan \
        WHERE nama_posisi = '%s'"%(pilih)
        cur.execute(sql)
        hasil = cur.fetchall()
        for i in hasil :
            self.txt_gaji.SetValue(str(i[0]))
            self.txt_tunjangan.SetValue(str(i[1]))
            self.txt_lembur.SetValue(str(i[2]))
                
    def OnLc_dataListItemSelected(self, event):       
        
        rowNumLc = event.m_itemIndex
        lcNIK = int(self.lc_data.GetItem(rowNumLc,0).GetText())
        
        #indexing data that want to take by using intNIK 
        sql = "SELECT * FROM datakaryawan WHERE NIK = '%d'"%lcNIK
        cur.execute(sql)
        hasil = cur.fetchall()
        for i in hasil :
            self.txt_NIK.SetValue(str(i[0]))
            self.txt_nama.SetValue(i[1])
            self.txt_tempat_lahir.SetValue(i[2])
            
            #Read date_lahir from database
            date_lahirDb = i[3]
            day_lahirDb = date_lahirDb.day
            month_lahirDb = date_lahirDb.month
            year_lahirDb = date_lahirDb.year
            displayed_lahirDb = wx.DateTimeFromDMY(day_lahirDb,month_lahirDb-1,year_lahirDb)
            self.date_lahir.SetValue(displayed_lahirDb)
            
            #Read date_masuk from database
            date_masukDb = i[4]
            day_masukDb = date_masukDb.day
            month_masukDb = date_masukDb.month
            year_masukDb = date_masukDb.year
            displayed_masukDb = wx.DateTimeFromDMY(day_masukDb,month_masukDb-1,year_masukDb)
            self.date_masuk.SetValue(displayed_masukDb)
            
            #Read radio data (gender) from database
            genderDb = i[5]
            if genderDb == "Laki-laki":
                self.rLaki.SetValue(True)
            else:
                self.rPerempuan.SetValue(True)
            
            self.txt_alamat.SetValue(i[6])
            self.txt_telepon.SetValue(i[7])
            IDPosisi = int(i[8])
        
        #Read Combobox data (posisi)
        sqlPos = "SELECT * FROM posisikaryawan WHERE ID_posisi = '%d'"%(IDPosisi)
        cur.execute(sqlPos)
        hasilPos = cur.fetchall()
        for j in hasilPos :
            self.cmbPosisi.SetStringSelection(j[1])
            self.txt_gaji.SetValue(str(j[2]))
            self.txt_tunjangan.SetValue(str(j[3]))
            self.txt_lembur.SetValue(str(j[4]))

    def OnBtnCariButton(self, event):
        self.lc_data.DeleteAllItems()
        sql = "SELECT datakaryawan.NIK, datakaryawan.nama, posisikaryawan.nama_posisi \
        FROM datakaryawan, posisikaryawan WHERE datakaryawan.nama LIKE '%%%s%%' \
        AND datakaryawan.ID_posisiFK=posisikaryawan.ID_posisi GROUP BY datakaryawan.nama ASC"\
        %(self.txtCari.GetValue())
        cur.execute(sql)
        hasil = cur.fetchall()
        p = self.lc_data.GetItemCount()
        for i in hasil:
            self.lc_data.InsertStringItem(p,"%s"%i[0])
            self.lc_data.SetStringItem(p,1,"%s"%i[1])
            self.lc_data.SetStringItem(p,2,"%s"%i[2])
            p = p + 1

    def OnBtnViewAllButton(self, event):
        self.lc_data.DeleteAllItems()
        sql = "SELECT datakaryawan.NIK, datakaryawan.nama, posisikaryawan.nama_posisi \
        FROM datakaryawan, posisikaryawan WHERE datakaryawan.ID_posisiFK=posisikaryawan.ID_posisi \
        GROUP BY datakaryawan.nama ASC"
        cur.execute(sql)
        hasil = cur.fetchall()
        p = self.lc_data.GetItemCount()
        for i in hasil:
            self.lc_data.InsertStringItem(p,"%s"%i[0])
            self.lc_data.SetStringItem(p,1,"%s"%i[1])
            self.lc_data.SetStringItem(p,2,"%s"%i[2])
            p = p + 1
        self.txtCari.SetValue("")
