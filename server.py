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

        cur.execute("SELECT gare_alias_libelle, gare_regionsncf, adresse_cp,  departement, uic_code FROM referentiel WHERE adresse_cp='76000'")

        i = 0

        while True:
            i += 1
            rslt = cur.fetchall()
        print(rslt)
        return stations_pb2.StationResponse(rslt)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

stations_pb2_grpc.add_StationsServicer_to_server(StationsServicer(), server)

print("Stations server running on 9200...")
server.add_insecure_port('[::]:9200')
server.start()
server.wait_for_termination()