import ldap
import ldap.modlist as modlist
import util

class LdapBase:

    def __init__(self, ldap_server='localhost', ldap_port='389', ssl=False, domain_name=None, username=None, password=None):
        protocol = 'ldaps' if ssl else 'ldap'
        ldap_url = "{0}://{1}:{2}".format(protocol, ldap_server, ldap_port)
        try:
            self.user_ldap = ldap.initialize(ldap_url)
        except Exception as e:
            print(e)
        self.domain_name = domain_name
        self.username = username
        self.password = password

        self.bind()

    def bind(self):
        pass

    def delete(self, username):
        pass

    def modify(self):
        pass


class LdapAdmin(LdapBase):

    def bind(self):
        try:
            dn = "cn={0},{1}".format(self.username, self.domain_name)
            self.user_ldap.simple_bind_s(dn, self.password)
        except ldap.INVALID_CREDENTIALS:
            self.user_ldap.unbind()
            return 'Wrong username or password'
        except Exception as e:
            print(e)

        return "Successfully authenticated"

    def add_user(self, attrs):
        dn = "uid={0},ou=People,{1}".format(util.byte_to_string(attrs['uid']), self.domain_name)
        # attrs['userPassword'] = Util.encrypt_string(attrs['userPassword'])
        try:
            ldif = modlist.addModlist(attrs)
            self.user_ldap.add_s(dn, ldif)
        except Exception as e:
            print(e)

    def modify_user(self, username, old_attrs, new_attrs):
        dn = "uid={0},ou=People,{1}".format(username, self.domain_name)
        try:
            ldif = modlist.modifyModlist(old_attrs, new_attrs)
            print(ldif)
            self.user_ldap.modify_s(dn, ldif)
        except Exception as e:
            print(e)

    def delete_user(self, username):
        dn = "uid={0},ou=People,{1}".format(username, self.domain_name)
        try:
            self.user_ldap.delete_s(dn)
        # except ldap.LDAPError as le:
        #     print(e)
        except Exception as e:
            print(e)

    def search_user(self, username):
        dn = "uid={0},ou=People,{1}".format(username, self.domain_name)
        try:
            user_info = self.user_ldap.search_s(dn, ldap.SCOPE_SUBTREE, "objectclass=*")
            return user_info
        except Exception as e:
            print(e)


class LdapUser(LdapBase):

    # def __del__(self):
    #     self.user_ldap.unbind()
    #     print("객체가 삭제되었습니다.")

    def bind(self):
        dn = "uid={0},ou=People,{1}".format(self.username, self.domain_name)
        try:
            self.user_ldap.simple_bind_s(dn, self.password)
        except ldap.INVALID_CREDENTIALS:
            self.user_ldap.unbind()
            return print('Wrong username or password')
        except Exception as e:
            print(e)

        return "Successfully authenticated"

    def search_user(self):
        dn = "uid={0},ou=People,{1}".format(self.username, self.domain_name)
        try:
            user_info = self.user_ldap.search_s(dn, ldap.SCOPE_SUBTREE, "objectclass=*")
            return user_info
        except Exception as e:
            print(e)
