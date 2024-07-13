import sqlite3
import sys
from pathlib import Path
from contextlib import closing

class SqlExecuttionToSqlite:
    """
    SQL execution class to Sqlite.
    """
    def __init__(self,db_filepath):
        """
        argument;
            - db_filepath:sqlite file path
        """
        self.db_name = db_filepath
    
    def create_sqlitefile(self):
        """
        explanation;
            Create a file if sqlite file does not exist.       
        """
        try:
            # コネクションの作成。ファイルがない場合は作成される
            conn = sqlite3.connect(self.db_name)
            # コネクションを閉じる
            conn.close()
        except sqlite3.Error as e:
            print(e)
            
            
    def execute_sql(self,mode,sql,data=None):
        """
        explanation;
            Function to execute sql.
            Execute sql after specifying mode.
        argument;
            - mode:
                select -> Returns header and value.
                insert -> Separate the data you want to insert from the SQL frame.
                others -> Assume a Create statement.
            - sql:
                The SQL to be executed.
            - data:
                Pass the data to be Inserted as a tuple type.
                If there is more than one data, pass a list of tuple type data records.                
            
        """        
        try:
            with closing(sqlite3.connect(self.db_path)) as conn:
                cur = conn.cursor()
                if mode=="select":
                    cur.execute(sql)
                    header = [description[0] for description in cur.description]
                    values = cur.fetchall()
                    return header,values
                    
                elif mode== "insert":
                    if type(data) == tuple:
                        cur.execute(sql,data)
                    else:
                        cur.executemany(sql,data)
                        
                    
                else:
                    # create table系を想定
                    cur.execute(sql)
                                
                conn.commit()
        except sqlite3.Error as e:
            print(e)

