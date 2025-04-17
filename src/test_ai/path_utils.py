
# import os
# import sys
# from pathlib import Path


# def set_project_paths():
#     """Set up the necessary project paths globally, resolving the project root directory."""
#     # Get the absolute path of the script
#     current_dir = Path(__file__).resolve().parent

#     # Traverse up to the project root directory by looking for .venv or another indicator
#     while not (current_dir / ".venv").exists():
#         current_dir = current_dir.parent
#         # Stop if we've reached the root directory (no .venv found)
#         if current_dir == current_dir.parent:
#             raise FileNotFoundError(
#                 "Could not find the project root directory with a .venv folder"
#             )

#     project_dir = current_dir  # This is the root of the project

#     # Define other paths relative to the project root
#     parent_dir = project_dir.parent
#     data_dir = project_dir / "data"    
#     template_dir = project_dir / "template"
#     output_dir = project_dir / "output"
#     db_dir = project_dir / "db"    
#     src_dir = project_dir / "src"

#     # Add project directories to sys.path for module imports
#     for directory in [
#         parent_dir,
#         project_dir,
#         data_dir,        
#         template_dir,
#         output_dir,
#         db_dir,               
#         src_dir,
#     ]:
#         if str(directory) not in sys.path:
#             sys.path.insert(0, str(directory))





#     # Return the paths for verification if needed
#     return {
#         "current_dir": current_dir,
#         "parent_dir": parent_dir,
#         "project_dir": project_dir,
#         "template_dir": template_dir,
#         "db_dir": db_dir,
#         "output_dir": output_dir,       
#         "src_dir": src_dir,
#         "data_dir":data_dir,
#     }





import os
import sys
from pathlib import Path


def get_project_root():
    """Get the project root by looking for pyproject.toml or another marker file."""
    current_path = Path(__file__).resolve()
    while current_path.parent != current_path:
        if (current_path / "pyproject.toml").exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError("Project root not found!")

# Define paths relative to the project root
PROJECT_ROOT = get_project_root()
PATHS = {
    "data_dir": PROJECT_ROOT / "data",
    "project_dir": PROJECT_ROOT,
    "template_dir": PROJECT_ROOT / "template",
    "db_dir": PROJECT_ROOT / "db",
    "output_dir": PROJECT_ROOT / "output",
    "src_dir": PROJECT_ROOT / "src"
}

def get_path(key: str) -> Path:
    """Get a pre-defined path by key."""
    if key not in PATHS:
        raise KeyError(f"Path key '{key}' not recognized. Valid keys: {list(PATHS.keys())}")
    return PATHS[key]

# Expose the get_path function for imports
__all__ = ["get_path"]