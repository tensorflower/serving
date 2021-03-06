# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import dynamic_reload_config_pb2 as dynamic__reload__config__pb2
import model_server_config_pb2 as model__server__config__pb2


class PredictionServiceStub(object):
  """open source marker; do not remove

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DynamicReload = channel.unary_unary(
        '/tensorflow.serving.PredictionService/DynamicReload',
        request_serializer=model__server__config__pb2.ModelServerConfig.SerializeToString,
        response_deserializer=dynamic__reload__config__pb2.ReloadResponse.FromString,
        )


class PredictionServiceServicer(object):
  """open source marker; do not remove

  """

  def DynamicReload(self, request, context):
    """DynamicReload  --Dynamically reloads modesl from config.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DynamicReload': grpc.unary_unary_rpc_method_handler(
          servicer.DynamicReload,
          request_deserializer=model__server__config__pb2.ModelServerConfig.FromString,
          response_serializer=dynamic__reload__config__pb2.ReloadResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensorflow.serving.PredictionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
