#!/usr/bin/env python3
"""
Simple unit tests for orgchart.py

Tests the org chart generation functionality using test_org.csv
"""

import unittest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout

from orgchart import Employee, read_data_file, extract_org, render_ascii


class TestOrgChart(unittest.TestCase):
    """Simple tests for org chart functionality"""
    
    def test_org_structure_equals_expected_dictionary(self):
        """Test that org structure matches expected nested dictionary"""
        reports = read_data_file("test_org.csv")
        org = extract_org(reports)
        
        # Convert org structure to simple nested dict for comparison
        def org_to_dict(org_dict):
            result = {}
            for manager, subordinates in org_dict.items():
                result[manager.name] = {
                    "title": manager.title,
                    "nreports": manager.nreports,
                    "subordinates": org_to_dict(subordinates)
                }
            return result
        
        actual = org_to_dict(org)
        
        # Expected structure
        expected = {
            "Chuck Norris": {
                "title": "CEO",
                "nreports": 9,
                "subordinates": {
                    "Alice Johnson": {
                        "title": "Engineering Manager", 
                        "nreports": 3,
                        "subordinates": {
                            "Carol White": {"title": "Senior Developer", "nreports": 0, "subordinates": {}},
                            "Dave Brown": {"title": "Developer", "nreports": 0, "subordinates": {}},
                            "Eve Davis": {"title": "Junior Developer", "nreports": 0, "subordinates": {}}
                        }
                    },
                    "Bob Smith": {
                        "title": "Sales Manager",
                        "nreports": 4, 
                        "subordinates": {
                            "Frank Wilson": {
                                "title": "Sales Lead",
                                "nreports": 2,
                                "subordinates": {
                                    "Henry Taylor": {"title": "Sales Rep", "nreports": 0, "subordinates": {}},
                                    "Ivy Anderson": {"title": "Sales Rep", "nreports": 0, "subordinates": {}}
                                }
                            },
                            "Grace Miller": {"title": "Account Manager", "nreports": 0, "subordinates": {}}
                        }
                    }
                }
            }
        }
        
        self.assertEqual(actual, expected)
    
    def test_ascii_output_equals_expected_string(self):
        """Test that ASCII output matches expected string exactly"""
        reports = read_data_file("test_org.csv")
        org = extract_org(reports)
        
        # Capture ASCII output
        output = StringIO()
        with redirect_stdout(output):
            render_ascii(org)
        
        actual = output.getvalue().strip()
        
        # Expected ASCII output
        expected = """Chuck Norris (CEO) -- 9
├── Alice Johnson (Engineering Manager) -- 3
│   ├── Carol White (Senior Developer)
│   ├── Dave Brown (Developer)
│   └── Eve Davis (Junior Developer)
└── Bob Smith (Sales Manager) -- 4
    ├── Frank Wilson (Sales Lead) -- 2
    │   ├── Henry Taylor (Sales Rep)
    │   └── Ivy Anderson (Sales Rep)
    └── Grace Miller (Account Manager)"""
        
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    # Ensure the test file exists
    if not os.path.exists("test_org.csv"):
        print("Error: test_org.csv not found. Please create the test file first.")
        sys.exit(1)
    
    # Run all tests
    unittest.main(verbosity=2)