# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miniproject.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import calculator
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 111, 17))
        self.label_5.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_5.setObjectName("label_5")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 30, 741, 111))
        self.listView.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.listView.setObjectName("listView")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 190, 361, 341))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_batsman = QtWidgets.QRadioButton(self.frame)
        self.select_batsman.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.select_batsman.setObjectName("select_batsman")
        self.horizontalLayout.addWidget(self.select_batsman)
        self.select_bowler = QtWidgets.QRadioButton(self.frame)
        self.select_bowler.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_bowler.setObjectName("select_bowler")
        self.horizontalLayout.addWidget(self.select_bowler)
        self.select_allrounder = QtWidgets.QRadioButton(self.frame)
        self.select_allrounder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_allrounder.setObjectName("select_allrounder")
        self.horizontalLayout.addWidget(self.select_allrounder)
        self.select_wicketkeeper = QtWidgets.QRadioButton(self.frame)
        self.select_wicketkeeper.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_wicketkeeper.setObjectName("select_wicketkeeper")
        self.horizontalLayout.addWidget(self.select_wicketkeeper)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.avail_team = QtWidgets.QListWidget(self.frame)
        self.avail_team.setObjectName("avail_team")
        self.verticalLayout.addWidget(self.avail_team)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 160, 186, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.avail_points = QtWidgets.QLineEdit(self.layoutWidget)
        self.avail_points.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 168, 191);")
        self.avail_points.setReadOnly(True)
        self.avail_points.setObjectName("avail_points")
        self.horizontalLayout_3.addWidget(self.avail_points)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(420, 160, 161, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.used_points = QtWidgets.QLineEdit(self.layoutWidget1)
        self.used_points.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 168, 191);\n"
"")
        self.used_points.setReadOnly(True)
        self.used_points.setObjectName("used_points")
        self.horizontalLayout_4.addWidget(self.used_points)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(410, 190, 351, 341))
        self.frame1.setObjectName("frame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 168, 191);\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.selected_team = QtWidgets.QListWidget(self.frame1)
        self.selected_team.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selected_team.setObjectName("selected_team")
        self.verticalLayout_2.addWidget(self.selected_team)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 80, 731, 43))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.numofbatsman = QtWidgets.QLineEdit(self.frame_2)
        self.numofbatsman.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 168, 191);")
        self.numofbatsman.setReadOnly(True)
        self.numofbatsman.setObjectName("numofbatsman")
        self.horizontalLayout_5.addWidget(self.numofbatsman)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.numofbowlers = QtWidgets.QLineEdit(self.frame_2)
        self.numofbowlers.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 168, 191);")
        self.numofbowlers.setReadOnly(True)
        self.numofbowlers.setObjectName("numofbowlers")
        self.horizontalLayout_5.addWidget(self.numofbowlers)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.numofallrounders = QtWidgets.QLineEdit(self.frame_2)
        self.numofallrounders.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 168, 191);")
        self.numofallrounders.setReadOnly(True)
        self.numofallrounders.setObjectName("numofallrounders")
        self.horizontalLayout_5.addWidget(self.numofallrounders)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.numofwicketkeeper = QtWidgets.QLineEdit(self.frame_2)
        self.numofwicketkeeper.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 168, 191);\n"
