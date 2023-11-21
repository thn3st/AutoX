class ProxyConvert:
    @staticmethod
    def convert_proxy_string_to_proxy(proxy_string):
        proxy_host = proxy_string.split(':')[0]
        proxy_port = proxy_string.split(':')[1]
        try:
            proxy_username = proxy_string.split(':')[2]
            proxy_password = proxy_string.split(':')[3]
        except:
            proxy_username, proxy_password = ('', '')

        if proxy_username != '':
            proxy = f'{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
        else:
            proxy = proxy_string
        return proxy

    @staticmethod
    def convert_proxy_string_to_proxy_json(proxy_string):
        proxy_host = proxy_string.split(':')[0]
        proxy_port = proxy_string.split(':')[1]
        try:
            proxy_username = proxy_string.split(':')[2]
            proxy_password = proxy_string.split(':')[3]
        except:
            proxy_username, proxy_password = ('', '')
        return {
            'proxy_host': proxy_host,
            'proxy_port': proxy_port,
            'proxy_username': proxy_username,
            'proxy_password': proxy_password
        }
