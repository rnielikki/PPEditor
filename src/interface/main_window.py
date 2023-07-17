# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 651)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_entries = QtWidgets.QFrame(self.centralwidget)
        self.frame_entries.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame_entries.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_entries.setObjectName("frame_entries")
        self.hl_entry_container = QtWidgets.QHBoxLayout(self.frame_entries)
        self.hl_entry_container.setObjectName("hl_entry_container")
        self.frame = QtWidgets.QFrame(self.frame_entries)
        self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sc = QtWidgets.QScrollArea(self.frame)
        self.sc.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sc.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sc.setLineWidth(0)
        self.sc.setWidgetResizable(True)
        self.sc.setObjectName("sc")
        self.sc_content = QtWidgets.QWidget()
        self.sc_content.setGeometry(QtCore.QRect(0, 0, 599, 530))
        self.sc_content.setObjectName("sc_content")
        self.fl_fields = QtWidgets.QFormLayout(self.sc_content)
        self.fl_fields.setContentsMargins(0, 0, 10, 0)
        self.fl_fields.setHorizontalSpacing(20)
        self.fl_fields.setVerticalSpacing(10)
        self.fl_fields.setObjectName("fl_fields")
        self.sc.setWidget(self.sc_content)
        self.verticalLayout.addWidget(self.sc)
        self.hl_entry_container.addWidget(self.frame)
        self.gridLayout.addWidget(self.frame_entries, 1, 0, 1, 1)
        self.frame_controls = QtWidgets.QFrame(self.centralwidget)
        self.frame_controls.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame_controls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_controls.setObjectName("frame_controls")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_controls)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_controls)
        self.frame_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_raw_data = QtWidgets.QLabel(self.frame_2)
        self.lb_raw_data.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lb_raw_data.setObjectName("lb_raw_data")
        self.verticalLayout_2.addWidget(self.lb_raw_data)
        self.te_raw_data = QtWidgets.QTextEdit(self.frame_2)
        self.te_raw_data.setEnabled(True)
        self.te_raw_data.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.te_raw_data.setFrameShape(QtWidgets.QFrame.Box)
        self.te_raw_data.setUndoRedoEnabled(False)
        self.te_raw_data.setAcceptRichText(True)
        self.te_raw_data.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.te_raw_data.setObjectName("te_raw_data")
        self.verticalLayout_2.addWidget(self.te_raw_data)
        self.pb_edit_raw_data = QtWidgets.QPushButton(self.frame_2)
        self.pb_edit_raw_data.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_edit_raw_data.setObjectName("pb_edit_raw_data")
        self.verticalLayout_2.addWidget(self.pb_edit_raw_data)
        self.gridLayout_2.addWidget(self.frame_2, 13, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.frame_controls)
        self.line_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 2, 0, 1, 1)
        self.lb_file_name = QtWidgets.QLabel(self.frame_controls)
        self.lb_file_name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lb_file_name.setObjectName("lb_file_name")
        self.gridLayout_2.addWidget(self.lb_file_name, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lb_section = QtWidgets.QLabel(self.frame_controls)
        self.lb_section.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lb_section.setObjectName("lb_section")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_section)
        self.cb_sections = QtWidgets.QComboBox(self.frame_controls)
        self.cb_sections.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cb_sections.setObjectName("cb_sections")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_sections)
        self.lb_entry = QtWidgets.QLabel(self.frame_controls)
        self.lb_entry.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lb_entry.setObjectName("lb_entry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_entry)
        self.cb_entries = QtWidgets.QComboBox(self.frame_controls)
        self.cb_entries.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cb_entries.setObjectName("cb_entries")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_entries)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_controls)
        self.line.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 12, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_controls)
        self.line_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 6, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pb_paste_entry = QtWidgets.QPushButton(self.frame_controls)
        self.pb_paste_entry.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_paste_entry.setObjectName("pb_paste_entry")
        self.gridLayout_3.addWidget(self.pb_paste_entry, 0, 1, 1, 1)
        self.pb_copy_entry = QtWidgets.QPushButton(self.frame_controls)
        self.pb_copy_entry.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_copy_entry.setObjectName("pb_copy_entry")
        self.gridLayout_3.addWidget(self.pb_copy_entry, 0, 0, 1, 1)
        self.pb_remove_current_entry = QtWidgets.QPushButton(self.frame_controls)
        self.pb_remove_current_entry.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_remove_current_entry.setObjectName("pb_remove_current_entry")
        self.gridLayout_3.addWidget(self.pb_remove_current_entry, 1, 0, 1, 1)
        self.pb_add_new_entry = QtWidgets.QPushButton(self.frame_controls)
        self.pb_add_new_entry.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_add_new_entry.setObjectName("pb_add_new_entry")
        self.gridLayout_3.addWidget(self.pb_add_new_entry, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lb_section_size = QtWidgets.QLabel(self.frame_controls)
        self.lb_section_size.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lb_section_size.setObjectName("lb_section_size")
        self.gridLayout_4.addWidget(self.lb_section_size, 0, 0, 1, 1)
        self.le_section_size = QtWidgets.QLineEdit(self.frame_controls)
        self.le_section_size.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.le_section_size.setObjectName("le_section_size")
        self.gridLayout_4.addWidget(self.le_section_size, 0, 1, 1, 1)
        self.lb_entry_amount = QtWidgets.QLabel(self.frame_controls)
        self.lb_entry_amount.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lb_entry_amount.setObjectName("lb_entry_amount")
        self.gridLayout_4.addWidget(self.lb_entry_amount, 1, 0, 1, 1)
        self.le_section_entry_amount = QtWidgets.QLineEdit(self.frame_controls)
        self.le_section_entry_amount.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.le_section_entry_amount.setObjectName("le_section_entry_amount")
        self.gridLayout_4.addWidget(self.le_section_entry_amount, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.pb_add_new_section = QtWidgets.QPushButton(self.frame_controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_add_new_section.sizePolicy().hasHeightForWidth())
        self.pb_add_new_section.setSizePolicy(sizePolicy)
        self.pb_add_new_section.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pb_add_new_section.setObjectName("pb_add_new_section")
        self.horizontalLayout.addWidget(self.pb_add_new_section)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_controls, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.action_load = QtWidgets.QAction(MainWindow)
        self.action_load.setObjectName("action_load")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_refresh = QtWidgets.QAction(MainWindow)
        self.action_refresh.setObjectName("action_refresh")
        self.action_p1 = QtWidgets.QAction(MainWindow)
        self.action_p1.setCheckable(True)
        self.action_p1.setEnabled(False)
        self.action_p1.setObjectName("action_p1")
        self.action_p2 = QtWidgets.QAction(MainWindow)
        self.action_p2.setCheckable(True)
        self.action_p2.setEnabled(False)
        self.action_p2.setObjectName("action_p2")
        self.action_p3 = QtWidgets.QAction(MainWindow)
        self.action_p3.setCheckable(True)
        self.action_p3.setEnabled(False)
        self.action_p3.setObjectName("action_p3")
        self.check_backup = QtWidgets.QAction(MainWindow)
        self.check_backup.setCheckable(True)
        self.check_backup.setChecked(True)
        self.check_backup.setObjectName("check_backup")
        self.action_guides = QtWidgets.QAction(MainWindow)
        self.action_guides.setEnabled(False)
        self.action_guides.setObjectName("action_guides")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setEnabled(False)
        self.action_about.setObjectName("action_about")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.menuFile.addAction(self.action_load)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_save_as)
        self.menuFile.addAction(self.action_refresh)
        self.menuMode.addAction(self.action_p1)
        self.menuMode.addAction(self.action_p2)
        self.menuMode.addAction(self.action_p3)
        self.menuSettings.addAction(self.check_backup)
        self.menuHelp.addAction(self.action_guides)
        self.menuHelp.addAction(self.action_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patapon Param Editor"))
        self.lb_raw_data.setText(_translate("MainWindow", "Raw data"))
        self.pb_edit_raw_data.setText(_translate("MainWindow", "Edit raw data"))
        self.pb_edit_raw_data.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.lb_file_name.setText(_translate("MainWindow", "Filename:"))
        self.lb_section.setText(_translate("MainWindow", "Section"))
        self.lb_entry.setText(_translate("MainWindow", "Entry"))
        self.pb_paste_entry.setText(_translate("MainWindow", "Paste entry"))
        self.pb_paste_entry.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.pb_copy_entry.setText(_translate("MainWindow", "Copy entry"))
        self.pb_copy_entry.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.pb_remove_current_entry.setText(_translate("MainWindow", "Remove entry"))
        self.pb_remove_current_entry.setShortcut(_translate("MainWindow", "Ctrl+Del"))
        self.pb_add_new_entry.setText(_translate("MainWindow", "Add new entry"))
        self.pb_add_new_entry.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.lb_section_size.setText(_translate("MainWindow", "Section size"))
        self.lb_entry_amount.setText(_translate("MainWindow", "Entry amount"))
        self.pb_add_new_section.setText(_translate("MainWindow", "Add new section"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action_load.setText(_translate("MainWindow", "Load"))
        self.action_load.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_refresh.setText(_translate("MainWindow", "Refresh"))
        self.action_refresh.setShortcut(_translate("MainWindow", "F5"))
        self.action_p1.setText(_translate("MainWindow", "Patapon 1"))
        self.action_p2.setText(_translate("MainWindow", "Patapon 2"))
        self.action_p3.setText(_translate("MainWindow", "Patapon 3"))
        self.check_backup.setText(_translate("MainWindow", "Save backups"))
        self.action_guides.setText(_translate("MainWindow", "Guides"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.action_save_as.setText(_translate("MainWindow", "Save as"))
        self.action_save_as.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
