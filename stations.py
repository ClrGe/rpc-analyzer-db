import sqlite3
import stations_pb2

class StationORM(object):
    def __init__(self):
        pass


    def search(self):

        connection = sqlite3.connect('data/DataAnalyzer.db')
        cur = connection.cursor()

        args = request.args
        regionquery = args.get("region")
        cp = args.get("zipcode")

        if not regionquery:
            query = "SELECT [fields.gare_alias_libelle_noncontraint], [fields.gare_regionsncf_libelle], [fields.adresse_cp],  [fields.departement_libellemin], [fields.uic_code] FROM referentiel WHERE [fields.adresse_cp] = "+cp
            cur.execute(query)
        if not cp:
            region = regionquery.upper()
            query = "SELECT [fields.gare_alias_libelle_noncontraint], [fields.gare_regionsncf_libelle], [fields.adresse_cp],  [fields.departement_libellemin], [fields.uic_code] FROM referentiel WHERE [fields.gare_regionsncf_libelle] = '"+region+"'"
            cur.execute(query)


        query = base_query + where_clause
        query_result = self.search(query)
        result = []
        for cur in query_result:
            response = stations_pb2.StationsResponse()
            response.gare_alias_libelle_noncontraint = str(cur[1])
            response.commune_libellemin = str(cur[2])
            response.uic_code = str(cur[3])
            response.adresse_cp = str(cur[4])
            response.departement_libellemin = str(cur[5])
            response.gare_regionsncf_libelle = str(cur[6])
            result.append(response)

        response_list = stations_pb2.responseListPB()
        response_list.station.extend(result)
        return response_list
