import grpc
from concurrent import futures
import sqlite3

import stations
import stations_pb2 as stations_pb2
import stations_pb2_grpc as stations_pb2_grpc

class StationsServicer(stations_pb2_grpc.StationsServicer):


    def Read(self, request, context):
        print("Read stations service called...")
        self.station = stations.Station()
        return self.station.select(request)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    stations_pb2_grpc.add_StationsServicer_to_server(StationsServicer(), server)

    print("Stations server running on 9600...")
    server.add_insecure_port('[::]:9600')
    server.start()
    server.wait_for_termination()

serve()