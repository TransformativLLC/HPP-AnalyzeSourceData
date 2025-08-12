import os
from typing import List


def get_source_file_names(raw_data_dir: str | None = os.getenv("RAW_DATA_BASE_DIR"),
                          upload_template: str | None = os.getenv("UPLOAD_TEMPLATE"),
                          target_extension: str = ".xlsx",
                          full_path: bool = True) -> List[str]:
    """
    Retrieve a list of raw data files from a specified directory, excluding the upload template.

    Args:
        raw_data_dir (str | None): Path to the directory containing data files.
                                   Defaults to RAW_DATA_BASE_DIR environment variable.
        upload_template (str | None): Name of the template file to exclude.
                                      Defaults to UPLOAD_TEMPLATE environment variable.
        target_extension (str): File extension to filter. Defaults to ".xlsx".
        full_path (bool): If True, include full path instead of relative path. Defaults to True.

    Returns:
        List[str]: List of filenames matching the criteria.

    Raises:
        PermissionError: If the program lacks permission to access the directory.
        Exception: For other unexpected errors during file operations.
    """
    source_files = []
    try:
        if raw_data_dir and os.path.exists(raw_data_dir):
            files = os.listdir(raw_data_dir)

            for file in files:
                if file != upload_template and file.endswith(target_extension):
                    source_files.append(f"{raw_data_dir if full_path else ''}{file}")
        else:
            print("Directory not found or RAW_DATA_BASE_DIR not set")
    except PermissionError:
        print("Permission denied to access the directory")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return source_files
