# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0estations.proto\" \n\rreadRequestPB\x12\x0f\n\x07zipcode\x18\x01 \x01(\t\"\x80\x01\n\x0ereadResponsePB\x12\x1a\n\x12gare_alias_libelle\x18\x01 \x01(\t\x12\x17\n\x0fgare_regionsncf\x18\x02 \x01(\t\x12\x12\n\nadresse_cp\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65partement\x18\x04 \x01(\t\x12\x10\n\x08uic_code\x18\x05 \x01(\t\"6\n\x12readResponseListPB\x12 \n\x07station\x18\x01 \x03(\x0b\x32\x0f.readResponsePB27\n\x08Stations\x12+\n\x04Read\x12\x0e.readRequestPB\x1a\x13.readResponseListPBb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stations_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _READREQUESTPB._serialized_start=18
  _READREQUESTPB._serialized_end=50
  _READRESPONSEPB._serialized_start=53
  _READRESPONSEPB._serialized_end=181
  _READRESPONSELISTPB._serialized_start=183
  _READRESPONSELISTPB._serialized_end=237
  _STATIONS._serialized_start=239
  _STATIONS._serialized_end=294
# @@protoc_insertion_point(module_scope)
