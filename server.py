# This script creates a gRPC server that serves train station data by reading data from a sqlite3 database
import grpc
from concurrent import futures
import sqlite3
from dotenv import load_dotenv
# import files generated from the proto definition
import stations_pb2 as stations_pb2
import stations_pb2_grpc as stations_pb2_grpc

load_dotenv()

PORT = os.getenv('PORT')
DB = os.getenv('DB')

# Connect to the SQLite3 database
def connectDB():
    connection = sqlite3.connect(DB)
    return connection

# StationsServicer class is implemented to handle the gRPC requests
class StationsServicer(stations_pb2_grpc.StationsServicer):
    # Read function is implemented to read the data from the sqlite3 database based on the zipcode passed in the request
    def Read(self, readRequestPB, context):
        connectDB()
        
        cp = readRequestPB.zipcode
        cur = connection.cursor()
        
        # sql query to fetch the data based on the zipcode
        sql = "SELECT gare_alias_libelle, gare_regionsncf, adresse_cp,  departement, uic_code FROM referentiel WHERE adresse_cp = " + cp
        exe = cur.execute(sql)
        rslt = exe.fetchall()
        
        # list to hold the data to be returned as the response
        result = []

        for i in rslt:
            response = stations_pb2.readResponsePB().Value()
            response.uic_code = str(i[4])
            response.gare_alias_libelle = str(i[0])
            response.adresse_cp = str(i[2])
            response.gare_regionsncf = str(i[1])
            result.append(response)

        response_list = stations_pb2.readResponsePB()
        response_list.value.extend(result)
        print(response_list)

        return response_list
    
# serve function starts the gRPC server and listens on port 9600
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stations_pb2_grpc.add_StationsServicer_to_server(StationsServicer(), server)
    
    print("Stations server running on 9600...")
    server.add_insecure_port('[::]:9600')
    
    server.start()
    server.wait_for_termination()

serve()