'''Mini-Project: Simple Test Reporter
Input: a list of test cases (name, result)
Output:
    Console report (✅ / ❌ with counts)
    JSON file with structured results
    Focus: Python fundamentals → functions, loops, file handling, JSON serialization.'''
import argparse
import logging
from pathlib import Path
from test_data import test_results
from reporter import print_report, save_report

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        )
    
def parse_args():
    parser = argparse.ArgumentParser(description="Simple Test Reporter")
    parser.add_argument(
        "--output",
         type=Path,
         default=Path("report.json"),
         help="Output JSON report file (default: report.json)",
     )
    return parser.parse_args()

if __name__ == "__main__":
    setup_logging()
    args = parse_args()
    passed, failed = print_report(test_results)
    save_report(test_results)
