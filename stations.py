import sqlite3
import stations_pb2

class Station(object):

    def run_query(self, sql):
        conn = sqlite3.connect('data/DataAnalyzer.db')
        curs = conn.cursor()
        curs.execute(sql)
        return curs

    def select(self, readRequestPB):
        cp = "75007"
        connection = sqlite3.connect('data/DataAnalyzer.db')
        cur = connection.cursor()
        sql = "SELECT gare_alias_libelle, gare_regionsncf, adresse_cp,  departement, uic_code FROM referentiel WHERE adresse_cp = " + cp

        exe = self.run_query(sql)
        rslt = exe.fetchall()
        print(rslt)

        result = []
        i = 0
        response =  stations_pb2.readResponsePB().Value()
        for i in rslt:
            response = i
            print(response)
            response.station = rslt[1]
                #response.departement = str(i[4])
                #response.uic_code = str(i[5])

            result.append(rslt)
            

        response_list = stations_pb2.readResponsePB()
        response_list.value.append(rslt)
        return response_list