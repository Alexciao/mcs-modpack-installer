import ui
import checker
import instance
import installer


def install_prism_launcher():
    """
    Main function to install Prism Launcher and the Minecraft instance.
    """
    # Check if Prism Launcher is installed
    if not checker.is_prism_launcher_installed():
        # Get the download URL for the Prism Launcher installer
        url = installer.get_prism_url()
        # Download the installer
        installer_path = installer.download_installer(url)
        # Run the installer
        installer.run_installer(installer_path)

    # Install the Minecraft instance
    instance.install_instance()


if __name__ == "__main__":
    # Create the main GUI window
    window = ui.create_main_window()
    window.mainloop()
