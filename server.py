import grpc
from concurrent import futures
import sqlite3

import stations
import stations_pb2 as stations_pb2
import stations_pb2_grpc as stations_pb2_grpc

class StationsServicer(stations_pb2_grpc.StationsServicer):


    def Read(self, request, context):

        conn = sqlite3.connect('data/DataAnalyzer.db')
        curs = conn.cursor()
        cp = "75007"
        connection = sqlite3.connect('data/DataAnalyzer.db')
        cur = connection.cursor()
        sql = "SELECT gare_alias_libelle, gare_regionsncf, adresse_cp,  departement, uic_code FROM referentiel WHERE adresse_cp = " + cp

        exe = curs.execute(sql)

        rslt = exe.fetchall()
        print(rslt)

        result = []

        for i in rslt:
            response = stations_pb2.readResponsePB().Value()
            response.uic_code = str(i[4])
            response.gare_alias_libelle = str(i[0])
            response.gare_alias_libelle = str(i[3])
            response.adresse_cp = str(i[2])
            response.gare_regionsncf = str(i[1])
            result.append(response)

        response_list = stations_pb2.readResponsePB()
        response_list.value.extend(result)
        print(response_list)

        return response_list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    stations_pb2_grpc.add_StationsServicer_to_server(StationsServicer(), server)

    print("Stations server running on 9600...")
    server.add_insecure_port('[::]:9600')
    server.start()
    server.wait_for_termination()

serve()