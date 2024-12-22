import yaml

def load_config(file_path="values.yaml"):
    """Load configuration from a YAML file."""
    try:
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        raise Exception(f"Configuration file not found: {file_path}")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")
