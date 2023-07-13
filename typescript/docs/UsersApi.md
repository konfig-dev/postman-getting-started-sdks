# UsersApi

All URIs are relative to *https://api.konfigthis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UsersApi.md#create) | **POST** /users | Create User
[**delete**](UsersApi.md#delete) | **DELETE** /users/{user_id} | Delete User
[**get**](UsersApi.md#get) | **GET** /users/{user_id} | Get User
[**list**](UsersApi.md#list) | **GET** /users | Get Users
[**update**](UsersApi.md#update) | **PUT** /users/{user_id} | Update User


# **create**

#### **POST** /users


### Example


```typescript
import { Konfig } from "konfig-typescript-sdk";

const konfig = new Konfig({
  // Defining the base path is optional and defaults to https://api.konfigthis.com
  // basePath: "https://api.konfigthis.com",
});

const createResponse = await konfig.users.create({
  name: "Me",
  email: "hello@world.com",
  country: "USA",
});

console.log(createResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usersCreateRequest** | **UsersCreateRequest**|  |


### Return type

**UsersCreateResponse**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |
**422** | Unprocessable Entity (WebDAV) (RFC 4918) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete**

#### **DELETE** /users/{user_id}


### Example


```typescript
import { Konfig } from "konfig-typescript-sdk";

const konfig = new Konfig({
  // Defining the base path is optional and defaults to https://api.konfigthis.com
  // basePath: "https://api.konfigthis.com",
});

const deleteResponse = await konfig.users.delete({
  userId: "userId_example",
});

console.log(deleteResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**string**] |  | defaults to undefined


### Return type

**UsersDeleteResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |
**422** | Unprocessable Entity (WebDAV) (RFC 4918) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get**

#### **GET** /users/{user_id}


### Example


```typescript
import { Konfig } from "konfig-typescript-sdk";

const konfig = new Konfig({
  // Defining the base path is optional and defaults to https://api.konfigthis.com
  // basePath: "https://api.konfigthis.com",
});

const getResponse = await konfig.users.get({
  userId: "userId_example",
});

console.log(getResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**string**] |  | defaults to undefined


### Return type

**UsersGetResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |
**422** | Unprocessable Entity (WebDAV) (RFC 4918) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list**

#### **GET** /users


### Example


```typescript
import { Konfig } from "konfig-typescript-sdk";

const konfig = new Konfig({
  // Defining the base path is optional and defaults to https://api.konfigthis.com
  // basePath: "https://api.konfigthis.com",
});

const listResponse = await konfig.users.list();

console.log(listResponse);
```


### Parameters
This endpoint does not need any parameter.


### Return type

**Array<UsersListResponseInner>**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update**

#### **PUT** /users/{user_id}


### Example


```typescript
import { Konfig } from "konfig-typescript-sdk";

const konfig = new Konfig({
  // Defining the base path is optional and defaults to https://api.konfigthis.com
  // basePath: "https://api.konfigthis.com",
});

const updateResponse = await konfig.users.update({
  userId: "userId_example",
  name: "new name",
  email: "new@email.com",
  country: "USA",
});

console.log(updateResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usersUpdateRequest** | **UsersUpdateRequest**|  |
 **userId** | [**string**] |  | defaults to undefined


### Return type

**UsersUpdateResponse**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |
**422** | Unprocessable Entity (WebDAV) (RFC 4918) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


