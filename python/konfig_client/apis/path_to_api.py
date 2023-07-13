import typing_extensions

from konfig_client.paths import PathValues
from konfig_client.apis.paths.users_user_id import UsersUserId
from konfig_client.apis.paths.users import Users

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS: Users,
    }
)

path_to_api = PathToApi(
    {
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS: Users,
    }
)
