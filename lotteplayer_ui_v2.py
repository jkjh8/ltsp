# -*- coding: utf-8 -*-

from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, pyqtSlot, pyqtSignal, QSize, Qt, QRect, QThread, QTime
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        font_Label = QFont()
        font_Label.setFamily(u"NanumBarunGothic");
        font_Label.setPointSize(14)
        font_10 = QFont();font_10.setPointSize(10)
        #font_10.setFamily(u"NanumBarunGothic")
        font_12 = QFont()
        #font_12.setFamily(u"NanumBarunGothic");font_12.setPointSize(12)
        windowIcon = QIcon();windowIcon.addFile(u":/icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_style_nomal = ("""
                                QPushButton{border:none;border-radius:15px;background-color:#f8f9f9}
                                QPushButton:checked{color:white;background-color:#566573}
                                QPushButton:hover{background-color:#EBF5FB}
                                QPushButton:checked:hover{color:white;background-color:#1C2833}
                                QPushButton:pressed{color:white;background-color:#503131}
                                QPushButton:checked:pressed{color:white;background-color:#503131}
                                """)
        self.btn_style_checked = ("""
                                QPushButton{border:none;border-radius:15px;color:white;background-color:#ff5050}
                                QPushButton:checked{color:white;background-color:#ff3300}
                                QPushButton:hover{background-color:#800000}
                                QPushButton:checked:hover{color:white;background-color:#800000}
                                QPushButton:pressed{color:white;background-color:#270B02}
                                QPushButton:checked:pressed{color:black;background-color:#E7E7E7}
                                """)
        self.btn_style_self = ("""
                                QPushButton{border:none;border-radius:15px;color:white;background-color:#0099ff}
                                QPushButton:checked{color:white;background-color:#ff0000}
                                QPushButton:hover{background-color:#FF0000}
                                QPushButton:checked:hover{color:white;background-color:#FF0000}
                                QPushButton:pressed{color:white;background-color:#28B463}
                                QPushButton:checked:pressed{color:black;background-color:#28B463}
                                """)
        self.combobox_style = ("""
                                QComboBox{color:black; border:1px solid #f8f9f9;}
                                QComboBox::drop-down {border:none; width:20px}
                                QComboBox:down-arrow {image: url(:/icons/down-arrow.png); width: 15px; height: 15px;}
                                QListView::item{height:30px;}
                                QListView::item:selected {color: white; background-color: #4D6C95}");
                                """)

    #Main Windwos
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("QMainWindow{background-color:#ffffff};")
        MainWindow.setWindowIcon(windowIcon)
        self.centralwidget = QWidget(MainWindow)

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0,0,0,0)

    #Main Window Vbox Layout
        self.vbox_MainWindow = QVBoxLayout()
### 1st Line
        self.hbox_Booth = QHBoxLayout()
        self.hbox_Booth.setContentsMargins(20,5,20,5)
        self.hbox_Booth.setSpacing(10)
        #Player Stacked Sel Button
        self.btn_Tab_Player = QPushButton('Player',self.centralwidget)
        playIcon = QIcon();playIcon.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Tab_Player.setIcon(playIcon)
        self.btn_Tab_Player.setMinimumSize(QSize(0, 30))
        self.btn_Tab_Player.setMaximumSize(QSize(150, 16777215))
        self.btn_Tab_Player.setFlat(True)
        self.btn_Tab_Player.setFocusPolicy(Qt.NoFocus)
        self.btn_Tab_Player.setStyleSheet("QPushButton{border:none}")
        self.hbox_Booth.addWidget(self.btn_Tab_Player)
        #Scheduler Stacked Sel Button
        self.btn_Tab_Schduler = QPushButton('스케줄러',self.centralwidget)
        calendar_icon = QIcon();calendar_icon.addFile(u":/icons/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Tab_Schduler.setIcon(calendar_icon)
        self.btn_Tab_Schduler.setMinimumSize(QSize(0, 30))
        self.btn_Tab_Schduler.setMaximumSize(QSize(150, 16777215))
        self.btn_Tab_Schduler.setFlat(True)
        self.btn_Tab_Schduler.setFocusPolicy(Qt.NoFocus)
        self.btn_Tab_Schduler.setStyleSheet("QPushButton{border:none}")
        self.hbox_Booth.addWidget(self.btn_Tab_Schduler)

        self.btn_Setup = QPushButton('설정',self.centralwidget)
        setup_icon = QIcon();setup_icon.addFile(u":/icons/system.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Setup.setIcon(setup_icon)
        self.btn_Setup.setMaximumSize(QSize(150, 16777215))
        self.btn_Setup.setIconSize(QSize(25, 25))
        self.btn_Setup.setFlat(True)
        self.btn_Setup.setFocusPolicy(Qt.NoFocus)
        self.btn_Setup.setStyleSheet("QPushButton{border:none}")      
        self.hbox_Booth.addWidget(self.btn_Setup)

        #Booth Sel
        self.lbl_Booth = QLabel('부스 선택',self.centralwidget)
        self.lbl_Booth.setMinimumSize(QSize(0, 25))
        self.lbl_Booth.setMaximumSize(QSize(60, 16777215))
        self.lbl_Booth.setFont(font_10)
        self.hbox_Booth.addWidget(self.lbl_Booth)

        self.cb_Booth = QComboBox(self.centralwidget)
        self.cb_Booth.setView(QListView())
        self.cb_Booth.setFont(font_10)
        for i in range(9):
            self.cb_Booth.addItem('Booth {}'.format(i+1))
            self.cb_Booth.setItemData(i,font_10,Qt.FontRole)
        self.cb_Booth.setMinimumSize(QSize(0, 30))
        self.cb_Booth.setMaximumSize(QSize(200, 16777215))
        self.cb_Booth.setStyleSheet(self.combobox_style)
        self.cb_Booth.setInsertPolicy(QComboBox.InsertAtBottom)
        self.cb_Booth.setFrame(False)
        self.hbox_Booth.addWidget(self.cb_Booth)

        self.lbl_blank = QLabel(self.centralwidget)
        self.hbox_Booth.addWidget(self.lbl_blank)

        #Audio Device Sel
        self.lbl_AudioDevice = QLabel('오디오 디바이스 선택',self.centralwidget)
        self.lbl_AudioDevice.setMinimumSize(QSize(120, 30))
        self.lbl_AudioDevice.setMaximumSize(QSize(130, 16777215))
        self.lbl_AudioDevice.setFont(font_10)
        self.hbox_Booth.addWidget(self.lbl_AudioDevice)

        self.cb_AudioDevice = QComboBox(self.centralwidget)
        self.cb_AudioDevice.setView(QListView())
        self.cb_AudioDevice.setMinimumSize(QSize(0, 30))
        self.cb_AudioDevice.setStyleSheet(self.combobox_style)
        self.cb_AudioDevice.setInsertPolicy(QComboBox.InsertAtBottom)
        self.cb_AudioDevice.setFrame(False)
        self.hbox_Booth.addWidget(self.cb_AudioDevice)
        self.vbox_MainWindow.addLayout(self.hbox_Booth)

        self.btn_Audiodecive_Refrash = QPushButton(self.centralwidget)
        self.btn_Audiodecive_Refrash.setMinimumSize(QSize(0, 30))
        self.btn_Audiodecive_Refrash.setMaximumSize(QSize(30, 16777215))
        self.btn_Audiodecive_Refrash.setIconSize(QSize(15, 15))
        icon7 = QIcon();icon7.addFile(u":/icons/loop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Audiodecive_Refrash.setIcon(icon7)
        self.btn_Audiodecive_Refrash.setFlat(True)
        self.btn_Audiodecive_Refrash.setFont(font_10)
        self.hbox_Booth.addWidget(self.btn_Audiodecive_Refrash)

    #2nd Line
        #Stack Widget
        self.stackedWidget = QStackedWidget(self.centralwidget)
        #self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setStyleSheet("background-color:#f8f9f9")
        #Stack Page 1
        self.page_1 = QWidget()
        self.gl_Stack_Page_1 = QGridLayout(self.page_1)
### Playlist
        #Label Playlist
        self.lbl_PlayList = QLabel('플레이 리스트',self.page_1)
        self.lbl_PlayList.setFont(font_Label)
        self.lbl_PlayList.setIndent(10)
        #self.lbl_PlayList.setStyleSheet("QLabel{color:#ffffff}")
        self.gl_Stack_Page_1.addWidget(self.lbl_PlayList, 0, 1, 1, 1)
        #Grid Widget Playlist
        self.gw_Playlist = QGridLayout()
        self.gl_Stack_Page_1.addLayout(self.gw_Playlist, 1, 1, 1, 1)
        #Playlist Table
        self.tw_Playlist = QTableWidget(0,1,self.page_1)
        self.tw_Playlist.setHorizontalHeaderItem(0, QTableWidgetItem('Title'))
        self.tw_Playlist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_Playlist.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_Playlist.horizontalHeader().setStretchLastSection(True)
        self.tw_Playlist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tw_Playlist.setMaximumSize(QSize(600, 16777215))
        #self.tw_Playlist.setStyleSheet("QWidget{color:#ffffff}; QTableWidget{gridline-color: #ffffff};")
        self.tw_Playlist.setFrameShape(QFrame.NoFrame)
        #self.tw_Playlist.setFrameShadow(QFrame.Plain)
        self.tw_Playlist.setStyleSheet("""
                                        QWidget{background-color:#f8f9f9}
                                        QHeaderView::section{padding:5px;border:0px}
                                        QTableView{selection-color:white;selection-background-color:#566573}
                                        QTableView QTableCornerButton::section {background:#f8f9f9}
                                        """)

        self.gw_Playlist.addWidget(self.tw_Playlist, 0, 0, 1, 1)
        #hbox Playlist buttons
        self.hbox_Playlist_add_del = QHBoxLayout()
        self.gw_Playlist.addLayout(self.hbox_Playlist_add_del, 2, 0, 1, 1)        

        self.btn_Playlist_Add = QPushButton('Add List',self.page_1)
        icon = QIcon();icon.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Playlist_Add.setIcon(icon)
        self.btn_Playlist_Add.setIconSize(QSize(25, 25))
        self.btn_Playlist_Add.setFocusPolicy(Qt.NoFocus)
        self.btn_Playlist_Add.setStyleSheet("QPushButton{border:none}")
        self.hbox_Playlist_add_del.addWidget(self.btn_Playlist_Add)

        self.btn_Playlist_Del = QPushButton('Del List',self.page_1)
        icon1 = QIcon();icon1.addFile(u":/icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Playlist_Del.setIcon(icon1)
        self.btn_Playlist_Del.setIconSize(QSize(25, 25))
        self.btn_Playlist_Del.setFocusPolicy(Qt.NoFocus)
        self.btn_Playlist_Del.setStyleSheet("QPushButton{border:none}")
        self.hbox_Playlist_add_del.addWidget(self.btn_Playlist_Del)
        #Playlist Play Continue
        self.btn_PlaylistPlay = QPushButton('플레이 리스트 연속 재생',self.page_1)
        self.btn_PlaylistPlay.setMinimumSize(QSize(250,10))
        self.btn_PlaylistPlay.setMaximumSize(QSize(300, 16777215))
        icon2 = QIcon();icon2.addFile(u":/icons/continue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_PlaylistPlay.setIcon(icon2)
        self.btn_PlaylistPlay.setIconSize(QSize(25, 25))
        self.btn_PlaylistPlay.setCheckable(True)
        self.btn_PlaylistPlay.setStyleSheet("""
                                            QPushButton{border:none;border-radius:10px;background-color:#f8f9f9}
                                            QPushButton:checked{color:white;background-color:#566573}
                                            """)
        self.gw_Playlist.addWidget(self.btn_PlaylistPlay, 3, 0, 1, 1, Qt.AlignCenter)

    ### Zone Selector
        self.lbl_Zone = QLabel('방송 구간 선택/방송 구간 상태',self.page_1)
        self.lbl_Zone.setFont(font_Label)
        self.lbl_Zone.setIndent(10)
        #self.lbl_Zone.setStyleSheet("QLabel{color:#ffffff}")

        self.gl_Stack_Page_1.addWidget(self.lbl_Zone, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeIncrement(QSize(1, 2))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.gw_Zone_Sel = QWidget()
        self.gw_Zone_Sel.setGeometry(QRect(0, 0, 498, 908))
        self.gridLayout_ZoneSel = QGridLayout(self.gw_Zone_Sel)
        self.gridLayout_ZoneSel.setObjectName(u"gridLayout_ZoneSel")

        self.zone_Buttons = [str(i) for i in range(72)]

        for i in range(len(self.zone_Buttons)):
            self.zone_Buttons[i] = QPushButton('{}'.format(i+1),self.gw_Zone_Sel)
            self.zone_Buttons[i].setMinimumSize(QSize(0, 40))
            self.zone_Buttons[i].setMaximumSize(QSize(200, 100))
            self.zone_Buttons[i].setStyleSheet(self.btn_style_nomal)
            self.zone_Buttons[i].setCheckable(True)
            self.gridLayout_ZoneSel.addWidget(self.zone_Buttons[i],int(i/6),int(i%6),1,1)

        self.scrollArea.setWidget(self.gw_Zone_Sel)

        self.gl_Stack_Page_1.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)

        #Stack Page 2
### Scheduler
        self.page_2 = QWidget()
        self.stackedWidget.addWidget(self.page_2)

        self.gl_Stack_Page2 = QGridLayout(self.page_2)

        self.vbox_Schedule = QVBoxLayout()
        self.vbox_Schedule.setContentsMargins(10,0,10,0)
        self.gl_Stack_Page2.addLayout(self.vbox_Schedule, 0, 0, 1, 1)

        self.lbl_Schedule = QLabel('Scheduler',self.page_2)
        self.lbl_Schedule.setIndent(10)
        self.lbl_Schedule.setFont(font_Label)
        self.vbox_Schedule.addWidget(self.lbl_Schedule)

        self.sa_Schedule = QScrollArea(self.page_2)
        self.sa_Schedule.setWidgetResizable(True)
        self.sa_Schedule.setStyleSheet("border:none")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 654, 904))
        self.sa_Schedule.setWidget(self.scrollAreaWidgetContents)
        self.vbox_Schedule.addWidget(self.sa_Schedule)

        self.gl_Schedule = QGridLayout(self.scrollAreaWidgetContents)
        self.gl_Schedule.setSpacing(0)
        self.gl_Schedule.setContentsMargins(0,0,0,0)

        self.scrollAreaWidgetContents.setStyleSheet("[coloredcell=\"true\"] {background-color:#EAECEE}")

        self.lbl_Name_0 = QLabel('No.',self.scrollAreaWidgetContents)
        self.lbl_Name_0.setProperty("coloredcell",True)
        self.lbl_Name_0.setMinimumSize(QSize(30, 40))
        self.lbl_Name_0.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_0, 0, 0, 1, 1)
        
        self.lbl_Name_1 = QLabel('파일',self.scrollAreaWidgetContents)
        self.lbl_Name_1.setProperty("coloredcell",True)
        #self.lbl_Name_1.setMinimumSize(QSize(100, 40))
        self.lbl_Name_1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_1, 0, 1, 1, 2)

        self.lbl_Name_2 = QLabel('방송구간',self.scrollAreaWidgetContents)
        self.lbl_Name_2.setProperty("coloredcell",True)
        #self.lbl_Name_2.setMinimumSize(QSize(100, 40))
        self.lbl_Name_2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_2, 0, 3, 1, 2)

        self.lbl_Name_3 = QLabel('요일',self.scrollAreaWidgetContents)
        self.lbl_Name_3.setProperty("coloredcell",True)
        self.lbl_Name_3.setMaximumSize(QSize(100, 40))
        self.lbl_Name_3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_3, 0, 5, 1, 1)

        self.lbl_Name_4 = QLabel('시간',self.scrollAreaWidgetContents)
        self.lbl_Name_4.setProperty("coloredcell",True)
        #self.lbl_Name_4.setMaximumSize(QSize(100, 20))
        self.lbl_Name_4.setMinimumSize(QSize(100, 40))
        self.lbl_Name_4.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_4, 0, 6, 1, 1)

        self.lbl_Name_5 = QLabel('활성화',self.scrollAreaWidgetContents)
        self.lbl_Name_5.setProperty("coloredcell",True)
        #self.lbl_Name_5.setFixedSize(40,20)
        self.lbl_Name_5.setMinimumSize(QSize(80, 40))
        self.lbl_Name_5.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_5, 0, 7, 1, 1)

        self.lbl_Name_6 = QLabel('삭제',self.scrollAreaWidgetContents)
        self.lbl_Name_6.setProperty("coloredcell",True)
        #self.lbl_Name_5.setFixedSize(40,20)
        self.lbl_Name_6.setMinimumSize(QSize(50, 40))
        self.lbl_Name_6.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_6, 0, 8, 1, 1)

        self.lbl_Name_7 = QLabel('복사',self.scrollAreaWidgetContents)
        self.lbl_Name_7.setProperty("coloredcell",True)
        #self.lbl_Name_5.setFixedSize(40,20)
        self.lbl_Name_7.setMinimumSize(QSize(50, 40))
        self.lbl_Name_7.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_7, 0, 9, 1, 1)

        

        self.schedule_List = [['i' for col in range(10)] for row in range(200)]
        self.schedule_Line = ['i']*201

        self.schedule_file_btn_grp = QButtonGroup()
        self.schedule_zone_sel_grp = QButtonGroup()
        self.schedule_del_btn_grp = QButtonGroup()
        self.schedule_copy_btn_grp = QButtonGroup()

        icon_copy = QIcon()
        icon_copy.addFile(u":/icons/copy.png", QSize(), QIcon.Normal, QIcon.Off)

        for i in range(200):
            self.schedule_List[i][0] = QLabel('{}'.format(i+1),self.scrollAreaWidgetContents)
            self.schedule_List[i][0].setMaximumSize(QSize(50, 100))
            self.schedule_List[i][0].setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.schedule_List[i][1] = QLineEdit(self.scrollAreaWidgetContents)
            self.schedule_List[i][1].setAcceptDrops(True)
            #self.schedule_List[i][1].setWordWrap(True)
            self.schedule_List[i][1].setMinimumSize(100,40)
            self.schedule_List[i][2] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][2].setIcon(icon2)
            self.schedule_List[i][2].setFlat(True)
            self.schedule_List[i][2].setMaximumSize(QSize(30, 100))
            self.schedule_file_btn_grp.addButton(self.schedule_List[i][2], i)
            self.schedule_List[i][3] = QLineEdit(self.scrollAreaWidgetContents)
            #self.schedule_List[i][3].setWordWrap(True)
            self.schedule_List[i][4] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][4].setIcon(icon2)
            self.schedule_List[i][4].setFlat(True)
            self.schedule_List[i][4].setMaximumSize(QSize(30, 100))
            self.schedule_zone_sel_grp.addButton(self.schedule_List[i][4], i)
            self.schedule_List[i][5] = QComboBox(self.scrollAreaWidgetContents)
            self.schedule_List[i][5].setView(QListView())
            self.schedule_List[i][5].setStyleSheet(self.combobox_style)
            for day in range(len(self.days)):
                self.schedule_List[i][5].addItem(self.days[day])
            self.schedule_List[i][6] = QTimeEdit(self.scrollAreaWidgetContents)
            self.schedule_List[i][6].setMinimumSize(100,30)
            self.schedule_List[i][6].setStyleSheet("QTimeEdit{border:none;padding:5px}")
            self.schedule_List[i][7] = QCheckBox(self.scrollAreaWidgetContents)
            self.schedule_List[i][7].setMinimumSize(QSize(50, 30))
            self.schedule_List[i][7].setStyleSheet("QCheckBox{margin-left:50%;margin-right:50%;}")
            self.schedule_List[i][8] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][8].setIcon(icon1)
            self.schedule_List[i][8].setFlat(True)
            self.schedule_List[i][8].setMinimumSize(QSize(50, 30))
            self.schedule_del_btn_grp.addButton(self.schedule_List[i][8],i)

            self.schedule_List[i][9] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][9].setIcon(icon_copy)
            self.schedule_List[i][9].setFlat(True)
            #self.schedule_List[i][9].setCheckable(True)
            self.schedule_List[i][9].setMinimumSize(QSize(80, 30))
            self.schedule_List[i][9].setStyleSheet(self.btn_style_nomal)
            self.schedule_copy_btn_grp.addButton(self.schedule_List[i][9],i)

            for j in range(10):
                self.gl_Schedule.addWidget(self.schedule_List[i][j], i+1,j,1,1)


        self.btn_schedule_Reset = QPushButton('Reset', self.page_2)
        self.btn_schedule_Reset.setMinimumSize(200,30)
        self.btn_schedule_Reset.setStyleSheet("""
                                            QPushButton{border:none;border-radius:10px;background-color:#EAECEE}
                                            QPushButton:hover{background-color:#CD6155}
                                            QPushButton:pressed{color:white;background-color:#566573}
                                            """)
        self.vbox_Schedule.addWidget(self.btn_schedule_Reset,Qt.AlignCenter)

### Setup Page
        self.page_3 = QWidget()
        self.Ip_Setup_Widget = QWidget(self.page_3)
        self.Ip_Setup_Widget.setGeometry(QRect(10, 20, 391, 171))
        self.gw_IpSetup = QGridLayout(self.Ip_Setup_Widget)
    
        self.lbl_IP_Setup = QLabel('IP Setup',self.Ip_Setup_Widget)
        self.lbl_IP_Setup.setFont(font_Label)
        self.gw_IpSetup.addWidget(self.lbl_IP_Setup, 0, 0, 1, 1)

        self.line_2 = QFrame(self.Ip_Setup_Widget)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.gw_IpSetup.addWidget(self.line_2, 1, 0, 1, 3)

        self.lbl_Serverip = QLabel('서버 IP',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.lbl_Serverip, 2, 0, 1, 1)

        self.le_Serverip = QLineEdit(self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.le_Serverip, 2, 1, 1, 2)

        self.lbl_Serverport = QLabel('서버 포트',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.lbl_Serverport, 3, 0, 1, 1)

        self.le_Serverport = QLineEdit(self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.le_Serverport, 3, 1, 1, 2)

        self.line = QFrame(self.Ip_Setup_Widget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gw_IpSetup.addWidget(self.line, 4, 0, 1, 3)

        self.btn_Set_Ip = QPushButton('확인',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.btn_Set_Ip, 5, 1, 1, 1)

        self.btn_Set_Ip_Cancel = QPushButton('취소',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.btn_Set_Ip_Cancel, 5, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        #End Stack Widget
        self.vbox_MainWindow.addWidget(self.stackedWidget)
### 3rd Line
    ###Player Control
        self.playControlButtons = QButtonGroup()

        self.vbox_Player = QVBoxLayout()
        self.vbox_Player.setContentsMargins(20,10,20,20)
        self.vbox_MainWindow.addLayout(self.vbox_Player)
        #Player Timeline
        self.hbox_PlayTime = QHBoxLayout()
        self.hbox_PlayTime.setSpacing(10)
        self.vbox_Player.addLayout(self.hbox_PlayTime)

        self.lbl_CurrentTime = QLabel('--/--',self.centralwidget)
        self.lbl_CurrentTime.setMinimumSize(QSize(40, 0))
        self.lbl_CurrentTime.setMaximumSize(QSize(100, 16777215))
        self.hbox_PlayTime.addWidget(self.lbl_CurrentTime)

        self.pgb_CurrentTime = QProgressBar(self.centralwidget)
        self.pgb_CurrentTime.setMaximumSize(QSize(16777215, 10))
        self.pgb_CurrentTime.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\nQProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        #self.pgb_CurrentTime.setValue(24)
        self.pgb_CurrentTime.setTextVisible(False)
        self.hbox_PlayTime.addWidget(self.pgb_CurrentTime)

        self.lbl_MediaTime = QLabel('--/--',self.centralwidget)
        self.lbl_MediaTime.setMinimumSize(QSize(40, 0))
        self.lbl_MediaTime.setMaximumSize(QSize(100, 16777215))
        self.hbox_PlayTime.addWidget(self.lbl_MediaTime)
        #Player Control Buttons
        self.hbox_PlayerControl = QHBoxLayout()
        self.hbox_PlayerControl.setSpacing(20)
        self.hbox_PlayerControl.setContentsMargins(20,10,20,0)
        #self.hbox_PlayerControl.setSizeConstraint(QLayout.SetFixedSize)

        self.vbox_Player.addLayout(self.hbox_PlayerControl)

        self.btn_Play = QPushButton(self.centralwidget)
        self.btn_Play.setMinimumSize(QSize(40, 40))
        icon3 = QIcon();icon3.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off);icon3.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_Play.setIcon(icon3)
        self.btn_Play.setIconSize(QSize(25, 25))
        self.btn_Play.setCheckable(True)
        self.btn_Play.setStyleSheet("""
            QPushButton{border:none;border-radius:20px;padding-left:10px}
            QPushButton:hover{background-color:#5499C7}
            QPushButton:checked{padding-left:0px;background-color:#ccff99}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_Play)                

        self.btn_RW = QPushButton(self.centralwidget)
        self.btn_RW.setMinimumSize(QSize(40, 40))
        icon4 = QIcon();icon4.addFile(u":/icons/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_RW.setIcon(icon4)
        self.btn_RW.setStyleSheet("""
            QPushButton{border:none;border-radius:20px;}
            QPushButton:hover{background-color:#7DCEA0}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_RW)

        self.btn_Stop = QPushButton(self.centralwidget)
        self.btn_Stop.setMinimumSize(QSize(40, 40))
        icon5 = QIcon();icon5.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Stop.setIcon(icon5)
        self.btn_Stop.setStyleSheet("""
            QPushButton{border:none;border-radius:20px}
            QPushButton:hover{background-color:#C0392B}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_Stop)

        self.btn_FF = QPushButton(self.centralwidget)
        self.btn_FF.setMinimumSize(QSize(40, 40))
        icon6 = QIcon();icon6.addFile(u":/icons/FF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_FF.setIcon(icon6)
        self.btn_FF.setStyleSheet("""
            QPushButton{border:none;border-radius:20px}
            QPushButton:hover{background-color:#A569BD}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_FF)

        self.btn_Loop = QPushButton(self.centralwidget)
        self.btn_Loop.setMinimumSize(QSize(40, 40))
        icon7 = QIcon();icon7.addFile(u":/icons/loop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Loop.setIcon(icon7)
        self.btn_Loop.setCheckable(True)
        self.btn_Loop.setStyleSheet("""
            QPushButton{border:none;border-radius:20px}
            QPushButton:hover{background-color:#5F6A6A}
            QPushButton:checked{padding-left:0px;background-color:#839192}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_Loop)

        self.hline_4 = QFrame(self.centralwidget)
        self.hline_4.setFrameShape(QFrame.VLine)
        self.hline_4.setFrameShadow(QFrame.Sunken)
        self.hbox_PlayerControl.addWidget(self.hline_4)

        self.lbl_Volume = QLabel(self.centralwidget)
        self.lbl_Volume.setMaximumSize(QSize(25, 25))
        self.lbl_Volume.setPixmap(QPixmap(u":/icons/adjust.png"))
        self.lbl_Volume.setScaledContents(True)
        self.hbox_PlayerControl.addWidget(self.lbl_Volume)

        self.Sld_Vol = QSlider(self.centralwidget)
        self.Sld_Vol.setMaximumSize(QSize(300, 16777215))
        self.Sld_Vol.setStyleSheet(u"QSlider::handle:horizontal {background-color: #05B8CC;border: 1px solid #5c5c5c;width: 18px;margin: -2px 0;border-radius: 5px;}")
        self.Sld_Vol.setMaximum(100)
        self.Sld_Vol.setOrientation(Qt.Horizontal)
        #self.Sld_Vol.setValue(100)
        self.hbox_PlayerControl.addWidget(self.Sld_Vol)

        self.lbl_Vol_Value = QLabel('100%',self.centralwidget)
        self.lbl_Vol_Value.setMinimumSize(QSize(30, 0))
        self.lbl_Vol_Value.setMaximumSize(QSize(50, 16777215))
        self.lbl_Vol_Value.setFont(font_12)
        self.lbl_Vol_Value.setAlignment(Qt.AlignCenter)
        self.hbox_PlayerControl.addWidget(self.lbl_Vol_Value)        

        self.gridLayout.addLayout(self.vbox_MainWindow, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

class Dialog_Zone_Sel(object):
    def setupUi(self,Dialog):
        self.btn_style_nomal = ("""
                                QPushButton{border:none;border-radius:15px;background-color:#F8F9F9}
                                QPushButton:checked{color:white;background-color:#566573}
                                QPushButton:hover{background-color:#EBF5FB}
                                QPushButton:checked:hover{color:white;background-color:#1C2833}
                                QPushButton:pressed{color:white;background-color:#503131}
                                QPushButton:checked:pressed{color:white;background-color:#503131}
                                """)
        self.btn_style_ok = ("background-color:#EAECEE")
        font_Label = QFont();font_Label.setFamily(u"NanumBarunGothic");font_Label.setPointSize(14)
        self.btn_zone_sel = ['i']*66
        self.btn_zone_sel_status = [0]*66
        self.popup_btn_grp = QButtonGroup()
        self.popup_btn_grp.setExclusive(False)
        Dialog.resize(600,600)
        Dialog.setWindowTitle("방송 구간 선택")
        Dialog.setStyleSheet("background-color:#f8f9f9")
        
        self.vbox_popup = QVBoxLayout(Dialog)
        self.vbox_popup.setContentsMargins(0,0,0,0)
        self.vbox_popup.setSpacing(10)
        self.lbl_popup_title = QLabel("지점 선택",Dialog)
        self.lbl_popup_title.setMinimumSize(100,30)
        self.lbl_popup_title.setFont(font_Label)
        self.lbl_popup_title.setStyleSheet("background-color:white;padding-left:30px")
        self.vbox_popup.addWidget(self.lbl_popup_title)

        self.gl_popup = QGridLayout()
        self.gl_popup.setContentsMargins(10,0,10,0)
        self.vbox_popup.addLayout(self.gl_popup)
        for i in range(66):
            self.btn_zone_sel[i] = QPushButton("{}".format(i+1), Dialog)
            self.btn_zone_sel[i].setMinimumSize(QSize(0, 40))
            self.btn_zone_sel[i].setMaximumSize(QSize(200, 100))
            self.btn_zone_sel[i].setCheckable(True)
            self.btn_zone_sel[i].setChecked(False)
            self.btn_zone_sel[i].setStyleSheet(self.btn_style_nomal)
            self.popup_btn_grp.addButton(self.btn_zone_sel[i],i)
            self.gl_popup.addWidget(self.btn_zone_sel[i],int(i/6),int(i%6),1,1)

        self.button_box_widget = QWidget(Dialog)
        self.button_box_widget.setStyleSheet("background-color:#ffffff")
        self.vbox_buttonbox = QVBoxLayout(self.button_box_widget)
        self.buttonBox = QDialogButtonBox(self.button_box_widget)
        self.buttonBox.setContentsMargins(0,0,20,0)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setMinimumHeight(40)
        self.buttonBox.setStyleSheet(self.btn_style_ok)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.vbox_buttonbox.addWidget(self.buttonBox)
        self.vbox_popup.addWidget(self.button_box_widget)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)  

        QMetaObject.connectSlotsByName(Dialog)

class Dialog_Message(object):
    def setupUi(self,Dialog):
        font_Label = QFont();font_Label.setFamily(u"NanumBarunGothic");font_Label.setPointSize(14)
        self.btn_style_ok = ("background-color:#EAECEE")

        Dialog.resize(600,300)
        Dialog.setWindowTitle("이벤트 방송")
        Dialog.setStyleSheet("background-color:#f8f9f9")
        
        self.vbox_popup = QVBoxLayout(Dialog)
        self.vbox_popup.setContentsMargins(0,0,0,0)
        #self.vbox_popup.setSpacing(10)
        self.lbl_popup_title = QLabel("스케쥴 방송",Dialog)
        self.lbl_popup_title.setFont(font_Label)
        self.lbl_popup_title.setMinimumHeight(40)
        self.lbl_popup_title.setMaximumHeight(40)
        self.lbl_popup_title.setStyleSheet("background-color:white;padding-left:30px")
        self.vbox_popup.addWidget(self.lbl_popup_title)

        self.lbl_Message = QLabel(Dialog)
        self.lbl_Message.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.vbox_popup.addWidget(self.lbl_Message)

        self.lbl_Message_Zone= QLabel(Dialog)
        self.lbl_Message_Zone.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.vbox_popup.addWidget(self.lbl_Message_Zone)

        self.button_box_widget = QWidget(Dialog)
        self.button_box_widget.setStyleSheet("background-color:#ffffff")
        self.vbox_buttonbox = QVBoxLayout(self.button_box_widget)
        self.buttonBox = QDialogButtonBox(self.button_box_widget)
        self.buttonBox.setContentsMargins(0,0,20,0)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setMinimumHeight(20)
        self.buttonBox.setMaximumHeight(40)
        self.buttonBox.setStyleSheet(self.btn_style_ok)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.vbox_buttonbox.addWidget(self.buttonBox)
        self.vbox_popup.addWidget(self.button_box_widget)

        self.buttonBox.accepted.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)