#!/usr/bin/python2
import sqlite3
# Got some great tips from:
# http://www.pythoncentral.io/introduction-to-sqlite-in-python/

# Class to manage all database operations
class DatabaseBuilder:

    # Create a new database connection _
    def __init__(self, dbfile, dbstruct):
        self.msg = '\n=======__init--() ==='    
        try:
            self.dbfile = dbfile
            self.dbstruct = dbstruct
            self.db = sqlite3.connect(self.dbfile) 
            self.msg += '\nStarted DB'    
            self.build()
        except Exception as e:
            self.msg += '\nERROR: '+str(e)   

    # Build the db and create the structure if it doesn't exist
    def build(self):
        self.msg = '\n====--database build()====='  
        try:
            cursor = self.db.cursor()
            # lets loop through our structure 
            for tablename in self.dbstruct:
                # Check if our table exists
                qry = "SELECT * FROM sqlite_master WHERE type='table' AND name='{}';".format(tablename)
                cursor.execute(qry)
                table = str(cursor.fetchone())
                # It doesn't seem to exist so lets create it
                if table == 'None':
                    fieldlist = s = ''
                    for fieldname in self.dbstruct[tablename]:
                        fieldtype = self.dbstruct[tablename][fieldname]
                        if fieldlist != '': s = ','
                        fieldlist += '{}{} {}'.format(s, fieldname,fieldtype)
                    qry = 'CREATE TABLE {0} ({1})'.format(tablename, fieldlist)
                    cursor.execute(qry)
                    self.msg += '\nBuilt a new database'
                else:
                    self.msg += '\nFound "{}" so didn\'t recreate it'.format(tablename) 
            self.db.commit()
            return True
        except Exception as e:
            self.msg += '\n'+str(e) 
    
    # Close the dbconnection
    def close(self):
        self.db.close()







