import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_windo import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel

from connection import Data
import calcfunc as calc_f

from dozecalc_window import Ui_Dialog as Doz_Dilog
from guide import Ui_Dialog as Guide_Dilog
from ppd_window import Ui_Dialog as Ppd_Dilog

from PySide6.QtSql import QSqlTableModel


class Calculator_activity(QMainWindow):
    def __init__(self):
        super(Calculator_activity, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        if not self.conn.create_connection():  # Проверяем, удалось ли подключиться
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных. Программа будет закрыта.")
            sys.exit(1)
        self.model = QSqlTableModel(self)
        self.ui.pushButton_menu_guide.clicked.connect(self.open_guide)
        self.ui.pushButton_ppd.clicked.connect(self.open_ppd_window)
        self.ui.pushButton_menu_dozcal.clicked.connect(self.open_dozcalc_window)


    def view_data(self, table_name, table_view):
        self.model.setTable(table_name)
        self.model.select()
        table_view.setModel(self.model)
    def view_data_dz(self):
        self.view_data("activitycalc", self.dozc_ui.tableView_dozcalc_result)

    def viw_data_ppd(self):
        self.view_data("activitycalc", self.ppd_ui.tableView_ppd_result)

    def open_guide(self):
        self.guide_window = QtWidgets.QDialog()
        self.guide_ui = Guide_Dilog()
        self.guide_ui.setupUi(self.guide_window)
        self.guide_window.show()
        #self.guide_ui.pushButton_fun.clicked.connect()
    
    def open_dozcalc_window(self):
        if not hasattr(self, "dozcalc_wind"):
            self.dozcalc_wind = QtWidgets.QDialog()
            self.dozc_ui = Doz_Dilog()
            self.dozc_ui.setupUi(self.dozcalc_wind)
            self.dozc_ui.pushButton_dozc_calc.clicked.connect(self.calculation_activity_dozc)
        self.view_data_dz()
        self.dozcalc_wind.show()

    def open_ppd_window(self):
        if not hasattr(self, "ppd_window"):
            self.ppd_window = QtWidgets.QDialog()
            self.ppd_ui = Ppd_Dilog()
            self.ppd_ui.setupUi(self.ppd_window)
            self.ppd_ui.pushButton_ppd_calc.clicked.connect(self.calculation_activity_ppd)
        self.viw_data_ppd()
        self.ppd_window.show()


    def calculation_activity_dozc(self):
        date_dz = self.dozc_ui.date_dozc_day.text()
        act_text_edit_dz = [self.dozc_ui.lineEdit_dozc_data_1, self.dozc_ui.lineEdit_dozc_data_2, self.dozc_ui.lineEdit_dozc_data_3,
                         self.dozc_ui.lineEdit_dozc_data_4, self.dozc_ui.lineEdit_dozc_data_5]
        act_data_dz = [float(i.text()) for i in act_text_edit_dz]
        seri_dz = self.dozc_ui.comboBox_dozc_usil.currentText()
        time_plus_dz = self.dozc_ui.timeEdit_dozc_timeplus.text()
        time_start_dz = self.dozc_ui.timeEdit_dozc_timestart.text()
        time_sep_dz = self.dozc_ui.timeEdit_dozc_timesep.text()

        if seri_dz == "11,5":
            stat = calc_f.statistic(act_data_dz)
            data_dz = round(sum(act_data_dz)/len(act_data_dz), 3)
            self.conn.add_new_measurm_query(date_dz, instr= "DZ", seri_num = seri_dz, geom = 'geom_dz', activ= data_dz, error=stat, output= '0.0')
        
        else:
            resilt_calc_dz = calc_f.output_dz(time_sep=time_sep_dz, time_start=time_start_dz, date=date_dz, dat=act_data_dz, expos=time_plus_dz)
            self.conn.add_new_measurm_query(date_dz, instr= "DZ", seri_num = seri_dz, geom = 'geom_dz', activ= resilt_calc_dz[0], error=resilt_calc_dz[1], output= '0.0')
        
        self.view_data_dz()
        
    def calculation_activity_ppd(self):
        date_ppd = self.ppd_ui.date_ppd_mes.text()
        act_text_edit_ppd = [self.ppd_ui.lineEdit_ppd_data_1, self.ppd_ui.lineEdit_ppd_data_2, self.ppd_ui.lineEdit_ppd_data_3, self.ppd_ui.lineEdit_ppd_data_4]
        act_data_ppd = [int(i.text()) for i in act_text_edit_ppd]
        time_sep_ppd = self.ppd_ui.timeEdit_ppd__timesep.text()
        time_meas_ppd = self.ppd_ui.timeEdit_ppd_timemesh.text()
        seria_ppd = self.ppd_ui.comboBox_ppd_seria.currentText()
        geom_ppd = self.ppd_ui.comboBox_ppd_geom.currentText()
        dead_time_ppd = int(self.ppd_ui.lineEdit_ppd_dt.text())
        expos_ppd = int(self.ppd_ui.lineEdit_ppd_expos.text())
        result_ppdcalc = calc_f.activity_calculation(data=act_data_ppd, exp=expos_ppd, time_separation=time_sep_ppd, time_start_meas=time_meas_ppd, ser=seria_ppd, geo=geom_ppd, deadtime=dead_time_ppd, date_of_measurment=date_ppd)
        self.conn.add_new_measurm_query(date_ppd, instr= "PPD", seri_num = seria_ppd, geom = geom_ppd, activ= result_ppdcalc[0], error=result_ppdcalc[1], output= result_ppdcalc[2])
        self.viw_data_ppd()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator_activity()
    window.show()
    sys.exit(app.exec())
    
