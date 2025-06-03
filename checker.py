import os
import platform


def get_prismlauncher_paths():
    """
    Returns a list of potential Prism Launcher installation paths
    for Windows only.
    """
    system = platform.system()

    if system != "Windows":
        raise NotImplementedError("This application only supports Windows")

    paths = []
    local_appdata = os.getenv("LOCALAPPDATA")
    if local_appdata:
        paths.append(os.path.join(local_appdata, "Programs", "PrismLauncher"))

    return paths


def is_prismlauncher_installed():
    """
    Checks if Prism Launcher is installed by looking for its directory
    in common locations on Windows.
    """
    potential_paths = get_prismlauncher_paths()

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
