from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("activity_db.db")

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database", "Click Cancel to exit", QtWidgets.QMessageBox.Cancel)
            return False
        
        query = QtSql.QSqlQuery()
        query.exec("""
            CREATE TABLE IF NOT EXISTS activitycalc (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Date VARCHAR(20),
            Instr VARCHAR(20),
            Seri_num VARCHAR(20),
            Geom VARCHAR(20),
            Activity REAL,
            Error REAL,
            Output REAL)
            """)


        return True

    def execute_query_with_params(self, sql_query, query_values = None): # коcнструктор запросов с параметрами в БД 
        query = QtSql.QSqlQuery() 
        query.prepare(sql_query)

        if query_values is not None:
            for query_vals in query_values:
                query.addBindValue(query_vals)
        query.exec()
        return query
    
    
    def add_new_measurm_query(self, date, instr, seri_num, geom, activ, error, output):
        sql_query = "INSERT INTO activitycalc (Date, Instr, Seri_num, Geom, Activity, Error, Output) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, instr, seri_num, geom, activ, error, output])

    
    # def qet_five_last_res(self, date_coll):
    #     sql_query = f"SELECT Date, Instr, Activity, Error FROM activitycalc ORDER BY {date_coll} DESC LIMIT 5"
    #     query = self.execute_query_with_params(sql_query)
    #     return query
        

    

