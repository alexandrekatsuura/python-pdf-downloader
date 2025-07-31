import os
from downloader import Downloader

class Main:
    """Main class to handle the command-line interface for the PDF downloader."""

    def __init__(self):
        """Initializes the Main class."""
        self.downloader = Downloader()

    def run(self):
        """Runs the main application loop."""
        print("Welcome to the PDF Downloader!")
        print("This tool allows you to download PDF and other document files from URLs.")
        print("-" * 60)

        while True:
            url = input("Enter the URL of the document to download (or 'quit' to exit): ").strip()
            
            if url.lower() == 'quit':
                print("Thank you for using the PDF Downloader!")
                break

            if not url:
                print("Please enter a valid URL.")
                continue

            filename = input("Enter the filename to save (with extension, e.g., 'document.pdf'): ").strip()
            
            if not filename:
                print("Please enter a valid filename.")
                continue

            # Create downloads directory if it doesn't exist
            downloads_dir = "downloads"
            if not os.path.exists(downloads_dir):
                os.makedirs(downloads_dir)

            output_path = os.path.join(downloads_dir, filename)

            print(f"Downloading {url}...")
            success = self.downloader.download_file(url, output_path)

            if success:
                print(f"File successfully downloaded to: {output_path}")
            else:
                print("Failed to download the file. Please check the URL and try again.")

            print("-" * 60)

if __name__ == "__main__":
    app = Main()
    app.run()

