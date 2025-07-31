import requests
import os

class Downloader:
    """A class to handle downloading of files from URLs."""

    def __init__(self):
        """Initializes the Downloader class."""
        pass

    def download_file(self, url: str, output_path: str) -> bool:
        """Downloads a file from a given URL and saves it to the specified path.

        Args:
            url (str): The URL of the file to download.
            output_path (str): The local path where the file will be saved.

        Returns:
            bool: True if the download was successful, False otherwise.
        """
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

            with open(output_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            return False
        except IOError as e:
            print(f"Error saving file to {output_path}: {e}")
            return False



