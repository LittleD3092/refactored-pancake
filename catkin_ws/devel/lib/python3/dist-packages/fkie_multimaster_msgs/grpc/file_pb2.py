# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fkie_multimaster_msgs/grpc/file.proto

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
  name='fkie_multimaster_msgs/grpc/file.proto',
  package='fkie_multimaster_msgs.file',
  syntax='proto3',
  serialized_pb=_b('\n%fkie_multimaster_msgs/grpc/file.proto\x12\x1a\x66kie_multimaster_msgs.file\"\x07\n\x05\x45mpty\"%\n\x15GetFileContentRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x84\x01\n\x13GetFileContentReply\x12\x38\n\x06status\x18\x01 \x01(\x0b\x32(.fkie_multimaster_msgs.file.ReturnStatus\x12\x33\n\x04\x66ile\x18\x02 \x01(\x0b\x32%.fkie_multimaster_msgs.file.FileChunk\")\n\rRenameRequest\x12\x0b\n\x03old\x18\x01 \x01(\t\x12\x0b\n\x03new\x18\x02 \x01(\t\"`\n\x16SaveFileContentRequest\x12\x11\n\toverwrite\x18\x01 \x01(\x08\x12\x33\n\x04\x66ile\x18\x02 \x01(\x0b\x32%.fkie_multimaster_msgs.file.FileChunk\"\x87\x01\n\x14SaveFileContentReply\x12\x38\n\x06status\x18\x01 \x01(\x0b\x32(.fkie_multimaster_msgs.file.ReturnStatus\x12\x35\n\x03\x61\x63k\x18\x02 \x01(\x0b\x32(.fkie_multimaster_msgs.file.FileChunkAck\"=\n\rCopyToRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x11\n\toverwrite\x18\x03 \x01(\x08\"e\n\tFileChunk\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\x01\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0e\n\x06offset\x18\x04 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12\x0f\n\x07package\x18\x06 \x01(\t\"9\n\x0c\x46ileChunkAck\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\x01\x12\x0c\n\x04size\x18\x04 \x01(\x04\"\x1f\n\x0fListPathRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x8b\x01\n\rListPathReply\x12\x38\n\x06status\x18\x01 \x01(\x0b\x32(.fkie_multimaster_msgs.file.ReturnStatus\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x32\n\x05items\x18\x03 \x03(\x0b\x32#.fkie_multimaster_msgs.file.PathObj\">\n\x08PathList\x12\x32\n\x05items\x18\x01 \x03(\x0b\x32#.fkie_multimaster_msgs.file.PathObj\"\xa9\x01\n\x07PathObj\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\x01\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12:\n\x04type\x18\x04 \x01(\x0e\x32,.fkie_multimaster_msgs.file.PathObj.PathType\"7\n\x08PathType\x12\x08\n\x04\x46ILE\x10\x00\x12\x07\n\x03\x44IR\x10\x01\x12\x0b\n\x07SYMLINK\x10\x02\x12\x0b\n\x07PACKAGE\x10\x03\"\xb8\x01\n\x0cReturnStatus\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x11\n\terror_msg\x18\x03 \x01(\t\x12\x12\n\nerror_file\x18\x04 \x01(\t\"_\n\nStatusType\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0c\n\x08IO_ERROR\x10\x02\x12\x0c\n\x08OS_ERROR\x10\x03\x12\x10\n\x0c\x43HANGED_FILE\x10\x04\x12\x10\n\x0cREMOVED_FILE\x10\x05\".\n\x13ListPackagesRequest\x12\x17\n\x0f\x63lear_ros_cache\x18\x01 \x01(\x08\"\x84\x01\n\x11ListPackagesReply\x12\x38\n\x06status\x18\x01 \x01(\x0b\x32(.fkie_multimaster_msgs.file.ReturnStatus\x12\x35\n\x05items\x18\x02 \x03(\x0b\x32&.fkie_multimaster_msgs.file.PackageObj\"(\n\nPackageObj\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t2\x87\x08\n\x0b\x46ileService\x12v\n\x0eGetFileContent\x12\x31.fkie_multimaster_msgs.file.GetFileContentRequest\x1a/.fkie_multimaster_msgs.file.GetFileContentReply0\x01\x12{\n\x0fSaveFileContent\x12\x32.fkie_multimaster_msgs.file.SaveFileContentRequest\x1a\x30.fkie_multimaster_msgs.file.SaveFileContentReply(\x01\x30\x01\x12\x61\n\nCopyFileTo\x12).fkie_multimaster_msgs.file.CopyToRequest\x1a(.fkie_multimaster_msgs.file.ReturnStatus\x12]\n\x06Rename\x12).fkie_multimaster_msgs.file.RenameRequest\x1a(.fkie_multimaster_msgs.file.ReturnStatus\x12\x62\n\x08ListPath\x12+.fkie_multimaster_msgs.file.ListPathRequest\x1a).fkie_multimaster_msgs.file.ListPathReply\x12n\n\x0cListPackages\x12/.fkie_multimaster_msgs.file.ListPackagesRequest\x1a-.fkie_multimaster_msgs.file.ListPackagesReply\x12Z\n\x0c\x43hangedFiles\x12$.fkie_multimaster_msgs.file.PathList\x1a$.fkie_multimaster_msgs.file.PathList\x12\x62\n\x12GetPackageBinaries\x12&.fkie_multimaster_msgs.file.PackageObj\x1a$.fkie_multimaster_msgs.file.PathList\x12W\n\x06\x44\x65lete\x12#.fkie_multimaster_msgs.file.PathObj\x1a(.fkie_multimaster_msgs.file.ReturnStatus\x12T\n\x03New\x12#.fkie_multimaster_msgs.file.PathObj\x1a(.fkie_multimaster_msgs.file.ReturnStatusb\x06proto3')
)



