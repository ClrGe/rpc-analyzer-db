import sqlite3
import stations_pb2

class Station(object):
    def run_query(self, sql):
        conn = sqlite3.connect('data/DataAnalyzer.db')
        curs = conn.cursor()
        curs.execute(sql)
        return curs
    def select(self, readRequestPB):
        connection = sqlite3.connect('data/DataAnalyzer.db')
        cur = connection.cursor()
        sql = "SELECT gare_alias_libelle, gare_regionsncf, adresse_cp,  departement, uic_code FROM referentiel"
        #exe = cur.execute(sql)
        exe = self.run_query(sql)
        #rslt = cur.fetchall()

        #print(exe.fetchall())

        result = []

        for cur in exe:
            response =  stations_pb2.readResponsePB()

            response.gare_alias_libelle = str(cur[1])
            response.gare_regionsncf = str(cur[2])
            # response.adresse_cp = str(cur[3])
            # response.departement = str(cur[4])
            # response.uic_code = str(cur[5])

            result.append(response)

        response_list = stations_pb2.readResponseListPB()
        response_list.station.extend(result)
        return response_list