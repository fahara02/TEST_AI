from test_ai.path_utils import get_path

# Set up project paths
paths = get_path()

# Expose paths for use in other scripts
__all__ = ["paths"]
