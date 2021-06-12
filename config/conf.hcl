ui = true
disable_mlock = true

storage "file" {
    path = "/data"
}

listener "tcp" {
    address = "0.0.0.0:8200"
    tls_cert_file = "/etc/certs/vault.crt"
    tls_key_file = "/etc/certs/vault.key"
}

api_addr = "https://0.0.0.0:8200"
