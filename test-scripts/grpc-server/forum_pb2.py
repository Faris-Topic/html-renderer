# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forum.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x66orum.proto\x12\x1d\x65xample.forum_rendering.proto\" \n\x0cHTMLResponse\x12\x10\n\x08htmlFile\x18\x01 \x01(\x0c\"0\n\x11\x43reatePostRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\"\x1c\n\x0eGetPostRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x0e\n\x0c\x45mptyRequest2\xc3\x03\n\rForumRenderer\x12i\n\x0bGetHomePage\x12+.example.forum_rendering.proto.EmptyRequest\x1a+.example.forum_rendering.proto.HTMLResponse\"\x00\x12l\n\x0eGetNewPostPage\x12+.example.forum_rendering.proto.EmptyRequest\x1a+.example.forum_rendering.proto.HTMLResponse\"\x00\x12p\n\rCreateNewPost\x12\x30.example.forum_rendering.proto.CreatePostRequest\x1a+.example.forum_rendering.proto.HTMLResponse\"\x00\x12g\n\x07GetPost\x12-.example.forum_rendering.proto.GetPostRequest\x1a+.example.forum_rendering.proto.HTMLResponse\"\x00\x42\x31Z/github.com/Faris-Topic/html-renderer/grpc/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'forum_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/Faris-Topic/html-renderer/grpc/proto'
  _globals['_HTMLRESPONSE']._serialized_start=46
  _globals['_HTMLRESPONSE']._serialized_end=78
  _globals['_CREATEPOSTREQUEST']._serialized_start=80
  _globals['_CREATEPOSTREQUEST']._serialized_end=128
  _globals['_GETPOSTREQUEST']._serialized_start=130
  _globals['_GETPOSTREQUEST']._serialized_end=158
  _globals['_EMPTYREQUEST']._serialized_start=160
  _globals['_EMPTYREQUEST']._serialized_end=174
  _globals['_FORUMRENDERER']._serialized_start=177
  _globals['_FORUMRENDERER']._serialized_end=628
# @@protoc_insertion_point(module_scope)
