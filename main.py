import LdapManager
import util


def main():

    # ldap_server = 'localhost'
    # ldap_port = '389'
    # ssl = False
    domain_name = 'dc=hpcpart,dc=info'
    admin = 'ldapadm'
    username = 'ldapadm'
    password = 'imsi0000'
    # admin = False

    attrs = {
        'objectClass': [b"person", b"posixAccount", b"inetOrgPerson"],
        'cn': b'02',
        'sn': b'test',
        'uid': b'test02',
        'homeDirectory': b'/home01/test02',
        'uidNumber': b'2003',
        'gidNumber': b'2000',
        'userPassword': bytes(util.encrypt_string('imsi0000'), 'utf-8'),
        'loginShell': b'/bin/bash'
    }

    old_attrs = {'userPassword': [b'imsi0001']}

    new_attrs = {'userPassword': [b'imsi0000']}

    # user = LdapManager.LdapUser(domain_name=domain_name, username=admin, password=password)
    # print(user.search_user())
    # user.modify_user(old_attrs, new_attrs)

    admin = LdapManager.LdapAdmin(domain_name=domain_name, username=username, password=password)
    # admin.add_user(attrs)
    # admin.delete_user('test02')
    print(admin.search_user('jrpark'))
    # admin.modify_user('test02', old_attrs, new_attrs)


if __name__ == '__main__':
    main()
