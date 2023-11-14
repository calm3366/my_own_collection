create_file_and_some_text
=========

Create some file in existing path and put there some text

[![Состояние сборки](https://travis-ci.org/CyVerse-Ansible/ansible-role-template.svg?branch=master)](https://travis-ci.org/CyVerse-Ansible/ansible -роль-шаблон)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-name--of--my--role-blue.svg)](https://galaxy.ansible.com /CyVerse-Ansible/ansible-role-template/)


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

---
- name: Create file and some text
  hosts: all
  roles: 
    - create_file_and_some_text

License
-------

GPL

Author Information
------------------

Arihin Ivan