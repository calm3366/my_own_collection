#!/usr/bin/python3

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: test_module

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.test_module:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.test_module:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.test_module:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    # определить доступные аргументы/параметры, которые пользователь может передать модулю
    module_args = dict(
        # name=dict(type='str', required=True),
        # new=dict(type='bool', required=False, default=False)
        path_to_file=dict(type="str", required=True),
        content=dict(type="str", required=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    # задайте результат в объекте, который нас в первую очередь интересует, изменено, а состояние изменено, если этот модуль эффективно изменил целевое состояние, будет включать в себя любые данные, которые вы хотите, чтобы ваш модуль передал обратно для использования, например, в последующей задаче
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    #объект AnsibleModule будет нашей абстракцией, работающей с Ansible, включая создание экземпляров, парой общих атрибутов будут аргументы/параметры, передаваемые при выполнении, а также поддержка режима проверки модулем.
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    # если пользователь работает с этим модулем только в режиме проверки, мы не хотим вносить какие-либо изменения в среду, просто возвращаем текущее состояние без изменений
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    # манипулируйте или изменяйте состояние по мере необходимости (это будет та часть, где ваш модуль будет делать то, что ему нужно)
    
    #result['message'] = 'goodbye'
    my_file = open(module.params['path_to_file'], "w+")
    my_file.write(module.params['content'])
    my_file.close()
    result['original_message'] = module.params['path_to_file']
    result['message'] = 'file: {} | text: {}'.format(module.params['path_to_file'],module.params['content'])

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    # используйте любую логику, которая вам нужна, чтобы определить, внес ли этот модуль какие-либо изменения в вашу цель
    # if module.params['new']:
    #     result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    # во время выполнения модуля, если есть исключение или условное состояние, которое фактически вызывает сбой, запустите AnsibleModule.fail_json(), чтобы передать сообщение и результат
    if module.params['content'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    # в случае успешного выполнения модуля вам нужно будет просто выполнить AnsibleModule.exit_json(), передав результаты ключа/значения
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()