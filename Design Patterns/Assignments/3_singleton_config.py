""" 
Implement a configuration manager using the Singleton 
Design Pattern. The configuration manager should read 
configuration settings from a file and provide access to 
these settings throughout the application. 
Demonstrate how the Singleton Design Pattern ensures 
that there is only one instance of the configuration manager,
preventing unnecessary multiple reads of the configuration 
file.
"""
class ConfigManager:
    # metaclass because it is best suited for this purpose.
    # private attribute
    _instance = None

    def __new__(cls):
        """
        Possible changes to the value of the `__init__` argument
        do not affect the returned instance.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._configurations = cls._instance._load_configurations()

        return cls._instance
    
    def _load_configurations(self):
        configurations = {}
        with open("configurations.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                configurations[key.strip()] = value.strip()
        return configurations

    def get_configuration(self, key=None):
        if key is None:
            return self._configurations
        return self._configurations.get(key, None)


config_manager1 = ConfigManager()
print("Configurations 1:")
print(config_manager1.get_configuration("setting1"))
print(config_manager1.get_configuration("setting2"))

# Changing configuration settings 
with open("configurations.txt", "w") as file:
    file.write("setting1 = value1_changed\n")
    file.write("setting2 = value2_changed\n")

config_manager2 = ConfigManager()
print("\nConfigurations 2:")
print(config_manager2.get_configuration("setting1"))  
print(config_manager2.get_configuration("setting2"))  

# config_manager1 and config_manager2 reference the same instance
print("\nAre config_manager1 and config_manager2 the same instance?")
print(config_manager1 is config_manager2)  