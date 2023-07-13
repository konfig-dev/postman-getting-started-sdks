# UsersApi

All URIs are relative to *https://api.konfigthis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create**](UsersApi.md#create) | **POST** /users | Create User |
| [**delete**](UsersApi.md#delete) | **DELETE** /users/{user_id} | Delete User |
| [**get**](UsersApi.md#get) | **GET** /users/{user_id} | Get User |
| [**list**](UsersApi.md#list) | **GET** /users | Get Users |
| [**update**](UsersApi.md#update) | **PUT** /users/{user_id} | Update User |


<a name="create"></a>
# **create**
> UsersCreateResponse create(usersCreateRequest).execute();

Create User

### Example
```java
import com.konfigthis.client.ApiClient;
import com.konfigthis.client.ApiException;
import com.konfigthis.client.ApiResponse;
import com.konfigthis.client.Konfig;
import com.konfigthis.client.Configuration;
import com.konfigthis.client.auth.*;
import com.konfigthis.client.model.*;
import com.konfigthis.client.api.UsersApi;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    Configuration configuration = new Configuration();
    configuration.host = "https://api.konfigthis.com";
    

    Konfig client = new Konfig(configuration);
    String name = "name_example";
    String email = "email_example";
    String country = "country_example";
    try {
      UsersCreateResponse result = client
              .users
              .create()
              .name(name)
              .email(email)
              .country(country)
              .execute();
      System.out.println(result);

      System.out.println(result.getId());

      System.out.println(result.getMessage());

    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#create");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }

    // Use .executeWithHttpInfo() to retrieve HTTP Status Code, Headers and Request
    try {
      ApiResponse<UsersCreateResponse> response = client
              .users
              .create()
              .name(name)
              .email(email)
              .country(country)
              .executeWithHttpInfo();
      System.out.println(response.getResponseBody());
      System.out.println(response.getResponseHeaders());
      System.out.println(response.getStatusCode());
      System.out.println(response.getRoundTripTime());
      System.out.println(response.getRequest());
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#create");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **usersCreateRequest** | [**UsersCreateRequest**](UsersCreateRequest.md)|  | |

### Return type

[**UsersCreateResponse**](UsersCreateResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |

<a name="delete"></a>
# **delete**
> UsersDeleteResponse delete(userId).execute();

Delete User

### Example
```java
import com.konfigthis.client.ApiClient;
import com.konfigthis.client.ApiException;
import com.konfigthis.client.ApiResponse;
import com.konfigthis.client.Konfig;
import com.konfigthis.client.Configuration;
import com.konfigthis.client.auth.*;
import com.konfigthis.client.model.*;
import com.konfigthis.client.api.UsersApi;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    Configuration configuration = new Configuration();
    configuration.host = "https://api.konfigthis.com";
    

    Konfig client = new Konfig(configuration);
    String userId = "{{userId}}";
    try {
      UsersDeleteResponse result = client
              .users
              .delete(userId)
              .execute();
      System.out.println(result);

      System.out.println(result.getMessage());

    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#delete");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }

    // Use .executeWithHttpInfo() to retrieve HTTP Status Code, Headers and Request
    try {
      ApiResponse<UsersDeleteResponse> response = client
              .users
              .delete(userId)
              .executeWithHttpInfo();
      System.out.println(response.getResponseBody());
      System.out.println(response.getResponseHeaders());
      System.out.println(response.getStatusCode());
      System.out.println(response.getRoundTripTime());
      System.out.println(response.getRequest());
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#delete");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | **String**|  | |

### Return type

[**UsersDeleteResponse**](UsersDeleteResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |

<a name="get"></a>
# **get**
> UsersGetResponse get(userId).execute();

Get User

### Example
```java
import com.konfigthis.client.ApiClient;
import com.konfigthis.client.ApiException;
import com.konfigthis.client.ApiResponse;
import com.konfigthis.client.Konfig;
import com.konfigthis.client.Configuration;
import com.konfigthis.client.auth.*;
import com.konfigthis.client.model.*;
import com.konfigthis.client.api.UsersApi;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    Configuration configuration = new Configuration();
    configuration.host = "https://api.konfigthis.com";
    

    Konfig client = new Konfig(configuration);
    String userId = "{{userId}}";
    try {
      UsersGetResponse result = client
              .users
              .get(userId)
              .execute();
      System.out.println(result);

      System.out.println(result.getName());

      System.out.println(result.getEmail());

      System.out.println(result.getCountry());

      System.out.println(result.getId());

    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#get");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }

    // Use .executeWithHttpInfo() to retrieve HTTP Status Code, Headers and Request
    try {
      ApiResponse<UsersGetResponse> response = client
              .users
              .get(userId)
              .executeWithHttpInfo();
      System.out.println(response.getResponseBody());
      System.out.println(response.getResponseHeaders());
      System.out.println(response.getStatusCode());
      System.out.println(response.getRoundTripTime());
      System.out.println(response.getRequest());
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#get");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | **String**|  | |

### Return type

[**UsersGetResponse**](UsersGetResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |

<a name="list"></a>
# **list**
> List&lt;UsersListResponseInner&gt; list().execute();

Get Users

### Example
```java
import com.konfigthis.client.ApiClient;
import com.konfigthis.client.ApiException;
import com.konfigthis.client.ApiResponse;
import com.konfigthis.client.Konfig;
import com.konfigthis.client.Configuration;
import com.konfigthis.client.auth.*;
import com.konfigthis.client.model.*;
import com.konfigthis.client.api.UsersApi;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    Configuration configuration = new Configuration();
    configuration.host = "https://api.konfigthis.com";
    

    Konfig client = new Konfig(configuration);
    try {
      List<UsersListResponseInner> result = client
              .users
              .list()
              .execute();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#list");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }

    // Use .executeWithHttpInfo() to retrieve HTTP Status Code, Headers and Request
    try {
      ApiResponse<List<UsersListResponseInner>> response = client
              .users
              .list()
              .executeWithHttpInfo();
      System.out.println(response.getResponseBody());
      System.out.println(response.getResponseHeaders());
      System.out.println(response.getStatusCode());
      System.out.println(response.getRoundTripTime());
      System.out.println(response.getRequest());
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#list");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;UsersListResponseInner&gt;**](UsersListResponseInner.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |

<a name="update"></a>
# **update**
> UsersUpdateResponse update(userId, usersUpdateRequest).execute();

Update User

### Example
```java
import com.konfigthis.client.ApiClient;
import com.konfigthis.client.ApiException;
import com.konfigthis.client.ApiResponse;
import com.konfigthis.client.Konfig;
import com.konfigthis.client.Configuration;
import com.konfigthis.client.auth.*;
import com.konfigthis.client.model.*;
import com.konfigthis.client.api.UsersApi;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    Configuration configuration = new Configuration();
    configuration.host = "https://api.konfigthis.com";
    

    Konfig client = new Konfig(configuration);
    String userId = "{{userId}}";
    String name = "name_example";
    String email = "email_example";
    String country = "country_example";
    try {
      UsersUpdateResponse result = client
              .users
              .update(userId)
              .name(name)
              .email(email)
              .country(country)
              .execute();
      System.out.println(result);

      System.out.println(result.getMessage());

    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#update");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }

    // Use .executeWithHttpInfo() to retrieve HTTP Status Code, Headers and Request
    try {
      ApiResponse<UsersUpdateResponse> response = client
              .users
              .update(userId)
              .name(name)
              .email(email)
              .country(country)
              .executeWithHttpInfo();
      System.out.println(response.getResponseBody());
      System.out.println(response.getResponseHeaders());
      System.out.println(response.getStatusCode());
      System.out.println(response.getRoundTripTime());
      System.out.println(response.getRequest());
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#update");
      System.err.println("Status code: " + e.getStatusCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | **String**|  | |
| **usersUpdateRequest** | [**UsersUpdateRequest**](UsersUpdateRequest.md)|  | |

### Return type

[**UsersUpdateResponse**](UsersUpdateResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * date -  <br>  * server -  <br>  * content-length -  <br>  * content-type -  <br>  |

