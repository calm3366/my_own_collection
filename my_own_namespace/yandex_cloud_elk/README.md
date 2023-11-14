create_file_and_some_text
=========

Create some file in existing path and put there some text

[![Role](https://travis-ci.org/CyVerse-Ansible/ansible-role-template.svg?branch=master)](https://github.com/calm3366/my_own_collection/tree/master/my_own_namespace/yandex_cloud_elk/roles/create_file_and_some_text)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-name--of--my--role-blue.svg)](https://github.com/calm3366/my_own_collection/tree/master/my_own_namespace/yandex_cloud_elk)


Requirements
------------

no

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| path_to_file            | yes      | /tmp/some_file.txt| string              | existing path to file                     |
| content                 | no       |"Content in new file" | string               | some text                       |

Dependencies
------------

no

Example Playbook
----------------
```
---
- name: Create file and some text
  hosts: all
  roles: 
    - create_file_and_some_text
```    

License
-------

GPL

Author Information
------------------

Arihin Ivan