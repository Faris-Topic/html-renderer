from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HTMLResponse(_message.Message):
    __slots__ = ["htmlFile"]
    HTMLFILE_FIELD_NUMBER: _ClassVar[int]
    htmlFile: bytes
    def __init__(self, htmlFile: _Optional[bytes] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ["title", "body"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
