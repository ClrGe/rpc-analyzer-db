import grpc
from concurrent import futures
import time
from datetime import date
import sqlite3

import stations_pb2 as stations_pb2
import stations_pb2_grpc as stations_pb2_grpc

class StationsServicer(stations_pb2_grpc.StationsServicer):

    def Read(self, request, context):
        connection = sqlite3.connect('data/DataAnalyzer.db')
        cur = connection.cursor()
        zipcode = "76000"
        sql = "SELECT gare_alias_libelle, gare_regionsncf, adresse_cp,  departement, uic_code FROM referentiel WHERE adresse_cp='76000'"
        exe = cur.execute(sql)

        rslt = cur.fetchall()

        result = []
        for cur in rslt:
            readResponsePB =  stations_pb2.readResponsePB(exe)

            readResponsePB.gare_alias_libelle = str(cur[1])
            readResponsePB.gare_regionsncf = str(cur[2])
            readResponsePB.adresse_cp = str(cur[3])
            readResponsePB.departement = str(cur[4])
            readResponsePB.uic_code = str(cur[5])

            result.append(readResponsePB)

        readResponseListPB = stations_pb2.readResponseListPB()
        readResponseListPB.station.extend(result)
        return readResponseListPB


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

stations_pb2_grpc.add_StationsServicer_to_server(StationsServicer(), server)

print("Stations server running on 9600...")
server.add_insecure_port('[::]:9600')
server.start()
server.wait_for_termination()