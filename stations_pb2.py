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


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0estations.proto\x1a\x19google/protobuf/any.proto\" \n\rreadRequestPB\x12\x0f\n\x07zipcode\x18\x01 \x01(\t\"\xab\x01\n\x0ereadResponsePB\x12$\n\x05value\x18\x01 \x03(\x0b\x32\x15.readResponsePB.Value\x1as\n\x05Value\x12\x1a\n\x12gare_alias_libelle\x18\x04 \x01(\t\x12\x10\n\x08uic_code\x18\x02 \x01(\t\x12\x12\n\nadresse_cp\x18\x05 \x01(\t\x12\x17\n\x0fgare_regionsncf\x18\x17 \x01(\t\x12\x0f\n\x07ui_code\x18\x06 \x01(\t\"6\n\x12readResponseListPB\x12 \n\x07station\x18\x01 \x03(\x0b\x32\x0f.readResponsePB24\n\x08Stations\x12(\n\x04Read\x12\x0f.readResponsePB\x1a\x0f.readResponsePBb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stations_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _READREQUESTPB._serialized_start=45
  _READREQUESTPB._serialized_end=77
  _READRESPONSEPB._serialized_start=80
  _READRESPONSEPB._serialized_end=251
  _READRESPONSEPB_VALUE._serialized_start=136
  _READRESPONSEPB_VALUE._serialized_end=251
  _READRESPONSELISTPB._serialized_start=253
  _READRESPONSELISTPB._serialized_end=307
  _STATIONS._serialized_start=309
  _STATIONS._serialized_end=361
# @@protoc_insertion_point(module_scope)
