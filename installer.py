import subprocess
import requests
import platform
import tempfile
import logging

log = logging.getLogger()


def get_prism_url(version: str = "9.4") -> str:
    """
    Downloads the Prism Launcher installer based on the operating system.
    Returns the path to the downloaded installer.
    """
    system = platform.system()
    url = f"https://github.com/PrismLauncher/PrismLauncher/releases/download/{version}/"

    if system == "Windows":
        url += f"PrismLauncher-Windows-MSVC-Setup-{version}.exe"

    elif system == "Darwin":  # macOS
        url += f"PrismLauncher-macOS-{version}.zip"

    else:
        raise NotImplementedError("System unsupported")

    return url


def download_installer(url: str) -> str:
    """
    Downloads the installer from the given URL and saves it to a temporary file.
    Returns the path to the downloaded file.
    """
    log.info(f"Downloading Prism Launcher installer")

    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an error for bad responses

    total_length = response.headers.get("content-length")
    if total_length is not None:
        total_length = int(total_length)
    downloaded = 0

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        last_percent: float = -1
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                temp_file.write(chunk)
                if total_length:
                    downloaded += len(chunk)
                    percent = round(downloaded * 100 / total_length)
                    if percent != last_percent:
                        log.info(f"Downloading {percent}%")
                        last_percent = percent
        log.info("Download completed")
        return temp_file.name


def run_installer(filename: str) -> None:
    """
    Installs Prism Launcher using the downloaded installer file.
    This function is a placeholder and should be implemented based on the OS.
    """
    system = platform.system()
    log.info(f"Installing...")

    if system == "Windows":
        # Windows installation logic (e.g., running the installer)
        subprocess.run([filename, "/S", "/ALLUSERS=0", "/LANG=ENGLISH"], check=True)
    elif system == "Darwin":

        subprocess.run(
            ["unzip", filename, "-d", "/Applications/PrismLauncher"], check=True
        )
    else:
        raise NotImplementedError("Installation not implemented for this OS")


def install_prism_launcher(version: str = "9.4"):
    """
    Main function to download and install Prism Launcher.
    """
    log.info(f"Starting Prism Launcher installation for {platform.system()}")

    url = get_prism_url(version)
    installer_path = download_installer(url)
    run_installer(installer_path)
    log.info("Launcher installation completed")
