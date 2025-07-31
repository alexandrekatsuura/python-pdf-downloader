# 📝 Python PDF Downloader

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-pdf-downloader?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-pdf-downloader?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-pdf-downloader?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-pdf-downloader?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-pdf-downloader?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created for learning purposes only.
> It is not intended for production use.

## ℹ️ About

This project is a command-line application built in Python that allows users to download PDF and other document files from specific websites. It's designed to demonstrate clean code structure, encapsulation, and testing with `pytest`.

## 🚀 Features

*   **Document Download**: Download PDF and other document files from provided URLs.
*   **Command-Line Interface (CLI)**: Simple interactive interface for user interaction.
*   **Error Handling**: Handles invalid URLs, network errors, and file saving issues gracefully.
*   **Unit Testing**: Comprehensive tests included using `pytest` to ensure accuracy and reliability.
*   **Clean Project Structure**: Modular organization for clarity, maintainability, and scalability.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **`requests`**: For making HTTP requests.
*   **`BeautifulSoup4`**: For parsing HTML content (optional, for future enhancements).
*   **`pytest`**: Framework used to create and run unit tests.

## ⚙️ How to Run the Project

### Prerequisites

Ensure that Python 3.x is installed on your machine.

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/alexandrekatsuura/python-pdf-downloader
    cd python-pdf-downloader
    ```

2.  (Optional but recommended) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Linux/macOS
    # .venv\\Scripts\\activate       # On Windows
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the program, use the following command:

```bash
python src/main.py
```

You will be prompted to enter the URL of the document to download and the desired output filename. The program will attempt to download and save the file.

## ✅ Running the Tests

To run the unit tests, from the project root directory:

```bash
pytest -v
```

This will execute all test cases located in the `tests/` directory, ensuring the download logic is working correctly.

## 📁 Project Structure

```bash
python-pdf-downloader/
├── src/
│   ├── main.py             # Main application entry point and CLI logic
│   └── downloader.py       # Core document download logic
├── tests/
│   └── test_downloader.py  # Unit tests for the Downloader class
├── .gitignore              # Specifies intentionally untracked files to ignore by Git
├── README.md               # Project documentation and setup instructions
└── requirements.txt        # Lists project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).


