# konfig-typescript-sdk@1.0.0

This API manages a simple User database
## Installing

### npm
```
npm install konfig-typescript-sdk --save
```

### yarn
```
yarn add konfig-typescript-sdk
```

**Important note: this library is can be used in both the client-side or server-side, but using it
in client-side browser code is not recommended as you would expose security credentials.**



## Getting Started

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

## Documentation for API Endpoints

All URIs are relative to *https://api.konfigthis.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UsersApi* | [**create**](docs/UsersApi.md#create) | **POST** /users | Create User
*UsersApi* | [**delete**](docs/UsersApi.md#delete) | **DELETE** /users/{user_id} | Delete User
*UsersApi* | [**get**](docs/UsersApi.md#get) | **GET** /users/{user_id} | Get User
*UsersApi* | [**list**](docs/UsersApi.md#list) | **GET** /users | Get Users
*UsersApi* | [**update**](docs/UsersApi.md#update) | **PUT** /users/{user_id} | Update User