"")
        self.numofwicketkeeper.setReadOnly(True)
        self.numofwicketkeeper.setObjectName("numofwicketkeeper")
        self.horizontalLayout_5.addWidget(self.numofwicketkeeper)
        self.frame.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.listView.raise_()
        self.label_5.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionEvaluate_Team_2 = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team_2.setObjectName("actionEvaluate_Team_2")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.avail_players={}
        self.select_players={}
        self.noofplayers=0
        self.select_batsman.toggled.connect(self.category)
        self.select_bowler.toggled.connect(self.category)
        self.select_allrounder.toggled.connect(self.category)
        self.select_wicketkeeper.toggled.connect(self.category)
        self.avail_team.itemDoubleClicked.connect(self.new_team)
        self.selected_team.itemDoubleClicked.connect(self.delete_player)
        self.connect=sqlite3.connect('project.db')
        self.cursor=self.connect.cursor()
        


    def menufunction(self,action):
        text=action.text()
        if text=='NEW Team':
            self.open_dialog_box()
        if text=='SAVE Team':
            self.save_team()
        if text=='EVALUATE Team':
            self.evaluate()
        if text=='OPEN Team':
            self.open()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Team selections"))
        self.select_batsman.setText(_translate("MainWindow", "BAT"))
        self.select_bowler.setText(_translate("MainWindow", "BOW"))
        self.select_allrounder.setText(_translate("MainWindow", "AR"))
        self.select_wicketkeeper.setText(_translate("MainWindow", "WK"))
        self.label.setText(_translate("MainWindow", "Points Available"))
        self.avail_points.setText(_translate("MainWindow", "####"))
        self.label_2.setText(_translate("MainWindow", "Points Used"))
        self.used_points.setText(_translate("MainWindow", "####"))
        self.label_3.setText(_translate("MainWindow", "Team Name"))
        self.label_4.setText(_translate("MainWindow", "Displayed Here"))
        self.label_6.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.numofbatsman.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.numofbowlers.setText(_translate("MainWindow", "##"))
        self.label_8.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.numofallrounders.setText(_translate("MainWindow", "##"))
        self.label_9.setText(_translate("MainWindow", "Wicket-Keeper (WK)"))
        self.numofwicketkeeper.setText(_translate("MainWindow", "##"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionEvaluate_Team_2.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
    def open_dialog_box(self):
        Dialog = QtWidgets.QDialog(MainWindow)
        ui3 = Ui_Dialog()
        ui3.setupUi(Dialog)
        check=Dialog.exec_()
        if check==QtWidgets.QDialog.Accepted:
            self.selected_newteam=ui3.newteamname.text()
            if self.selected_newteam!="":
                self.label_4.setText(self.selected_newteam)
                self.numofbatsman.setText('0')
                self.numofbowlers.setText('0')
                self.numofallrounders.setText('0')
                self.numofwicketkeeper.setText('0')
                self.avail_points.setText('1000')
                self.used_points.setText('0')
                self.cursor.execute('SELECT Player,ctg FROM stats;')
                self.select_players.clear()
                self.avail_players.clear()
                player_list=list(self.cursor.fetchall())
                for i in player_list:
                    self.avail_players[i[0]]=i[1]
                self.selected_team.clear()
                self.noofplayers=0
            else:
                self.create_message_box('Teamname is required to create a cricket team')
    
    def category(self):
        self.avail_team.clear()
        if self.select_batsman.isChecked()==True:
            for player in self.avail_players.keys():
                if self.avail_players[player]=='BAT':
                    self.avail_team.addItem(player)        
        elif self.select_bowler.isChecked()==True:
            for player in self.avail_players.keys():
                if self.avail_players[player]=='BWL':
                    self.avail_team.addItem(player)
        elif self.select_allrounder.isChecked()==True:
            for player in self.avail_players.keys():
                if self.avail_players[player]=='AR':
                    self.avail_team.addItem(player)
        elif self.select_wicketkeeper.isChecked()==True:
            for player in self.avail_players.keys():
                if self.avail_players[player]=='WK':
                    self.avail_team.addItem(player)
    
    def new_team(self,item):
        if self.noofplayers<11:
            self.member=item.text()
            self.cursor.execute('SELECT value FROM stats where player="{}"'.format(self.member))
            score=list(self.cursor.fetchall())
            score=score[0][0]
            val=int(self.avail_points.text())
            val1=int(self.used_points.text())
            if val-score>=0:
                if self.avail_players[self.member]=='WK':
                    if int(self.numofwicketkeeper.text())==0:
                        self.avail_team.takeItem(self.avail_team.row(item))
                        self.selected_team.addItem(self.member)
                        wk_counter=int(self.numofwicketkeeper.text())
                        wk_counter+=1
                        self.numofwicketkeeper.setText(str(wk_counter))
                        scr=val-score
                        self.avail_points.setText(str(scr))
                        tot=val1+score
                        self.used_points.setText(str(tot))
                        self.select_players[self.member]=self.avail_players[self.member]
                        del self.avail_players[self.member]
                        self.noofplayers+=1
                    else:
                        self.create_message_box('More than one Wicket-Keeper is not allowed')
                else:
                    if self.avail_players[self.member]=='BAT':
                        self.avail_team.takeItem(self.avail_team.row(item))
                        bat_counter=int(self.numofbatsman.text())
                        bat_counter+=1
                        self.numofbatsman.setText(str(bat_counter))
                    if self.avail_players[self.member]=='BWL':
                        self.avail_team.takeItem(self.avail_team.row(item))
                        bwl_counter=int(self.numofbowlers.text())
                        bwl_counter+=1
                        self.numofbowlers.setText(str(bwl_counter))
                    if self.avail_players[self.member]=='AR':
                        self.avail_team.takeItem(self.avail_team.row(item))
                        ar_counter=int(self.numofallrounders.text())
                        ar_counter+=1
                        self.numofallrounders.setText(str(ar_counter))
                    scr=val-score
                    self.avail_points.setText(str(scr))
                    tot=val1+score
                    self.used_points.setText(str(tot))
                    self.selected_team.addItem(self.member)
                    self.select_players[self.member]=self.avail_players[self.member]
                    del self.avail_players[self.member]
                    self.noofplayers+=1
            else:
                self.create_message_box('You cant add this player')
        else:
            self.create_message_box('cricket team should not exceed 11 players')   
        
    def create_message_box(self,txt):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(txt)
        msg.setWindowTitle('Alert')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    def create_info_message_box(self,txt):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(txt)
        msg.setWindowTitle('Notification')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()    
    

    def delete_player(self,item):
        self.delmem=item.text()
        self.cursor.execute('SELECT value FROM stats where player="{}"'.format(self.delmem))
        delscore=list(self.cursor.fetchall())
        delscore=delscore[0][0]
        newval=int(self.used_points.text())
        newval1=int(self.avail_points.text())
        if self.select_players[self.delmem]=='WK':
            self.selected_team.takeItem(self.selected_team.row(item))
            self.numofwicketkeeper.setText(str(0))
        elif self.select_players[self.delmem]=='BAT':
            self.selected_team.takeItem(self.selected_team.row(item))
            bat_decounter=int(self.numofbatsman.text())
            bat_decounter-=1
            self.numofbatsman.setText(str(bat_decounter))
        elif self.select_players[self.delmem]=='BWL':
            self.selected_team.takeItem(self.selected_team.row(item))
            bwl_decounter=int(self.numofbowlers.text())
            bwl_decounter-=1
            self.numofbowlers.setText(str(bwl_decounter))
        elif self.select_players[self.delmem]=='AR':
            self.selected_team.takeItem(self.selected_team.row(item))
            ar_decounter=int(self.numofallrounders.text())
            ar_decounter-=1
            self.numofallrounders.setText(str(ar_decounter))
        scr1=newval-delscore
        self.used_points.setText(str(scr1))
        tot1=newval1+delscore
        self.avail_points.setText(str(tot1))
        self.avail_players[self.delmem]=self.select_players[self.delmem]
        del self.select_players[self.delmem]
        self.noofplayers-=1

    def save_team(self):
        selected_players=" ".join(self.select_players)
        li=[]
        if self.label_4.text()!="Displayed Here":
            self.cursor.execute('SELECT name FROM teams;')
            tn=list(self.cursor.fetchall())
            for i in tn:
                li.append(i[0])
            if len(self.select_players)==11:
                if self.label_4.text() in li:
                    self.cursor.execute('DELETE FROM teams WHERE name="{}"'.format(self.label_4.text()))
                    self.cursor.execute('INSERT INTO teams(name,players,value) VALUES("{}","{}","{}")'.format(self.label_4.text(),selected_players,self.used_points.text()))
                else:
                    self.cursor.execute('INSERT INTO teams(name,players,value) VALUES("{}","{}","{}")'.format(self.label_4.text(),selected_players,self.used_points.text()))
                self.connect.commit()
                self.create_info_message_box('Your team has been saved successfully!!')
            else:
                self.create_message_box('cricket team should have exactly 11 players')
        else:
            self.create_message_box('cricket team should be created to save the team')


    def evaluate(self):
        Dialog = QtWidgets.QDialog(MainWindow)
        ui1 = Ui1_Dialog()
        ui1.setupUi(Dialog)
        Dialog.exec_()

    def open(self):
        Dialog = QtWidgets.QDialog(MainWindow)
        ui2 = Ui2_Dialog()
        ui2.setupUi(Dialog)
        check1=Dialog.exec_()
        if check1==QtWidgets.QDialog.Accepted:
            self.team_name=ui2.teamselection.currentText()
            if self.team_name!='select team':
                self.label_4.setText(self.team_name)
                self.numofbatsman.setText('0')
                self.numofbowlers.setText('0')
                self.numofallrounders.setText('0')
                self.numofwicketkeeper.setText('0')
                self.avail_points.setText('1000')
                self.used_points.setText('0')
                self.selected_team.clear()
                self.noofplayers=0
                self.openteams()
            else:
                self.create_message_box('selection of teamname is required to open a team')

    def openteams(self):
        self.select_players.clear()
        self.avail_players.clear()
        self.cursor.execute('SELECT players,value FROM teams WHERE name="{}"'.format(self.team_name))
        open_players=list(self.cursor.fetchall())
        open_players1=open_players[0][0].split(" ")
        self.selected_team.addItems(open_players1)
        players_score=open_players[0][1]
        self.used_points.setText(str(players_score))
        rem_score=int(self.avail_points.text())-int(players_score)
        self.avail_points.setText(str(rem_score))
        self.cursor.execute('SELECT player,ctg from stats;')
        selected=list(self.cursor.fetchall())
        for i in selected:
            if i[0] in open_players1:
                self.select_players[i[0]]=i[1]
            else:
                self.avail_players[i[0]]=i[1]
        for op in self.select_players.keys():
            if self.select_players[op]=='BAT':
                count_batsman=int(self.numofbatsman.text())
                count_batsman+=1
                self.numofbatsman.setText(str(count_batsman))
            if self.select_players[op]=='BWL':
                count_bowlers=int(self.numofbowlers.text())
                count_bowlers+=1
                self.numofbowlers.setText(str(count_bowlers))
            if self.select_players[op]=='AR':
                count_allrounders=int(self.numofallrounders.text())
                count_allrounders+=1
                self.numofallrounders.setText(str(count_allrounders))
            if self.select_players[op]=='WK':
                count_wicketkeeper=int(self.numofwicketkeeper.text())
                count_wicketkeeper+=1
                self.numofwicketkeeper.setText(str(count_wicketkeeper))
            self.noofplayers+=1


        


class Ui2_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        font = QtGui.QFont()
        font.setUnderline(True)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 260, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 40, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.teamselection = QtWidgets.QComboBox(Dialog)
        self.teamselection.setGeometry(QtCore.QRect(120, 120, 151, 25))
        self.teamselection.setObjectName("teamselection")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.connect=sqlite3.connect('project.db')
        self.cursor=self.connect.cursor()
        self.teamselection.addItem('select team')
        self.teamselection.setCurrentText('select team')
        self.cursor.execute('SELECT name FROM teams')
        team=list(self.cursor.fetchall())
        for i in team:
            self.teamselection.addItem(i[0])
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Your Team"))
        

class Ui1_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(727, 500)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 20, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 67, 17))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(50, 100, 591, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listofplayers = QtWidgets.QListWidget(Dialog)
        self.listofplayers.setGeometry(QtCore.QRect(110, 161, 256, 271))
        self.listofplayers.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listofplayers.setAutoScroll(True)
        self.listofplayers.setObjectName("listofplayers")
        self.listofscores = QtWidgets.QListWidget(Dialog)
        self.listofscores.setGeometry(QtCore.QRect(390, 160, 256, 271))
        self.listofscores.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listofscores.setAutoScroll(True)
        self.listofscores.setObjectName("listofscores")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(110, 60, 441, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_team = QtWidgets.QComboBox(self.widget)
        self.select_team.setEditable(False)
        self.select_team.setObjectName("select_team")
        self.horizontalLayout.addWidget(self.select_team)
        self.select_match = QtWidgets.QComboBox(self.widget)
        self.select_match.setObjectName("select_match")
        self.horizontalLayout.addWidget(self.select_match)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(390, 120, 131, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.score_cal = QtWidgets.QLineEdit(self.widget1)
        self.score_cal.setStyleSheet("color: rgb(64, 168, 191);")
        self.score_cal.setReadOnly(True)
        self.score_cal.setObjectName("score_cal")
        self.horizontalLayout_2.addWidget(self.score_cal)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(240, 450, 251, 27))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(60)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calculation = QtWidgets.QPushButton(self.widget2)
        self.calculation.setObjectName("calculation")
        self.horizontalLayout_3.addWidget(self.calculation)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.buttonBox.setFont(font)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.select_team.activated.connect(self.play_list)
        self.select_match.activated.connect(self.button)
        self.calculation.clicked.connect(self.evaluate_score)
        self.connect=sqlite3.connect('project.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('SELECT name FROM teams')
        team_names=list(self.cursor.fetchall())
        self.select_team.addItem('Select Team')
        self.select_team.setCurrentText('Select Team')
        for i in team_names:
            self.select_team.addItem(i[0])
        self.select_match.addItem('Select Match')
        self.select_match.addItem('match1')
        self.select_match.setEnabled(False)
        self.calculation.setEnabled(False)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the performance of your Fantasy team"))
        self.label_2.setText(_translate("Dialog", "Players"))
        self.label_3.setText(_translate("Dialog", "Points"))
        self.score_cal.setText(_translate("Dialog", "0"))
        self.calculation.setText(_translate("Dialog", "calculate score"))

    def play_list(self):
        if self.select_team.currentText()!='Select Team':
            self.select_match.setEnabled(True)
            self.select_match.setCurrentText('Select Match')
            self.listofplayers.clear()
            teamname=self.select_team.currentText()
            self.cursor.execute('SELECT players FROM teams WHERE name="{}"'.format(teamname))
            self.getplayers=list(self.cursor.fetchall())
            self.getplayers=self.getplayers[0][0]
            self.setplayer=self.getplayers.split(" ")
            self.listofplayers.addItems(self.setplayer)
            self.listofscores.clear()
            self.score_cal.setText('0')
        else:
            self.calculation.setEnabled(False)
            self.select_match.setEnabled(False)
    def button(self):
        if self.select_match.currentText()!='Select Match':
            self.calculation.setEnabled(True)
        else:
            self.calculation.setEnabled(False)
        
    def evaluate_score(self):
        lis=['scored','faced','fours','sixes','bowled','given','wkts','catches','stumping','run_out']
        score_dic={}
        total_score=0
        ind_score=0
        for i in self.setplayer:
            for j in lis:
                self.cursor.execute('SELECT {} FROM match WHERE player="{}"'.format(j,i))
                score_dic[j]=list(self.cursor.fetchall())[0][0]
            ind_score=calculator.batting_points(score_dic)+calculator.bowling_points(score_dic)
            total_score+=ind_score
            score_dic={}
            self.listofscores.addItem(str(ind_score))
        lis=[]
        self.score_cal.setText(str(total_score))
        self.select_match.setEnabled(False)
        self.calculation.setEnabled(False)

           
            



        


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.newteamname = QtWidgets.QLineEdit(self.frame)
        self.newteamname.setObjectName("newteamname")
        self.horizontalLayout.addWidget(self.newteamname)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "New Team :"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
