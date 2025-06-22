def escape_font_path(path):
    path = path.replace("\\", "/")  # Use forward slashes
    path = path.replace(":", "\\:")  # Escape colon
    return path