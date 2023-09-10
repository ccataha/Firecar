# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from xray_api.proto.transport.internet.grpc.encoding import stream_pb2 as transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2


class GRPCServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Tun = channel.stream_stream(
                '/xray.transport.internet.grpc.encoding.GRPCService/Tun',
                request_serializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.Hunk.SerializeToString,
                response_deserializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.Hunk.FromString,
                )
        self.TunMulti = channel.stream_stream(
                '/xray.transport.internet.grpc.encoding.GRPCService/TunMulti',
                request_serializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.MultiHunk.SerializeToString,
                response_deserializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.MultiHunk.FromString,
                )


class GRPCServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Tun(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TunMulti(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRPCServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Tun': grpc.stream_stream_rpc_method_handler(
                    servicer.Tun,
                    request_deserializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.Hunk.FromString,
                    response_serializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.Hunk.SerializeToString,
            ),
            'TunMulti': grpc.stream_stream_rpc_method_handler(
                    servicer.TunMulti,
                    request_deserializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.MultiHunk.FromString,
                    response_serializer=transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.MultiHunk.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'xray.transport.internet.grpc.encoding.GRPCService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GRPCService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Tun(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/xray.transport.internet.grpc.encoding.GRPCService/Tun',
            transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.Hunk.SerializeToString,
            transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.Hunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TunMulti(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/xray.transport.internet.grpc.encoding.GRPCService/TunMulti',
            transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.MultiHunk.SerializeToString,
            transport_dot_internet_dot_grpc_dot_encoding_dot_stream__pb2.MultiHunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
