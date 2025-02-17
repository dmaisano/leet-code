def read_file_lines(file_path: str) -> list[str]:
    """Reads a text file and returns a list of its non-empty lines.
    Args:
        file_path: The relative path to the text file.
    Returns:
        A list of non-empty lines in the file, with any trailing newline characters removed.
    Raises:
        IOError: If there is an error opening or reading the file.
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return [line.rstrip("\n") for line in lines if line.rstrip("\n")]
    except IOError as e:
        raise IOError(f"Error reading file: {e}") from e
    except Exception as e:
        raise IOError(f"An unexpected error occurred: {e}") from e
