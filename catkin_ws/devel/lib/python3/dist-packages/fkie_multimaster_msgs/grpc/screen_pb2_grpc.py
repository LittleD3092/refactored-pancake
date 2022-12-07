# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from fkie_multimaster_msgs.grpc import screen_pb2 as fkie__multimaster__msgs_dot_grpc_dot_screen__pb2


class ScreenServiceStub(object):
  """* The screen manager service definition. 
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetScreens = channel.unary_unary(
        '/fkie_multimaster_msgs.screen.ScreenService/GetScreens',
        request_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screen.SerializeToString,
        response_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screens.FromString,
        )
    self.GetAllScreens = channel.unary_unary(
        '/fkie_multimaster_msgs.screen.ScreenService/GetAllScreens',
        request_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
        response_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screens.FromString,
        )
    self.GetMultipleScreens = channel.unary_unary(
        '/fkie_multimaster_msgs.screen.ScreenService/GetMultipleScreens',
        request_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
        response_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screens.FromString,
        )
    self.RosClean = channel.unary_unary(
        '/fkie_multimaster_msgs.screen.ScreenService/RosClean',
        request_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
        response_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
        )
    self.DeleteLog = channel.unary_unary(
        '/fkie_multimaster_msgs.screen.ScreenService/DeleteLog',
        request_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Nodes.SerializeToString,
        response_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
        )
    self.GetLogDiskSize = channel.unary_unary(
        '/fkie_multimaster_msgs.screen.ScreenService/GetLogDiskSize',
        request_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
        response_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.DirSize.FromString,
        )
    self.WipeScreens = channel.unary_unary(
        '/fkie_multimaster_msgs.screen.ScreenService/WipeScreens',
        request_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
        response_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
        )


class ScreenServiceServicer(object):
  """* The screen manager service definition. 
  """

  def GetScreens(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllScreens(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMultipleScreens(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RosClean(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLog(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLogDiskSize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WipeScreens(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ScreenServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetScreens': grpc.unary_unary_rpc_method_handler(
          servicer.GetScreens,
          request_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screen.FromString,
          response_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screens.SerializeToString,
      ),
      'GetAllScreens': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllScreens,
          request_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
          response_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screens.SerializeToString,
      ),
      'GetMultipleScreens': grpc.unary_unary_rpc_method_handler(
          servicer.GetMultipleScreens,
          request_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
          response_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Screens.SerializeToString,
      ),
      'RosClean': grpc.unary_unary_rpc_method_handler(
          servicer.RosClean,
          request_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
          response_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
      ),
      'DeleteLog': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLog,
          request_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Nodes.FromString,
          response_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
      ),
      'GetLogDiskSize': grpc.unary_unary_rpc_method_handler(
          servicer.GetLogDiskSize,
          request_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
          response_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.DirSize.SerializeToString,
      ),
      'WipeScreens': grpc.unary_unary_rpc_method_handler(
          servicer.WipeScreens,
          request_deserializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.FromString,
          response_serializer=fkie__multimaster__msgs_dot_grpc_dot_screen__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkie_multimaster_msgs.screen.ScreenService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
