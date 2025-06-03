import requests
import os
import subprocess
import platform
import tempfile

INSTANCE_URL = "https://raw.githubusercontent.com/Alexciao/mcs-modpack-installer/master/instance.zip"


def download_instance():
    """
    Downloads the instance zip file from the specified URL and saves it to a temporary file.
    Returns the path to the downloaded file.
    """
    response = requests.get(INSTANCE_URL, stream=True)
    response.raise_for_status()  # Raise an error for bad responses

    total_length = response.headers.get("content-length")
    if total_length is not None:
        total_length = int(total_length)
    downloaded = 0

    with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_file:
        last_percent: float = -1
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                temp_file.write(chunk)
                if total_length:
                    downloaded += len(chunk)
                    percent = round(downloaded * 100 / total_length)
                    if percent != last_percent:
                        print(f"Downloading {percent}%")
                        last_percent = percent
        print("Download completed")
        return temp_file.name


def install_instance():
    # Check for Windows support
    if platform.system() != "Windows":
        raise NotImplementedError("This application only supports Windows")

    # Get PrismLauncher path
    from checker import get_prismlauncher_paths

    path = os.path.join(get_prismlauncher_paths()[0], "prismlauncher.exe")


if __name__ == "__main__":
    install_instance()
