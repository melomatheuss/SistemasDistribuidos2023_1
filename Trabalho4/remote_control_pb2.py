# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_control.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14remote_control.proto\x12\x0eremote_control\"9\n\nCmdRequest\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\x0e\n\x06\x63lient\x18\x02 \x01(\t\x12\x0e\n\x06passwd\x18\x03 \x01(\t\")\n\x0b\x43mdResponse\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t2S\n\rRemoteControl\x12\x42\n\x07\x45xecCmd\x12\x1a.remote_control.CmdRequest\x1a\x1b.remote_control.CmdResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'remote_control_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CMDREQUEST._serialized_start=40
  _CMDREQUEST._serialized_end=97
  _CMDRESPONSE._serialized_start=99
  _CMDRESPONSE._serialized_end=140
  _REMOTECONTROL._serialized_start=142
  _REMOTECONTROL._serialized_end=225
# @@protoc_insertion_point(module_scope)