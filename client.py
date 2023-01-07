from __future__ import print_function

import time
import grpc

import stations_pb2, stations_pb2_grpc

class StationClient(object):
    def __init__(self):
        pass
    def get_station(self, stub):
        read_request = stations_pb2.StationsRequest()
        return stub.Read(read_request)

def run():
    channel = grpc.insecure_channel('localhost:40084')
    stub = stations_pb2_grpc.StationsStub(channel)
    print(stub)
    response = stub.StationsResponse()
    print(reponse.value)

run()