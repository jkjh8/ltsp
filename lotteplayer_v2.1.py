# -*- coding: utf-8 -*-
import sys
import vlc
import time
import socket
import os.path
import math
import struct
import datetime
import lotteplayer_rc
import re
import json
import os
from lotteplayer_ui_v2 import Ui_MainWindow, Dialog_Zone_Sel, Dialog_Message
from _thread import *
from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, pyqtSlot, pyqtSignal, QSize, Qt, QRect, QThread, QTime, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import *


class Main(QMainWindow, Ui_MainWindow, Dialog_Zone_Sel, Dialog_Message):
    play = pyqtSignal(str)
    pause = pyqtSignal()
    stop = pyqtSignal()
    get_vol = pyqtSignal()
    set_vol = pyqtSignal(int)
    auidodevice_call = pyqtSignal()
    audioDevice_Change = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        # Variable
        self.setup = ({'serverip': '172.28.242.216', 'serverport': 5008, 'boothNum': 10, 'audioDeviceId': 0, 'vol': 70,
                       'zone_name_1': '센텀시티', 'zone_name_2': '이시아폴리스', 'zone_name_3': '상인점', 'zone_name_4': '대구점', 'zone_name_5': '포항점', 'zone_name_6': '아쿠아몰', 'zone_name_7': '광복점', 'zone_name_8': '광주점',
                       'zone_name_9': '전주점', 'zone_name_10': '청주영플라자', 'zone_name_11': '대전점', 'zone_name_12': '서울역점', 'zone_name_13': '영등포점', 'zone_name_14': '중동점', 'zone_name_15': '관악점', 'zone_name_16': '창원점',
                       'zone_name_17': '창원영패션관', 'zone_name_18': '일산점', 'zone_name_19': '구리점', 'zone_name_20': '평촌점', 'zone_name_21': '안산점', 'zone_name_22': '미아점', 'zone_name_23': '스타시티', 'zone_name_24': '노원점',
                       'zone_name_25': '분당점', 'zone_name_26': '잠실점', 'zone_name_27': '동래점', 'zone_name_28': '청량지점', 'zone_name_29': '에비뉴엘', 'zone_name_30': '영플라자', 'zone_name_31': '본점', 'zone_name_32': '강남점',
                       'zone_name_33': '청주아울렛', 'zone_name_34': '울산점', 'zone_name_35': '김해아울렛', 'zone_name_36': '파주아울렛', 'zone_name_37': '서면점', 'zone_name_38': '율하점', 'zone_name_39': '수완아울렛', 'zone_name_40': '광주월드컵점',
                       'zone_name_41': '부여아울렛', 'zone_name_42': '이천아울렛', 'zone_name_43': '고양터미널', 'zone_name_44': '에비뉴엘\n월드타워', 'zone_name_45': '수원점', 'zone_name_46': '광명점', 'zone_name_47': '구리아울렛', 'zone_name_48': '동부산점',
                       'zone_name_49': '마산점', 'zone_name_50': '광교아울렛', 'zone_name_51': '가산아울렛', 'zone_name_52': '진주아울렛', 'zone_name_53': '남악아울렛', 'zone_name_54': '고양아울렛', 'zone_name_55': '군산아울렛', 'zone_name_56': '기흥아울렛',
                       'zone_name_57': '인천터미널'})

        self.logserver = ('172.28.242.40', 9999)
        self.zone_status = ({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0,
                            34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 48: 0, 49: 0, 50: 0, 51: 0, 52: 0, 53: 0, 54: 0, 55: 0, 56: 0, 57: 0, 58: 0, 59: 0, 60: 0, 61: 0, 62: 0, 63: 0, 64: 0, 65: 0, 66: 0})
        self.zone_state = (['대기중', '방송중\nBooth 1', '방송중\nBooth 2', '방송중\nBooth 3', '방송중\nBooth 4', '방송중\nBooth 5', '방송중\nBooth 6', '방송중\nBooth 7', '방송중\nBooth 8', '방송중\nBooth 9',
                            '방송중\nPlayer 1', '방송중\nPlayer 2', '방송중\nPlayer 3', '방송중\nPlayer 4', '방송중\nPlayer 5', '방송중\nPlayer 6', '방송중\nPlayer 7', '방송중\nPlayer 8', '방송중\nPlayer 9'])
        self.playIndex = 0
        self.playLoop = 0
        self.playlist = []
        self.zone_list = []
        self.copy_ID = 99

        self.days = ["매일", "월~목", "금~일", "월~수",
                     "목~일", "월", "화", "수", "목", "금", "토", "일"]
        self.days_value = [[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3], [4, 5, 6], [
            0, 1, 2], [3, 4, 5, 6], [0], [1], [2], [3], [4], [5], [6]]

        self.dialog = QDialog()
        self.dialog.Qui = Dialog_Zone_Sel()
        self.dialog.Qui.setupUi(self.dialog)
        self.dialog_Message = QDialog()
        self.dialog_Message.Qui = Dialog_Message()
        self.dialog_Message.Qui.setupUi(self.dialog_Message)

        self.setupUi(self)
        self.setWindowTitle('Audio Player - 224.1.128.128 : 5007')

        self.setup_file_road()

        self.timerVar = QTimer()
        self.timerVar.setInterval(1000)

        # Thread Class
        self.audioplayer = audioplayer()
        self.udp_server = udp_server()
        #self.schedulePlay = schedulePlay()
        #self.chimeplayer = chimeplayer()
        #Signal & Slot
        self.Sld_Vol.valueChanged.connect(self.lbl_Vol_Value.setNum)
        self.Sld_Vol.valueChanged.connect(self.vol_Set)
        self.btn_Tab_Player.clicked.connect(
            lambda: self.stacked_Wiget_Page_Change(0))
        self.btn_Tab_Schduler.clicked.connect(
            lambda: self.stacked_Wiget_Page_Change(1))
        self.btn_Setup.clicked.connect(
            lambda: self.stacked_Wiget_Page_Change(2))
        self.btn_Playlist_Add.clicked.connect(self.addList)
        self.btn_Playlist_Del.clicked.connect(self.delList)
        self.tw_Playlist.cellClicked.connect(self.select_Playlist_row)
        self.tw_Playlist.cellDoubleClicked.connect(self.doubleClick_Playlist)
        self.btn_Stop.clicked.connect(lambda: self.play_audio(0))
        self.btn_Play.clicked.connect(lambda: self.play_audio(1))
        self.btn_RW.clicked.connect(lambda: self.play_audio(2))
        self.btn_FF.clicked.connect(lambda: self.play_audio(3))
        self.btn_Loop.clicked.connect(lambda: self.play_audio(4))
        self.btn_PlaylistPlay.clicked.connect(lambda: self.play_audio(4))
        self.btn_schedule_Reset.clicked.connect(self.scheduler_reset)
        self.btn_Audiodecive_Refrash.clicked.connect(self.audio_Device_Refrash)
        self.play.connect(self.audioplayer.play)
        self.pause.connect(self.audioplayer.pause)
        self.stop.connect(self.audioplayer.stop)
        self.auidodevice_call.connect(self.audioplayer.get_Audio_Devices)
        self.get_vol.connect(self.audioplayer.audio_Vol_Get)
        self.set_vol.connect(self.audioplayer.audio_Vol_Set)

        self.cb_Booth.currentIndexChanged.connect(self.set_Booth_Index)

        self.audioplayer.player_Status.connect(self.player_state_change)
        self.audioplayer.audio_devices.connect(self.audio_devices)

        self.udp_server.udp_data.connect(self.server_data_parcing)

        self.schedule_file_btn_grp.buttonClicked[int].connect(
            self.schedule_file_load)
        self.schedule_zone_sel_grp.buttonClicked[int].connect(
            self.schedule_zone_sel)
        self.schedule_del_btn_grp.buttonClicked[int].connect(
            self.schedule_List_del)
        self.schedule_copy_btn_grp.buttonClicked[int].connect(
            self.schedule_copy)

        for i in range(200):
            self.schedule_List[i][7].stateChanged.connect(
                self.schedule_value_change)
            self.schedule_List[i][5].currentIndexChanged.connect(
                self.schedule_value_change)
            self.schedule_List[i][6].timeChanged.connect(
                self.schedule_value_change)

        # self.schedulePlay.Timer_Receive_String.connect(self.schedule_parcing)
        self.btn_Set_Ip.clicked.connect(self.server_ip_setup)
        self.timerVar.timeout.connect(self.schedule_parcing)
        self.show()

        # Thread Start
        self.udp_server.start()
        # self.schedulePlay.start()
        self.timerVar.start()

        # Start Set Value

        self.set_vol.emit(self.setup['vol'])
        self.get_vol.emit()
        self.set_ButtonName()
        self.setup_file_road()
        self.cb_Booth.setCurrentIndex(self.setup['boothNum']-10)
        # self.cb_AudioDevice.setCurrentIndex(self.setup['audioDeviceId'])
        self.le_Serverip.setText(self.setup['serverip'])
        self.le_Serverport.setText(str(self.setup['serverport']))
        start_new_thread(self.server_call, ('t:request,!',))
        start_new_thread(self.server_call,
                         ('t:booth{},!'.format(self.setup['boothNum']),))
        start_new_thread(self.log_server_call, ('0,{}번 부스 이벤트 플레이가 실행되었습니다.'.format(
            self.setup['boothNum']-9),))

        self.cb_AudioDevice.currentIndexChanged.connect(self.set_Audio_Device)
        self.audioDevice_Change.connect(self.audioplayer.set_Audio_Device)
        self.set_vol.emit(self.setup['vol'])
        self.device_Setup_State = True
        self.auidodevice_call.emit()
