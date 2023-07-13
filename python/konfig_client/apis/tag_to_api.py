import typing_extensions

from konfig_client.apis.tags import TagValues
from konfig_client.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USERS: UsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USERS: UsersApi,
    }
)