_PATHOBJ_PATHTYPE = _descriptor.EnumDescriptor(
  name='PathType',
  full_name='fkie_multimaster_msgs.file.PathObj.PathType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYMLINK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1110,
  serialized_end=1165,
)
_sym_db.RegisterEnumDescriptor(_PATHOBJ_PATHTYPE)

_RETURNSTATUS_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='fkie_multimaster_msgs.file.ReturnStatus.StatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IO_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OS_ERROR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGED_FILE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVED_FILE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1257,
  serialized_end=1352,
)
_sym_db.RegisterEnumDescriptor(_RETURNSTATUS_STATUSTYPE)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='fkie_multimaster_msgs.file.Empty',
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
  serialized_start=69,
  serialized_end=76,
)


_GETFILECONTENTREQUEST = _descriptor.Descriptor(
  name='GetFileContentRequest',
  full_name='fkie_multimaster_msgs.file.GetFileContentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.GetFileContentRequest.path', index=0,
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
  serialized_start=78,
  serialized_end=115,
)


_GETFILECONTENTREPLY = _descriptor.Descriptor(
  name='GetFileContentReply',
  full_name='fkie_multimaster_msgs.file.GetFileContentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fkie_multimaster_msgs.file.GetFileContentReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='fkie_multimaster_msgs.file.GetFileContentReply.file', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=118,
  serialized_end=250,
)


_RENAMEREQUEST = _descriptor.Descriptor(
  name='RenameRequest',
  full_name='fkie_multimaster_msgs.file.RenameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='old', full_name='fkie_multimaster_msgs.file.RenameRequest.old', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new', full_name='fkie_multimaster_msgs.file.RenameRequest.new', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=252,
  serialized_end=293,
)


_SAVEFILECONTENTREQUEST = _descriptor.Descriptor(
  name='SaveFileContentRequest',
  full_name='fkie_multimaster_msgs.file.SaveFileContentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overwrite', full_name='fkie_multimaster_msgs.file.SaveFileContentRequest.overwrite', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='fkie_multimaster_msgs.file.SaveFileContentRequest.file', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=295,
  serialized_end=391,
)


_SAVEFILECONTENTREPLY = _descriptor.Descriptor(
  name='SaveFileContentReply',
  full_name='fkie_multimaster_msgs.file.SaveFileContentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fkie_multimaster_msgs.file.SaveFileContentReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ack', full_name='fkie_multimaster_msgs.file.SaveFileContentReply.ack', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=394,
  serialized_end=529,
)


_COPYTOREQUEST = _descriptor.Descriptor(
  name='CopyToRequest',
  full_name='fkie_multimaster_msgs.file.CopyToRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.CopyToRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='fkie_multimaster_msgs.file.CopyToRequest.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overwrite', full_name='fkie_multimaster_msgs.file.CopyToRequest.overwrite', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=531,
  serialized_end=592,
)


