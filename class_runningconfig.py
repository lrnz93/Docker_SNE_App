class RunningConfig:
    class __RunningConfig:
        def __init__(self):
            self.dict = dict()

    instance = None

    def __init__(self, key=None, value=None):
        if not RunningConfig.instance:
            RunningConfig.instance = RunningConfig.__RunningConfig()

    def get_config(self, key):
        return self.instance.dict[key]

    def set_config(self, key, value):
        return self.instance.dict.update({key:value})