########################################################## player FN ########################################################################

    def song_length(value):
        self.lbl_MediaTime.setText(self.format_time(value))
        self.media_length = value

    # Play time return
    def format_time(self, milliseconds):
        self.position = milliseconds / 1000
        m, s = divmod(self.position, 60)
        h, m = divmod(m, 60)
        return ("%02d/%02d" % (m, s))

    # Select booth
    def set_Booth_Index(self, index):
        self.setup['boothNum'] = index + 10
        self.set_ButtonName()
        self.setup_file_save()

    # Audio Device List Retrun
    def audio_Device_Refrash(self):
        self.cb_AudioDevice.clear()
        self.auidodevice_call.emit()
        # self.audioDevice_Change.emit(0)

    @pyqtSlot(list)
    def audio_devices(self, devicelist):
        self.device_Setup_State = False
        for i in range(len(devicelist)):
            self.cb_AudioDevice.addItem(devicelist[i])
        self.find_device()

    def find_device(self):
        self.device_Setup_State = True
        for i in range(self.cb_AudioDevice.count()):
            # if 'ADAT' in self.cb_AudioDevice.itemText(i):
            if self.setup['audioDeviceId'] == self.cb_AudioDevice.itemText(i):
                self.cb_AudioDevice.setCurrentIndex(i)
                self.audioDevice_Change.emit(i)
                print(self.cb_AudioDevice.itemText(i))

    @pyqtSlot(int)
    def set_Audio_Device(self, id):
        if id > -1 and self.device_Setup_State:
            self.audioDevice_Change.emit(id)
            self.setup['audioDeviceId'] = self.cb_AudioDevice.currentText()
            self.setup_file_save()

    # Audio Vol Set
    def vol_Set(self, volValue):
        self.set_vol.emit(volValue)
        self.setup['vol'] = volValue
        self.setup_file_save()

    def stacked_Wiget_Page_Change(self, pageNum):
        self.stackedWidget.setCurrentIndex(pageNum)

    # Set Button Name
    def set_ButtonName(self):
        for i in range(66):
            zonestate_index = self.zone_status[i+1]
            if 'zone_name_{}'.format(i+1) in self.setup:
                if zonestate_index <= 18:
                    self.zone_Buttons[i].setText(
                        '{}\n-{}-'.format(self.setup['zone_name_{}'.format(i+1)], self.zone_state[zonestate_index]))
                else:
                    self.zone_Buttons[i].setText(
                        '{}\n-{}-'.format(self.setup['zone_name_{}'.format(i+1)], "외부 방송"))
                if zonestate_index == 0:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_nomal)
                elif zonestate_index == self.setup['boothNum']-9:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_self)
                else:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_checked)

    # Play List
    def addList(self):
        files = QFileDialog.getOpenFileNames(self, 'Select one or more files to open', os.path.expanduser(
            "~\\Desktop"), 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)', None)
        cnt = len(files[0])
        row = len(self.playlist)

        for i in range(row, row+cnt):
            self.playlist.append(files[0][i-row])
        self.tw_Playlist.setRowCount(len(self.playlist))

        for i in range(len(self.playlist)):
            self.tw_Playlist.setItem(i, 0, QTableWidgetItem(
                os.path.basename(self.playlist[i])))

        self.tw_Playlist.selectRow(0)
        self.playIndex = 0

    def delList(self):
        row = self.tw_Playlist.rowCount()
        index = []
        for item in self.tw_Playlist.selectedIndexes():
            index.append(item.row())
        index = list(set(index))
        index.reverse()
        for i in index:
            del self.playlist[i]
        self.tw_Playlist.setRowCount(len(self.playlist))
        for i in range(len(self.playlist)):
            self.tw_Playlist.setItem(i, 0, QTableWidgetItem(
                os.path.basename(self.playlist[i])))

    def select_Playlist_row(self, row, colum):
        self.playIndex = row

    def doubleClick_Playlist(self, row, colum):
        if self.btn_Play.isChecked == True:
            self.play_audio(0)
            time.sleep(1)
        self.playIndex = row
        self.btn_Play.setChecked(True)
        self.play_audio(1)

    def overlapzone_popup(self, overlap_zone_name, title, message):
        self.dialog_Message.setWindowTitle(title)
        self.dialog_Message.Qui.lbl_Message.setText(message)
        if str(type(overlap_zone_name)) == "<class 'list'>":
            print_Message = ','.join(overlap_zone_name)
        else:
            print_Message = overlap_zone_name
        self.dialog_Message.Qui.lbl_Message_Zone.setText(print_Message)
        self.dialog_Message.show()
        start_new_thread(self.popup_close, (10,))
        # self.btn_Play.setChecked(False)

    def popup_close(self, timer):
        time.sleep(timer)
        self.dialog_Message.close()

    # Audio Play
    def play_audio(self, index):
        if index == 0:
            self.stop.emit()

        elif index == 1:
            self.find_device()
            # self.audioDevice_Change.emit(self.setup['audioDeviceId'])
            if self.btn_Play.isChecked() == True:
                try:
                    self.zone_list = []
                    for i in range(len(self.zone_Buttons)):
                        if self.zone_Buttons[i].isChecked():
                            self.zone_list.append(i+1)
                    overlap_zone_name = self.find_zone_overlap(self.zone_list)
                    if overlap_zone_name:
                        start_new_thread(self.log_server_call, ('0, {}부스 방송구간 중복으로 이벤트 방송이 실행되지 않았습니다. -{}-'.format(
                            self.setup['boothNum']-9, ','.join(overlap_zone_name)),))
                        self.overlapzone_popup(
                            overlap_zone_name, '이벤트 방송', '방송구간 중복으로 방송이 중단됩니다.')
                        self.stop.emit()
                        #self.zone_list = []

                    else:
                        if self.playlist:
                            broadcast_zone = []
                            # broadcast_zone_name=[]
                            for n in range(len(self.zone_list)):
                                broadcast_zone.append('{}:{}'.format(
                                    self.zone_list[n], self.setup['boothNum']))
                                # broadcast_zone_name.append(self.setup['zone_name_{}'.format(self.zone_list[n])])
                            if broadcast_zone:
                                start_new_thread(
                                    self.server_call, ('t:onair,{},!'.format(','.join(broadcast_zone)),))
                            #start_new_thread(self.log_server_call,('0, {}부스 이벤트 방송 실행. -{}-'.format(self.setup['boothNum']-9,','.join(broadcast_zone_name)),))
                            # time.sleep(2)
                            # self.play.emit(self.playlist[self.playIndex])
                            start_new_thread(
                                self.wait_play, (self.playlist[self.playIndex],))
                            self.tw_Playlist.selectRow(self.playIndex)
                            self.btn_Play.setChecked(True)
                            self.statusbar.showMessage(
                                self.tw_Playlist.item(self.playIndex, 0).text())
                        else:
                            self.Play_Button_Status = 0
                            self.btn_Play.setChecked(False)
                            self.addList()
                except:
                    self.stop.emit()
                    self.statusBar().showMessage('Player에 문제가 발생하여 파일을 재생할 수 없습니다.', 5000)
                    start_new_thread(self.log_server_call, ('0, {}부스 Player에 문제가 발생하여 파일을 재생할 수 없습니다.'.format(
                        self.setup['boothNum']-9),))
            else:
                print('else')
                self.pause.emit()
        elif index == 2:
            self.stop.emit()
            if self.playIndex > 1:
                self.playIndex -= 1
            self.tw_Playlist.selectRow(self.playIndex)
        elif index == 3:
            self.stop.emit()
            if self.playIndex >= self.tw_Playlist.rowCount()-1:
                self.playIndex = 0
            else:
                self.playIndex += 1
            self.tw_Playlist.selectRow(self.playIndex)

        elif index == 4:
            loop = self.btn_Loop.isChecked()
            playlistplay = self.btn_PlaylistPlay.isChecked()
            if loop == True and playlistplay == False:
                self.playLoop = 1
            elif loop == False and playlistplay == True:
                self.playLoop = 2
            elif loop == True and playlistplay == True:
                self.playLoop = 3
            else:
                self.playLoop = 0

    # Player Callback
    @pyqtSlot(str, int)
    def player_state_change(self, key, value):
        # 파일길이
        if key == 'length':
            self.lbl_MediaTime.setText(self.format_time(value))
            self.media_length = value
        # 현재 시간
        elif key == 'current_time':
            self.lbl_CurrentTime.setText(self.format_time(value))
            self.pgb_CurrentTime.setValue(
                math.ceil(value/self.media_length*100))
        # 정지
        elif key == 'stop' and value == 1:
            loop = self.btn_Loop.isChecked()
            playlistplay = self.btn_PlaylistPlay.isChecked()
            if loop == True and playlistplay == False:
                self.playLoop = 1
            elif loop == False and playlistplay == True:
                self.playLoop = 2
            elif loop == True and playlistplay == True:
                self.playLoop = 3
            else:
                self.playLoop = 0

            if self.playLoop == 1:
                self.play.emit(self.playlist[self.playIndex])
                self.statusbar.showMessage(
                    self.tw_Playlist.item(self.playIndex, 0).text())
            elif self.playLoop == 2:
                if self.playIndex == self.tw_Playlist.rowCount()-1:
                    self.tw_Playlist.selectRow(0)
                    self.playIndex = 0
                    self.song_finished()
                else:
                    self.play_next()
            elif self.playLoop == 3:
                self.play_next()
            else:
                self.song_finished()
                start_new_thread(self.log_server_call, ('0, {}번 이벤트 플레이어 방송이 종료되었습니다.'.format(
                    self.setup['boothNum']-9),))
        elif key == 'stop' and value == 0:
            self.Play_Button_Status = 0
            self.song_finished()

            start_new_thread(self.log_server_call, ('0, {}번 이벤트 플레이어 방송을 정지 하였습니다.'.format(
                self.setup['boothNum']-9),))

        # 볼륨
        elif key == 'vol':
            self.Sld_Vol.setValue(value)

    def play_next(self):
        if self.playIndex >= self.tw_Playlist.rowCount()-1:
            self.playIndex = 0
        else:
            self.playIndex += 1
        print(self.playIndex)
        self.statusbar.clearMessage()
        self.tw_Playlist.selectRow(self.playIndex)
        self.play.emit(self.playlist[self.playIndex])
        self.statusbar.showMessage(
            self.tw_Playlist.item(self.playIndex, 0).text())

    def song_finished(self):
        self.lbl_MediaTime.setText('--/--')
        self.lbl_CurrentTime.setText('--/--')
        self.pgb_CurrentTime.setValue(0)
        self.btn_Play.setChecked(False)
        self.statusbar.clearMessage()
        if self.zone_list:
            broadcast_zone = []
            for i in range(len(self.zone_list)):
                broadcast_zone.append('{}:{}'.format(self.zone_list[i], 0))
            start_new_thread(
                self.server_call, ('t:onair,{},!'.format(','.join(broadcast_zone)),))
            start_new_thread(self.log_server_call, ('0,{} 부스 방송이 종료 되었습니다.'.format(
                self.setup['boothNum']-9),))
            self.zone_list = []
        # self.auidodevice_call.emit()

    def server_ip_setup(self):
        self.setup['serverip'] = self.le_Serverip.text()
        self.setup['serverport'] = int(self.le_Serverport.text())
        self.setup_file_save()

    # Udp Mulicast Callback
    def server_data_parcing(self, data):
        # print(data)
        recv_data = data.split(',')
        for i in range(len(recv_data)):
            try:
                key, value = recv_data[i].split(':')
            except:
                pass
            try:
                self.zone_status[int(key)] = int(value)
            except:
                pass
        self.set_ButtonName()

    # Udp Send Data
    def log_server_call(self, data):
        try:
            udp_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sender.sendto((data).encode('utf8'), self.logserver)
            udp_sender.close()
        except:
            self.statusBar().showMessage('네트워크가 활성화 되지 않았습니다.', 5000)
    # Log Server Call

    def server_call(self, data):
        try:
            udp_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sender.sendto(
                (data).encode(), (self.setup['serverip'], self.setup['serverport']))
            #print(data, self.setup['serverip'],self.setup['serverport'])
            udp_sender.close()
        except:
            self.statusBar().showMessage('네트워크가 활성화 되지 않았습니다.', 5000)

    def setup_file_save(self):
        with open('setup.json', 'w') as file:
            json.dump(self.setup, file, ensure_ascii=False)

    def setup_file_road(self):
        try:
            with open('setup.json', 'r') as file:
                self.setup = json.load(file)
                #setup = json.dumps(json_setup)
            for i in range(200):
                if 'schedule_file_{}'.format(i) in self.setup:
                    self.schedule_List[i][1].setText(
                        self.setup['schedule_file_{}'.format(i)])
                if 'schedule_zone_{}'.format(i) in self.setup:
                    self.schedule_List[i][3].setText(
                        self.setup['schedule_zone_{}'.format(i)])
                if 'schedule_days_{}'.format(i) in self.setup:
                    self.schedule_List[i][5].setCurrentIndex(
                        self.setup['schedule_days_{}'.format(i)])
                if 'schedule_time_{}'.format(i) in self.setup:
                    times = self.setup['schedule_time_{}'.format(i)].split(',')
                    self.schedule_List[i][6].setTime(
                        QTime(int(times[0]), int(times[1]), int(times[2])))
                if 'schedule_act_{}'.format(i) in self.setup:
                    self.schedule_List[i][7].setChecked(
                        self.setup['schedule_act_{}'.format(i)])
        except:
            self.overlapzone_popup(
                '셋업 파일을 읽어 올 수 없어 초기화 되었습니다.', '에러', '셋업 파일을 읽어 올 수 없습니다.')

    # Scheduler
    @pyqtSlot(int)
    def schedule_file_load(self, index):
        file = QFileDialog.getOpenFileName(
            self, 'Select one or more files to open', '', 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)', None)
        self.schedule_List[index][1].setText(file[0])
        self.setup['schedule_file_{}'.format(index)] = file[0]
        self.setup_file_save()

    @pyqtSlot(int)
    def schedule_zone_sel(self, index):
        # print(index)
        select_zone = []
        for i in range(66):
            if 'zone_name_{}'.format(i+1) in self.setup:
                self.dialog.Qui.btn_zone_sel[i].setText(
                    self.setup['zone_name_{}'.format(i+1)])
            self.dialog.Qui.btn_zone_sel[i].setChecked(False)

        selected_zone = self.schedule_List[index][3].text().split(',')
        try:
            for i in range(len(selected_zone)):
                select_zone = [
                    item for item, value in self.setup.items() if value == selected_zone[i]]
                if 'zone_name_' in select_zone[0] and select_zone[0] in self.setup:
                    self.dialog.Qui.btn_zone_sel[int(
                        (re.findall('\d+', select_zone[0]))[0])-1].setChecked(True)
        except:
            pass

        if self.dialog.exec_():
            select_zone = []
            for i in range(len(self.dialog.Qui.btn_zone_sel)):
                if self.dialog.Qui.btn_zone_sel[i].isChecked():
                    select_zone.append(self.setup['zone_name_{}'.format(i+1)])
            if len(select_zone) == 0:
                select_zone_txt = ""
            else:
                select_zone_txt = ','.join(select_zone)
            self.schedule_List[index][3].setText(select_zone_txt)
            self.setup['schedule_zone_{}'.format(index)] = (select_zone_txt)
            self.setup_file_save()

    @pyqtSlot(int)
    def schedule_List_del(self, i):
        self.schedule_List[i][1].setText("")
        self.schedule_List[i][3].setText("")
        self.schedule_List[i][5].setCurrentIndex(0)
        self.schedule_List[i][6].setTime(QTime(0, 0, 0))
        self.schedule_List[i][7].setChecked(False)

        self.setup['schedule_file_{}'.format(i)] = ""
        self.setup['schedule_zone_{}'.format(i)] = ""
        self.setup['schedule_days_{}'.format(i)] = 0
        self.setup['schedule_time_{}'.format(i)] = '0,0,0'
        self.setup['schedule_act_{}'.format(i)] = False
        self.setup_file_save()

    @pyqtSlot(int)
    def schedule_copy(self, index):
        if self.copy_ID == 99:
            self.copy_ID = index
            self.schedule_List[index][9].setStyleSheet(
                "QPushButton{border:none;border-radius:15px;background-color:#18A9B4}")
        else:
            self.schedule_List[index][1].setText(
                self.schedule_List[self.copy_ID][1].text())
            self.schedule_List[index][3].setText(
                self.schedule_List[self.copy_ID][3].text())
            self.schedule_List[index][5].setCurrentIndex(
                self.schedule_List[self.copy_ID][5].currentIndex())
            self.schedule_List[index][6].setTime(
                self.schedule_List[self.copy_ID][6].time())
            self.schedule_List[index][7].setChecked(
                self.schedule_List[self.copy_ID][7].isChecked())
            self.setup['schedule_file_{}'.format(
                index)] = self.schedule_List[self.copy_ID][1].text()
            self.setup['schedule_zone_{}'.format(
                index)] = self.schedule_List[self.copy_ID][3].text()
            self.setup['schedule_days_{}'.format(
                index)] = self.schedule_List[self.copy_ID][5].currentIndex()
            self.setup['schedule_time_{}'.format(index)] = ('{},{},{}'.format(self.schedule_List[index][6].time(
            ).hour(), self.schedule_List[index][6].time().minute(), self.schedule_List[index][6].time().second()))
            self.setup['schedule_act_{}'.format(
                index)] = self.schedule_List[self.copy_ID][7].isChecked()
            self.setup_file_save()
            self.copy_ID = 99
            for i in range(200):
                self.schedule_List[i][9].setStyleSheet(self.btn_style_nomal)

    def schedule_value_change(self):
        for i in range(200):
            self.setup['schedule_days_{}'.format(
                i)] = self.schedule_List[i][5].currentIndex()
            self.setup['schedule_time_{}'.format(i)] = ('{},{},{}'.format(self.schedule_List[i][6].time(
            ).hour(), self.schedule_List[i][6].time().minute(), self.schedule_List[i][6].time().second()))
            self.setup['schedule_act_{}'.format(
                i)] = self.schedule_List[i][7].isChecked()
        self.setup_file_save()

    @pyqtSlot()
    def schedule_parcing(self):
        for i in range(200):
            if self.schedule_List[i][7].isChecked():
                if self.schedule_List[i][6].time().toString("hh:mm:ss") == QTime.currentTime().toString("hh:mm:ss"):
                    dt = datetime.datetime.now().weekday()
                    combobox_index = self.schedule_List[i][5].currentIndex()
                    for n in range(len(self.days_value[combobox_index])):
                        if self.days_value[combobox_index][n] == dt:
                            if self.btn_Play.isChecked() == False:
                                self.zone_list = self.schedule_zone_check(i)
                                overlap_zone_name = self.find_zone_overlap(
                                    self.zone_list)
                                # 방송구간 중복 확인
                                if overlap_zone_name:
                                    start_new_thread(self.log_server_call, ('0, {}부스 방송구간 중복으로 {}번 스케줄 방송이 실행되지 않았습니다. -{}-'.format(
                                        self.setup['boothNum']-9, i+1, ','.join(overlap_zone_name)),))
                                    self.overlapzone_popup(
                                        overlap_zone_name, '스케줄 방송', '방송구간 중복으로 스케쥴 방송이 중단됩니다.')
                                else:
                                    if os.path.isfile(self.schedule_List[i][1].text()):
                                        self.playLoop = 0
                                        broadcast_zone = []
                                        broadcast_zone_name = []
                                        for n in range(len(self.zone_list)):
                                            broadcast_zone.append('{}:{}'.format(
                                                self.zone_list[n], self.setup['boothNum']))
                                            broadcast_zone_name.append(
                                                self.setup['zone_name_{}'.format(self.zone_list[n])])
                                        start_new_thread(
                                            self.server_call, ('t:onair,{},!'.format(','.join(broadcast_zone)),))
                                        start_new_thread(self.log_server_call, ('0, {}부스 이벤트 방송 실행. -{}-'.format(
                                            self.setup['boothNum']-9, ','.join(broadcast_zone_name)),))
                                        self.overlapzone_popup(
                                            '{}번 스케줄이 실행되었습니다.'.format(i+1), '스케줄 방송', '스케쥴 방송 실행중')
                                        # play audio
                                        try:
                                            # self.audioDevice_Change.emit(self.setup['audioDeviceId'])
                                            # time.sleep(2)
                                            self.Play_Button_Status = 1
                                            # self.play.emit(self.schedule_List[i][1].text())
                                            start_new_thread(
                                                self.wait_play, (self.schedule_List[i][1].text(),))
                                            self.statusbar.showMessage(
                                                self.schedule_List[i][1].text())
                                            self.btn_Play.setChecked(True)
                                        except:
                                            self.statusbar.showMessage(
                                                '플레이어에 문제가 발생했습니다.', 5000)
                                            self.Play_Button_Status = 0
                                            self.btn_Play.setChecked(False)
                                    else:
                                        self.Play_Button_Status = 0
                                        self.btn_Play.setChecked(False)
                                        start_new_thread(self.log_server_call, ('0, {}부스 재생 파일 문제로 {}번 스케줄 방송이 실행되지 않았습니다.'.format(
                                            self.setup['boothNum']-9, i+1),))
                                        self.overlapzone_popup(
                                            self.schedule_List[i][1].text(), '스케줄 방송', '재생 파일 문제로 방송이 실행되지 않았습니다.')
                            else:
                                start_new_thread(self.log_server_call, ('0, 플레이어가 사용중이어서 {}번 부스 스케줄 방송이 실행되지 않았습니다.'.format(
                                    self.setup['boothNum']-9),))
                                self.overlapzone_popup(
                                    '스케줄 방송이 실행되지 않았습니다.', '스케줄 방송', '플레이어가 사용중 입니다.')

    @pyqtSlot()
    def scheduler_reset(self):
        for i in range(200):
            self.schedule_List[i][1].setText("")
            self.schedule_List[i][3].setText("")
            self.schedule_List[i][5].setCurrentIndex(0)
            self.schedule_List[i][6].setTime(QTime(0, 0, 0))
            self.schedule_List[i][7].setChecked(False)

            self.setup['schedule_file_{}'.format(i)] = ""
            self.setup['schedule_zone_{}'.format(i)] = ""
            self.setup['schedule_days_{}'.format(i)] = 0
            self.setup['schedule_time_{}'.format(i)] = '0,0,0'
            self.setup['schedule_act_{}'.format(i)] = False
        self.setup_file_save()
        start_new_thread(self.log_server_call, ('0, {}번 부스 스케줄이 리셋 되었습니다.'.format(
            self.setup['boothNum']-9),))

    def wait_play(self, playlist):
        time.sleep(2)
        self.play.emit(playlist)

    def find_zone_overlap(self, zone_list):
        zone_overlap = []
        zone_overlap_state = False
        for i in range(len(zone_list)):
            if self.zone_status[zone_list[i]] > 0 and self.zone_status[zone_list[i]] != self.setup['boothNum']:
                zone_overlap.append(
                    self.setup['zone_name_{}'.format(zone_list[i])])
        if len(zone_overlap) > 0:
            zone_overlap_state = True
        return (zone_overlap)

    def schedule_zone_check(self, index):
        zone_sel_status = []
        schedule_zone_sel = self.schedule_List[index][3].text().split(',')
        for i in range(len(schedule_zone_sel)):
            select_zone = [item for item, value in self.setup.items(
            ) if value == schedule_zone_sel[i]]
            if 'zone_name_' in select_zone[0] and select_zone[0] in self.setup:
                zone_sel_status.append(
                    int(re.findall('\d+', select_zone[0])[0]))
        return zone_sel_status


