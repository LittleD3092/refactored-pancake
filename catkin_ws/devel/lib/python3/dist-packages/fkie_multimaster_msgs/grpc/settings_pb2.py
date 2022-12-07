# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fkie_multimaster_msgs/grpc/settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fkie_multimaster_msgs/grpc/settings.proto',
  package='fkie_multimaster_msgs.settings',
  syntax='proto3',
  serialized_pb=_b('\n)fkie_multimaster_msgs/grpc/settings.proto\x12\x1e\x66kie_multimaster_msgs.settings\"\x07\n\x05\x45mpty\"\x18\n\x06\x46ilter\x12\x0e\n\x06nslist\x18\x01 \x03(\t\"\x14\n\x04Yaml\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t2\xc6\x01\n\x0fSettingsService\x12Y\n\tGetConfig\x12&.fkie_multimaster_msgs.settings.Filter\x1a$.fkie_multimaster_msgs.settings.Yaml\x12X\n\tSetConfig\x12$.fkie_multimaster_msgs.settings.Yaml\x1a%.fkie_multimaster_msgs.settings.Emptyb\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='fkie_multimaster_msgs.settings.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=84,
)


_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='fkie_multimaster_msgs.settings.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nslist', full_name='fkie_multimaster_msgs.settings.Filter.nslist', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=110,
)


_YAML = _descriptor.Descriptor(
  name='Yaml',
  full_name='fkie_multimaster_msgs.settings.Yaml',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='fkie_multimaster_msgs.settings.Yaml.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Filter'] = _FILTER
DESCRIPTOR.message_types_by_name['Yaml'] = _YAML
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'fkie_multimaster_msgs.grpc.settings_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.settings.Empty)
  ))
_sym_db.RegisterMessage(Empty)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), dict(
  DESCRIPTOR = _FILTER,
  __module__ = 'fkie_multimaster_msgs.grpc.settings_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.settings.Filter)
  ))
_sym_db.RegisterMessage(Filter)

Yaml = _reflection.GeneratedProtocolMessageType('Yaml', (_message.Message,), dict(
  DESCRIPTOR = _YAML,
  __module__ = 'fkie_multimaster_msgs.grpc.settings_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.settings.Yaml)
  ))
_sym_db.RegisterMessage(Yaml)



_SETTINGSSERVICE = _descriptor.ServiceDescriptor(
  name='SettingsService',
  full_name='fkie_multimaster_msgs.settings.SettingsService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=135,
  serialized_end=333,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='fkie_multimaster_msgs.settings.SettingsService.GetConfig',
    index=0,
    containing_service=None,
    input_type=_FILTER,
    output_type=_YAML,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfig',
    full_name='fkie_multimaster_msgs.settings.SettingsService.SetConfig',
    index=1,
    containing_service=None,
    input_type=_YAML,
    output_type=_EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SETTINGSSERVICE)

DESCRIPTOR.services_by_name['SettingsService'] = _SETTINGSSERVICE

# @@protoc_insertion_point(module_scope)
