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

# Configuração do registro de log
logging.basicConfig(level=logging.DEBUG, filename='cmds.log', filemode='w', format='%(process)d - [%(asctime)s] : %(levelname)s -> %(message)s')

class RemoteControl(remote_control_pb2_grpc.RemoteControlServicer):  # Classe RemoteControl para implementar o serviço gRPC

    def ExecCmd(self, request, context):
        # Executa o comando recebido como uma subprocesso e captura a saída
        result = subprocess.run(request.cmd.split(), capture_output=True)
        resultDecoded = result.stdout.decode()
        
        logging.debug(f"[{request.client}] INPUT: {request.cmd}")         # Registra o comando de entrada e sua saída no log
        logging.debug(f"[{request.client}] OUTPUT: {resultDecoded}")
        
        # Retorna a resposta do comando ao cliente
        return remote_control_pb2.CmdResponse(cmd=resultDecoded, error="0")

# Função para iniciar o servidor gRPC
def serve():
    logging.debug('Iniciando servidor...')
    
    # Cria um servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Registra a implementação do serviço RemoteControl no servidor
    remote_control_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControl(), server)
    
    # Adiciona uma porta de escuta ao servidor
    server.add_insecure_port("[::]:50051")
    
    # Inicia o servidor gRPC
    server.start()
    
    # Aguarda a finalização do servidor
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

