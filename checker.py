import os
import platform


def get_prismlauncher_paths():
    """
    Returns a list of potential Prism Launcher installation paths
    based on the operating system.
    """
    system = platform.system()
    paths = []

    if system == "Windows":
        appdata = os.getenv("APPDATA")
        local_appdata = os.getenv("LOCALAPPDATA")
        if appdata:
            paths.append(os.path.join(appdata, "PrismLauncher"))
        if local_appdata:
            paths.append(os.path.join(local_appdata, "Programs", "PrismLauncher"))

    elif system == "Darwin":  # macOS
        home = os.path.expanduser("~")
        paths.append(
            os.path.join(home, "Library", "Application Support", "PrismLauncher")
        )
    return paths


def is_prismlauncher_installed():
    """
    Checks if Prism Launcher is installed by looking for its directory
    in common locations based on the operating system.
    """
    potential_paths = get_prismlauncher_paths()
    if not potential_paths:
        raise NotImplementedError("System unsupported")

    for path in potential_paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                return True
    return False


if __name__ == "__main__":
    if is_prismlauncher_installed():
        print(f"Prism Launcher appears to be installed on {platform.system()}.")
    else:
        print(f"Prism Launcher does not appear to be installed on {platform.system()}.")
