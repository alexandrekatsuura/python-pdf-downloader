import pytest
import os
import tempfile
from unittest.mock import patch, mock_open, MagicMock
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import requests

from downloader import Downloader

class TestDownloader:
    """Test class for the Downloader class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.downloader = Downloader()

    @patch('downloader.requests.get')
    def test_download_file_success(self, mock_get):
        """Test successful file download."""
        # Mock the response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.iter_content.return_value = [b'test content']
        mock_get.return_value = mock_response

        # Create a temporary file for testing
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name

        try:
            # Test the download
            result = self.downloader.download_file("http://example.com/test.pdf", temp_path)
            
            # Assertions
            assert result is True
            mock_get.assert_called_once_with("http://example.com/test.pdf", stream=True)
            mock_response.raise_for_status.assert_called_once()
            
            # Check if file was written
            with open(temp_path, 'rb') as f:
                content = f.read()
                assert content == b'test content'
        finally:
            # Clean up
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    @patch('downloader.requests.get')
    def test_download_file_http_error(self, mock_get):
        """Test download failure due to HTTP error."""
        # Mock the response to raise an HTTP error
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("HTTP Error")
        mock_get.return_value = mock_response

        # Test the download
        result = self.downloader.download_file("http://example.com/nonexistent.pdf", "test.pdf")
        
        # Assertions
        assert result is False
        mock_get.assert_called_once_with("http://example.com/nonexistent.pdf", stream=True)

    @patch('downloader.requests.get')
    def test_download_file_io_error(self, mock_get):
        """Test download failure due to IO error."""
        # Mock the response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.iter_content.return_value = [b'test content']
        mock_get.return_value = mock_response

        # Test the download with an invalid path
        result = self.downloader.download_file("http://example.com/test.pdf", "/invalid/path/test.pdf")
        
        # Assertions
        assert result is False
        mock_get.assert_called_once_with("http://example.com/test.pdf", stream=True)

    def test_downloader_initialization(self):
        """Test that the Downloader class initializes correctly."""
        downloader = Downloader()
        assert isinstance(downloader, Downloader)


