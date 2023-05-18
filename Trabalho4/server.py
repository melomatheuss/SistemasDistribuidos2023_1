'''
MATHEUS MELO
NATHALIA ALMADA
'''

#rode o proto com o comando
#python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. remote_control.proto

import grpc
import remote_control_pb2
import remote_control_pb2_grpc
from concurrent import futures
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG, filename='cmds.log', filemode='w', format='%(process)d - [%(asctime)s] : %(levelname)s -> %(message)s')

class RemoteControl(remote_control_pb2_grpc.RemoteControlServicer):
    def ExecCmd(self, request, context):
        result = subprocess.run(request.cmd.split(), capture_output=True)
        resultDecoded = result.stdout.decode()
        logging.debug(f"[{request.client}] INPUT: {request.cmd}")
        logging.debug(f"[{request.client}] OUTPUT: {resultDecoded}")
        return remote_control_pb2.CmdResponse(cmd=resultDecoded, error="0")

def serve():
    logging.debug('Iniciando servidor...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    remote_control_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControl(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
