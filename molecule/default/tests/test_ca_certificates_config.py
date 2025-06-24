import pytest
import re

INSTALLED_CA_CERTIFICATES_NAME = "ca-certificates"
INSTALLED_CURL_NAME = "curl"
VAULT_URL="https://vault.rachuna-net.pl/ui/"


def test_ca_certificates_installed(host):
    package = host.package(INSTALLED_CA_CERTIFICATES_NAME)
    assert package.is_installed, "Pakiet "+INSTALLED_CA_CERTIFICATES_NAME+" nie jest zainstalowany!"

def test_ca_certificates_installed(host):
    package = host.package(INSTALLED_CURL_NAME)
    assert package.is_installed, "Pakiet "+INSTALLED_CURL_NAME+" nie jest zainstalowany!"

def test_vault_url_accessible(host):
    """Sprawdza, czy curl może połączyć się z Vaultem przez HTTPS"""
    command = host.run(f"curl -s -o /dev/null -w '%{{http_code}}' {VAULT_URL}")
    assert command.rc == 0, "Błąd połączenia curl z Vaultem"
    assert command.stdout.strip() == "200", f"Vault nie zwrócił statusu 200 OK (otrzymano: {command.stdout.strip()})"