############################################################# Audio Player #############################################################

class audioplayer(QThread):
    player_Status = pyqtSignal(str, int)
    audio_devices = pyqtSignal(list)

    def __init__(self, parent=None):
        super(audioplayer, self).__init__(parent)
        self.new_Player()

    def new_Player(self):
        self.instance = vlc.Instance()
        self._player = self.instance.media_player_new()
        self.Event_Manager = self._player.event_manager()
        self.Event_Manager.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.songFinished)
        self.Event_Manager.event_attach(
            vlc.EventType.MediaPlayerLengthChanged, self.get_Media_Langth, self._player)
        self.Event_Manager.event_attach(
            vlc.EventType.MediaPlayerTimeChanged, self.pos_Callback, self._player)

    @pyqtSlot()
    def get_Audio_Devices(self):
        self.devices_name = []
        self.mods = self._player.audio_output_device_enum()
        if self.mods:
            mod = self.mods
            while mod:
                mod = mod.contents
                self.devices_name.append((mod.description).decode())
                mod = mod.next
        # print(self.devices_name)
        self.audio_devices.emit(self.devices_name)
        #print("audioplayer get devices")

    @pyqtSlot(int)
    def set_Audio_Device(self, deviceId):
        self.devices = []
        self.mods = self._player.audio_output_device_enum()
        if self.mods:
            mod = self.mods
            while mod:
                mod = mod.contents
                self.devices.append(mod.device)
                self.devices_name.append((mod.description).decode())
                mod = mod.next
        vlc.libvlc_audio_output_device_list_release(self.mods)
        self._player.audio_output_device_set(None, self.devices[deviceId])
        #print ("change Audio Device = {}".format(deviceId))

    @pyqtSlot(str)
    def play(self, music):
        if os.path.isfile(music):
            media = self.instance.media_new(music)
            self._player.set_media(media)
            self._player.play()

    @pyqtSlot()
    def pause(self):
        self._player.pause()

    @pyqtSlot()
    def stop(self):
        self.player_Status.emit('stop', 0)
        self._player.stop()
        self.new_Player()

    def songFinished(self, evnet):
        self.player_Status.emit('stop', 1)

    def pos_Callback(self, time, player):
        self.player_Status.emit('current_time', time.u.new_time)
        # print(time.u.new_time)

    def get_Media_Langth(self, time, player):
        self.player_Status.emit('length', time.u.new_length)

    @pyqtSlot(int)
    def audio_Vol_Set(self, vol):
        self._player.audio_set_volume(vol)

    @pyqtSlot()
    def audio_Vol_Get(self):
        self.player_Status.emit('vol', self._player.audio_get_volume())


