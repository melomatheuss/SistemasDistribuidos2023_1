'''
MATHEUS MELO 
NATHALIA ALMADA
'''
#rode o proto com o comando
#python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. remote_control.proto

import grpc
import remote_control_pb2
import remote_control_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        while True:
            cmd = input('Digite um comando para enviar ao servidor:\n')  #Solicita ao usuário que digite um comando

            # Cria um stub para o serviço RemoteControl
            stub = remote_control_pb2_grpc.RemoteControlStub(channel)
            response = stub.ExecCmd(remote_control_pb2.CmdRequest(cmd=cmd))  # Chama o método ExecCmd, passando a solicitação contendo o comando

           # Imprime a saída do comando retornado pelo servidor
            print(f'[localhost:50051] OUTPUT:\n{response.cmd}')

if __name__ == "__main__":
    run()
