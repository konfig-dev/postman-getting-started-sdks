package com.konfigthis.client;

import com.konfigthis.client.api.UsersApi;

public class Konfig {
    private ApiClient apiClient;
    public final UsersApi users;

    public Konfig() {
        this(null);
    }

    public Konfig(Configuration configuration) {
        this.apiClient = new ApiClient(null, configuration);
        this.users = new UsersApi(this.apiClient);
    }

}