_FILECHUNK = _descriptor.Descriptor(
  name='FileChunk',
  full_name='fkie_multimaster_msgs.file.FileChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.FileChunk.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='fkie_multimaster_msgs.file.FileChunk.mtime', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='fkie_multimaster_msgs.file.FileChunk.size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='fkie_multimaster_msgs.file.FileChunk.offset', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='fkie_multimaster_msgs.file.FileChunk.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package', full_name='fkie_multimaster_msgs.file.FileChunk.package', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=594,
  serialized_end=695,
)


_FILECHUNKACK = _descriptor.Descriptor(
  name='FileChunkAck',
  full_name='fkie_multimaster_msgs.file.FileChunkAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.FileChunkAck.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='fkie_multimaster_msgs.file.FileChunkAck.mtime', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='fkie_multimaster_msgs.file.FileChunkAck.size', index=2,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=697,
  serialized_end=754,
)


_LISTPATHREQUEST = _descriptor.Descriptor(
  name='ListPathRequest',
  full_name='fkie_multimaster_msgs.file.ListPathRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.ListPathRequest.path', index=0,
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
  serialized_start=756,
  serialized_end=787,
)


_LISTPATHREPLY = _descriptor.Descriptor(
  name='ListPathReply',
  full_name='fkie_multimaster_msgs.file.ListPathReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fkie_multimaster_msgs.file.ListPathReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.ListPathReply.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='fkie_multimaster_msgs.file.ListPathReply.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=790,
  serialized_end=929,
)


_PATHLIST = _descriptor.Descriptor(
  name='PathList',
  full_name='fkie_multimaster_msgs.file.PathList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='fkie_multimaster_msgs.file.PathList.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=931,
  serialized_end=993,
)


_PATHOBJ = _descriptor.Descriptor(
  name='PathObj',
  full_name='fkie_multimaster_msgs.file.PathObj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.PathObj.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='fkie_multimaster_msgs.file.PathObj.mtime', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='fkie_multimaster_msgs.file.PathObj.size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='fkie_multimaster_msgs.file.PathObj.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PATHOBJ_PATHTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=996,
  serialized_end=1165,
)


_RETURNSTATUS = _descriptor.Descriptor(
  name='ReturnStatus',
  full_name='fkie_multimaster_msgs.file.ReturnStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='fkie_multimaster_msgs.file.ReturnStatus.code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fkie_multimaster_msgs.file.ReturnStatus.error_code', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='fkie_multimaster_msgs.file.ReturnStatus.error_msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_file', full_name='fkie_multimaster_msgs.file.ReturnStatus.error_file', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RETURNSTATUS_STATUSTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1168,
  serialized_end=1352,
)


_LISTPACKAGESREQUEST = _descriptor.Descriptor(
  name='ListPackagesRequest',
  full_name='fkie_multimaster_msgs.file.ListPackagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clear_ros_cache', full_name='fkie_multimaster_msgs.file.ListPackagesRequest.clear_ros_cache', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1354,
  serialized_end=1400,
)


_LISTPACKAGESREPLY = _descriptor.Descriptor(
  name='ListPackagesReply',
  full_name='fkie_multimaster_msgs.file.ListPackagesReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fkie_multimaster_msgs.file.ListPackagesReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='fkie_multimaster_msgs.file.ListPackagesReply.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1403,
  serialized_end=1535,
)


_PACKAGEOBJ = _descriptor.Descriptor(
  name='PackageObj',
  full_name='fkie_multimaster_msgs.file.PackageObj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fkie_multimaster_msgs.file.PackageObj.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='fkie_multimaster_msgs.file.PackageObj.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1537,
  serialized_end=1577,
)

_GETFILECONTENTREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_GETFILECONTENTREPLY.fields_by_name['file'].message_type = _FILECHUNK
_SAVEFILECONTENTREQUEST.fields_by_name['file'].message_type = _FILECHUNK
_SAVEFILECONTENTREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_SAVEFILECONTENTREPLY.fields_by_name['ack'].message_type = _FILECHUNKACK
_LISTPATHREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_LISTPATHREPLY.fields_by_name['items'].message_type = _PATHOBJ
_PATHLIST.fields_by_name['items'].message_type = _PATHOBJ
_PATHOBJ.fields_by_name['type'].enum_type = _PATHOBJ_PATHTYPE
_PATHOBJ_PATHTYPE.containing_type = _PATHOBJ
_RETURNSTATUS_STATUSTYPE.containing_type = _RETURNSTATUS
_LISTPACKAGESREPLY.fields_by_name['status'].message_type = _RETURNSTATUS
_LISTPACKAGESREPLY.fields_by_name['items'].message_type = _PACKAGEOBJ
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['GetFileContentRequest'] = _GETFILECONTENTREQUEST
DESCRIPTOR.message_types_by_name['GetFileContentReply'] = _GETFILECONTENTREPLY
DESCRIPTOR.message_types_by_name['RenameRequest'] = _RENAMEREQUEST
DESCRIPTOR.message_types_by_name['SaveFileContentRequest'] = _SAVEFILECONTENTREQUEST
DESCRIPTOR.message_types_by_name['SaveFileContentReply'] = _SAVEFILECONTENTREPLY
DESCRIPTOR.message_types_by_name['CopyToRequest'] = _COPYTOREQUEST
DESCRIPTOR.message_types_by_name['FileChunk'] = _FILECHUNK
DESCRIPTOR.message_types_by_name['FileChunkAck'] = _FILECHUNKACK
DESCRIPTOR.message_types_by_name['ListPathRequest'] = _LISTPATHREQUEST
DESCRIPTOR.message_types_by_name['ListPathReply'] = _LISTPATHREPLY
DESCRIPTOR.message_types_by_name['PathList'] = _PATHLIST
DESCRIPTOR.message_types_by_name['PathObj'] = _PATHOBJ
DESCRIPTOR.message_types_by_name['ReturnStatus'] = _RETURNSTATUS
DESCRIPTOR.message_types_by_name['ListPackagesRequest'] = _LISTPACKAGESREQUEST
DESCRIPTOR.message_types_by_name['ListPackagesReply'] = _LISTPACKAGESREPLY
DESCRIPTOR.message_types_by_name['PackageObj'] = _PACKAGEOBJ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.Empty)
  ))
_sym_db.RegisterMessage(Empty)

GetFileContentRequest = _reflection.GeneratedProtocolMessageType('GetFileContentRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFILECONTENTREQUEST,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.GetFileContentRequest)
  ))
_sym_db.RegisterMessage(GetFileContentRequest)

GetFileContentReply = _reflection.GeneratedProtocolMessageType('GetFileContentReply', (_message.Message,), dict(
  DESCRIPTOR = _GETFILECONTENTREPLY,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.GetFileContentReply)
  ))
_sym_db.RegisterMessage(GetFileContentReply)

RenameRequest = _reflection.GeneratedProtocolMessageType('RenameRequest', (_message.Message,), dict(
  DESCRIPTOR = _RENAMEREQUEST,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.RenameRequest)
  ))
_sym_db.RegisterMessage(RenameRequest)

SaveFileContentRequest = _reflection.GeneratedProtocolMessageType('SaveFileContentRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAVEFILECONTENTREQUEST,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.SaveFileContentRequest)
  ))
_sym_db.RegisterMessage(SaveFileContentRequest)

SaveFileContentReply = _reflection.GeneratedProtocolMessageType('SaveFileContentReply', (_message.Message,), dict(
  DESCRIPTOR = _SAVEFILECONTENTREPLY,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.SaveFileContentReply)
  ))
_sym_db.RegisterMessage(SaveFileContentReply)

CopyToRequest = _reflection.GeneratedProtocolMessageType('CopyToRequest', (_message.Message,), dict(
  DESCRIPTOR = _COPYTOREQUEST,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.CopyToRequest)
  ))
_sym_db.RegisterMessage(CopyToRequest)

FileChunk = _reflection.GeneratedProtocolMessageType('FileChunk', (_message.Message,), dict(
  DESCRIPTOR = _FILECHUNK,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.FileChunk)
  ))
_sym_db.RegisterMessage(FileChunk)

FileChunkAck = _reflection.GeneratedProtocolMessageType('FileChunkAck', (_message.Message,), dict(
  DESCRIPTOR = _FILECHUNKACK,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.FileChunkAck)
  ))
_sym_db.RegisterMessage(FileChunkAck)

ListPathRequest = _reflection.GeneratedProtocolMessageType('ListPathRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPATHREQUEST,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.ListPathRequest)
  ))
