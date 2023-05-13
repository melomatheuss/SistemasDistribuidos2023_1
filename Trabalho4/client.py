#rode o proto com o comando
#python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. linux_machine.proto

import grpc
import linux_machine_pb2
import linux_machine_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = linux_machine_pb2_grpc.LinuxMachineStub(channel)
        command = input("Digite o comando a ser executado: ")
        response = stub.Execute(linux_machine_pb2.CommandRequest(command=command))
        print(response.output)

if __name__ == "__main__":
    run()
