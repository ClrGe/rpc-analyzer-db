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
        for i in rslt:
            response =  stations_pb2.readResponsePB().Value()
            response.gare_alias_libelle = str(i[1])
                #response.gare_regionsncf = str(i[2])
                #response.adresse_cp = str(i[3])
                #response.departement = str(i[4])
                #response.uic_code = str(i[5])

            result.append(response)
            

        response_list = stations_pb2.readResponsePB()
        response_list.value.extend(result)
        return response_list