_sym_db.RegisterMessage(ListPathRequest)

ListPathReply = _reflection.GeneratedProtocolMessageType('ListPathReply', (_message.Message,), dict(
  DESCRIPTOR = _LISTPATHREPLY,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.ListPathReply)
  ))
_sym_db.RegisterMessage(ListPathReply)

PathList = _reflection.GeneratedProtocolMessageType('PathList', (_message.Message,), dict(
  DESCRIPTOR = _PATHLIST,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.PathList)
  ))
_sym_db.RegisterMessage(PathList)

PathObj = _reflection.GeneratedProtocolMessageType('PathObj', (_message.Message,), dict(
  DESCRIPTOR = _PATHOBJ,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.PathObj)
  ))
_sym_db.RegisterMessage(PathObj)

ReturnStatus = _reflection.GeneratedProtocolMessageType('ReturnStatus', (_message.Message,), dict(
  DESCRIPTOR = _RETURNSTATUS,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.ReturnStatus)
  ))
_sym_db.RegisterMessage(ReturnStatus)

ListPackagesRequest = _reflection.GeneratedProtocolMessageType('ListPackagesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKAGESREQUEST,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.ListPackagesRequest)
  ))
_sym_db.RegisterMessage(ListPackagesRequest)

ListPackagesReply = _reflection.GeneratedProtocolMessageType('ListPackagesReply', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKAGESREPLY,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.ListPackagesReply)
  ))
_sym_db.RegisterMessage(ListPackagesReply)

PackageObj = _reflection.GeneratedProtocolMessageType('PackageObj', (_message.Message,), dict(
  DESCRIPTOR = _PACKAGEOBJ,
  __module__ = 'fkie_multimaster_msgs.grpc.file_pb2'
  # @@protoc_insertion_point(class_scope:fkie_multimaster_msgs.file.PackageObj)
  ))
_sym_db.RegisterMessage(PackageObj)



_FILESERVICE = _descriptor.ServiceDescriptor(
  name='FileService',
  full_name='fkie_multimaster_msgs.file.FileService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1580,
  serialized_end=2611,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFileContent',
    full_name='fkie_multimaster_msgs.file.FileService.GetFileContent',
    index=0,
    containing_service=None,
    input_type=_GETFILECONTENTREQUEST,
    output_type=_GETFILECONTENTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SaveFileContent',
    full_name='fkie_multimaster_msgs.file.FileService.SaveFileContent',
    index=1,
    containing_service=None,
    input_type=_SAVEFILECONTENTREQUEST,
    output_type=_SAVEFILECONTENTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CopyFileTo',
    full_name='fkie_multimaster_msgs.file.FileService.CopyFileTo',
    index=2,
    containing_service=None,
    input_type=_COPYTOREQUEST,
    output_type=_RETURNSTATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Rename',
    full_name='fkie_multimaster_msgs.file.FileService.Rename',
    index=3,
    containing_service=None,
    input_type=_RENAMEREQUEST,
    output_type=_RETURNSTATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPath',
    full_name='fkie_multimaster_msgs.file.FileService.ListPath',
    index=4,
    containing_service=None,
    input_type=_LISTPATHREQUEST,
    output_type=_LISTPATHREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPackages',
    full_name='fkie_multimaster_msgs.file.FileService.ListPackages',
    index=5,
    containing_service=None,
    input_type=_LISTPACKAGESREQUEST,
    output_type=_LISTPACKAGESREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ChangedFiles',
    full_name='fkie_multimaster_msgs.file.FileService.ChangedFiles',
    index=6,
    containing_service=None,
    input_type=_PATHLIST,
    output_type=_PATHLIST,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPackageBinaries',
    full_name='fkie_multimaster_msgs.file.FileService.GetPackageBinaries',
    index=7,
    containing_service=None,
    input_type=_PACKAGEOBJ,
    output_type=_PATHLIST,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='fkie_multimaster_msgs.file.FileService.Delete',
    index=8,
    containing_service=None,
    input_type=_PATHOBJ,
    output_type=_RETURNSTATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='New',
    full_name='fkie_multimaster_msgs.file.FileService.New',
    index=9,
    containing_service=None,
    input_type=_PATHOBJ,
    output_type=_RETURNSTATUS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['FileService'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)
