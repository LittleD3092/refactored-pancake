# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from fkie_multimaster_msgs/SyncMasterInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import fkie_multimaster_msgs.msg

class SyncMasterInfo(genpy.Message):
  _md5sum = "ba4b02792114bcc4bae507c60dd14d66"
  _type = "fkie_multimaster_msgs/SyncMasterInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string masteruri
string[] nodes
fkie_multimaster_msgs/SyncTopicInfo[] publisher
fkie_multimaster_msgs/SyncTopicInfo[] subscriber
fkie_multimaster_msgs/SyncServiceInfo[] services
================================================================================
MSG: fkie_multimaster_msgs/SyncTopicInfo
string topic
string node
string nodeuri
================================================================================
MSG: fkie_multimaster_msgs/SyncServiceInfo
string service
string serviceuri
string node
string nodeuri"""
  __slots__ = ['masteruri','nodes','publisher','subscriber','services']
  _slot_types = ['string','string[]','fkie_multimaster_msgs/SyncTopicInfo[]','fkie_multimaster_msgs/SyncTopicInfo[]','fkie_multimaster_msgs/SyncServiceInfo[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       masteruri,nodes,publisher,subscriber,services

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SyncMasterInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.masteruri is None:
        self.masteruri = ''
      if self.nodes is None:
        self.nodes = []
      if self.publisher is None:
        self.publisher = []
      if self.subscriber is None:
        self.subscriber = []
      if self.services is None:
        self.services = []
    else:
      self.masteruri = ''
      self.nodes = []
      self.publisher = []
      self.subscriber = []
      self.services = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.masteruri
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.nodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.nodes:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.publisher)
      buff.write(_struct_I.pack(length))
      for val1 in self.publisher:
        _x = val1.topic
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.nodeuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.subscriber)
      buff.write(_struct_I.pack(length))
      for val1 in self.subscriber:
        _x = val1.topic
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.nodeuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.services)
      buff.write(_struct_I.pack(length))
      for val1 in self.services:
        _x = val1.service
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.serviceuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.nodeuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.publisher is None:
        self.publisher = None
      if self.subscriber is None:
        self.subscriber = None
      if self.services is None:
        self.services = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.masteruri = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.masteruri = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.nodes = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.nodes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.publisher = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncTopicInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.topic = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.topic = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.node = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.node = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.nodeuri = str[start:end]
        self.publisher.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subscriber = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncTopicInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.topic = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.topic = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.node = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.node = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.nodeuri = str[start:end]
        self.subscriber.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.services = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncServiceInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.service = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.service = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.serviceuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.serviceuri = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.node = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.node = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.nodeuri = str[start:end]
        self.services.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.masteruri
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.nodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.nodes:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.publisher)
      buff.write(_struct_I.pack(length))
      for val1 in self.publisher:
        _x = val1.topic
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.nodeuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.subscriber)
      buff.write(_struct_I.pack(length))
      for val1 in self.subscriber:
        _x = val1.topic
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.nodeuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.services)
      buff.write(_struct_I.pack(length))
      for val1 in self.services:
        _x = val1.service
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.serviceuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.node
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.nodeuri
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.publisher is None:
        self.publisher = None
      if self.subscriber is None:
        self.subscriber = None
      if self.services is None:
        self.services = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.masteruri = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.masteruri = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.nodes = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.nodes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.publisher = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncTopicInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.topic = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.topic = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.node = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.node = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.nodeuri = str[start:end]
        self.publisher.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subscriber = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncTopicInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.topic = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.topic = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.node = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.node = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.nodeuri = str[start:end]
        self.subscriber.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.services = []
      for i in range(0, length):
        val1 = fkie_multimaster_msgs.msg.SyncServiceInfo()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.service = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.service = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.serviceuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.serviceuri = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.node = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.node = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.nodeuri = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.nodeuri = str[start:end]
        self.services.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
