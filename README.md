# ansible-role-cyhy-feeds #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cyhy-feeds/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-feeds/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-cyhy-feeds/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-feeds/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[cisagov/cyhy-feeds](https://github.com/cisagov/cyhy-feeds).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| file_owner_group | The name of the group that should own any files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| file_owner_username | The name of the user that should own any files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |

## Dependencies ##

- [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)
- [cisagov/ansible-role-python](https://github.com/cisagov/ansible-role-python)

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  tasks:
    - name: Install cyhy-feeds
      ansible.builtin.include_role:
        name: cyhy_feeds
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
