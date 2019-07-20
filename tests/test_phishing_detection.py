#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `phishing_detection` package."""


import unittest
from click.testing import CliRunner

from phishing_detection import phishing_detection
from phishing_detection import cli


class TestPhishing_detection(unittest.TestCase):
    """Tests for `phishing_detection` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'phishing_detection.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
