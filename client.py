from __future__ import print_function

import time
import grpc

import stations_pb2, stations_pb2_grpc

class StationClient(object):
    def __init__(self):
        pass
    def get_station(self, stub):
        read_request = stations_pb2.StationsRequest()
        read_request.zipcode = "76000"
        return stub.Read(read_request)

def run():
    channel = grpc.insecure_channel('localhost:40084')
    stub = stations_pb2_grpc.StationsStub(channel)
    print(stub)

if __name__ == '__main__':
    run()