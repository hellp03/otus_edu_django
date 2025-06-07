import os
import pytest
from unittest.mock import patch
from utils import clean_monitor

class TestCleanMonitor:

    @patch('os.system')
    @patch('os.name', 'nt')  # Симулируем Windows
    def test_clean_monitor_windows(self, mock_system):
        clean_monitor()
        mock_system.assert_called_once_with('cls')  # Проверяем, что вызвана команда 'cls'

    @patch('os.system')
    @patch('os.name', 'posix')  # Симулируем Unix/Linux
    def test_clean_monitor_unix(self, mock_system):
        clean_monitor()
        mock_system.assert_called_once_with('clear')  # Проверяем, что вызвана команда 'clear'

    @patch('os.system')
    @patch('os.name', 'some_other_os')  # Симулируем другую ОС
    def test_clean_monitor_other_os(self, mock_system):
        clean_monitor()
        mock_system.assert_not_called()