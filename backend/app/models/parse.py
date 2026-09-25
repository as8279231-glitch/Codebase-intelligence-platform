from pydantic import BaseModel


class ParseRequest(BaseModel):
    file_path: str


class RepositoryParseRequest(BaseModel):
    repository_path: str

