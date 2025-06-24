## Przykładowe użycie
```yml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: ca-certificates
      vars:
        input_debug: true
        input_certificates:
          ca: >-
              {{
                lookup('community.hashi_vault.vault_kv2_get', 'certificates/internal-serivces-intermediate-ca', engine_mount_point='kv')['secret']['certificate']
              }}
          intermediate: >-
              {{
                lookup('community.hashi_vault.vault_kv2_get', 'certificates/internal-services-intermediate-ca', engine_mount_point='kv')['secret']['intermediate']
              }}
```
## Testy molecule

```bash
python3 -m venv ~/.venvs/molecule
source ~/.venvs/molecule/bin/activate
pip install --upgrade pip

pip3 install ansible-core molecule molecule-proxmox pytest-testinfra ansible-lint molecule-plugins requests testinfra

export TEST_PROXMOX_DEBUG=
export TEST_PROXMOX_HOST=
export TEST_PROXMOX_PORT=
export TEST_PROXMOX_USER=
export TEST_PROXMOX_PASSWORD=
export TEST_PROXMOX_NODE=

molecule test

# molecule create
# molecule converge
# molecule verify
# molecule destroy
 ```