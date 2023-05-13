import grpc
import subprocess
import linux_machine_pb2
import linux_machine_pb2_grpc

class LinuxMachine(linux_machine_pb2_grpc.LinuxMachineServicer):
    def Execute(self, request, context):
        command = request.command.split()
        output = subprocess.check_output(command).decode()
        return linux_machine_pb2.CommandResponse(output=output)

def serve():
    server = grpc.server(grpc.insecure_channel("[::]:50051"))
    linux_machine_pb2_grpc.add_LinuxMachineServicer_to_server(LinuxMachine(), server)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
