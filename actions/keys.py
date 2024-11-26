class Keys:
    keys = {}

    @staticmethod
    def add_key(key_name):
        if key_name in Keys.keys:
            return
        Keys.keys[key_name] = True

    @staticmethod
    def get_key(key_name):
        return key_name in Keys.keys

    @staticmethod
    def remove_key(key_name):
        if key_name in Keys.keys:
            del Keys.keys[key_name]
        else:
            print(f"Warning: Key {key_name} not found to down, cannot up it.")

    @staticmethod
    def list_keys():
        return Keys.keys.keys()
