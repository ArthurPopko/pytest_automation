class Config:
    def __init__(self, env):
        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'The "{env}" env does not exist. Valid envs are in {SUPPORTED_ENVS}')

        self.base_url = {
            'dev': 'http://google.com',
            'qa': 'http://mail.ru'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]


