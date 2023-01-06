import grpc
from concurrent import futures
import time
from datetime import date
import sqlite3
import logging

import stations_pb2 as stations_pb2
import stations_pb2_grpc as stations_pb2_grpc
import stations

today = date.today()
d1 = today.strftime("%d%m%Y")
logging.basicConfig(filename='./data/logs_'+d1+'.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s : %(message)s')

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class StationsServicer(stations_pb2_grpc.StationsServicer):
    def __init__(self):
        self.__emp_orm = stations.StationORM()
    def Read(self, request, context):
        print("Read stations service called...")
        return self.__emp_orm.select(request)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stations_pb2_grpc.add_StationsServicer_to_server(StationsServicer(), server)
    server.add_insecure_port('[::]:9200')
    server.start()
    print("Stations server running on 9200...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except:
        server.stop(0)


if __name__ == '__main__':
    serve()