class chimeplayer(QThread):
    def __init__(self, parent=None):
        super(chimeplayer, self).__init__(parent)
        self.new_Player()

    def new_Player(self):
        self.instance = vlc.Instance()
        self._player = self.instance.media_player_new()
        self.Event_Manager = self._player.event_manager()

    @pyqtSlot(str)
    def play(self, music):
        media = self.instance.media_new('chime.wav')
        self._player.set_media(media)
        self._player.play()


class udp_server(QThread):
    udp_data = pyqtSignal(str)

    def __init__(self, parent=None):
        super(udp_server, self).__init__(parent)
        MCAST_GRP = '224.1.128.128'
        MCAST_PORT = 5007
        self.sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except AttributeError:
            pass
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
        self.sock.bind(('', MCAST_PORT))
        host = socket.gethostbyname(socket.gethostname())
        self.sock.setsockopt(
            socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
        self.sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(
            MCAST_GRP) + socket.inet_aton(host))

    def run(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                self.udp_data.emit(data.decode('utf-8'))
                print('recv_data = {}'.format(data.decode('utf-8')))
            except (socket.error, e):
                print('Expection')
                hexdata = binascii.hexlify(data)
                print('Data = %s' % hexdata)


"""
class schedulePlay(QThread):
    Timer_Receive_String = pyqtSignal(int,int)
    def __init__(self, parent = None):
        super(schedulePlay, self).__init__(parent)
        self.tm_min = 0

    def run(self):
        while True:
            self.now = time.localtime(time.time())
            if self.tm_min != self.now.tm_min:
                self.tm_min = self.now.tm_min
                self.Timer_Receive_String.emit(self.now.tm_hour,self.now.tm_min)
            time.sleep(1)
            print(self.now.tm_hour,self.now.tm_min)
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
