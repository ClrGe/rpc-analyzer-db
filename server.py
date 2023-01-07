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

        sql = "SELECT gare_alias_libelle, gare_regionsncf, adresse_cp,  departement, uic_code FROM referentiel WHERE adresse_cp='76000'"
        exe = cur.execute(sql)

        rslt = cur.fetchall()
        result = stations_pb2.StationsResponse(exe)
        toto = "toto"
        return toto

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

stations_pb2_grpc.add_StationsServicer_to_server(StationsServicer(), server)

print("Stations server running on 9200...")
server.add_insecure_port('[::]:9200')
server.start()
server.wait_for_termination()