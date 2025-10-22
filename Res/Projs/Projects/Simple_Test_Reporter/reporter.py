import json
import logging
import os
import tempfile
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__) #instead of logging.info(...)

def atomic_write(path: Path, content: str, encoding: str = "utf-8"):
     """Write file atomically: temp file + replace."""
     path = Path(path)
     path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile("w", dir=path.parent, delete=False, encoding=encoding) as tmp:
        tmp.write(content)
        tmp.flush()
        os.fsync(tmp.fileno())
    os.replace(tmp.name, str(path))

def print_report(test_results):
    """Print test results to console with counts."""
    passed = failed = 0
    for name, result in test_results:
        if result:
            print(f"✅ {name} PASSED")
            passed += 1
        else:
            print(f"❌ {name} FAILED")
            failed += 1

    total = len(test_results)
    rate = (passed / total * 100) if total > 0 else 0
    summary = f"Summary: {passed} passed, {failed} failed, total {total}, pass rate {rate:.1f}%"
    print("\n" + summary)
    logger.info(summary)

return passed, failed, rate


def save_report(test_results, output_file="report.json"):
    """Save test results as structured JSON with timestamp."""
    report = {
        "generated_at": datetime.utcnow().isoformat(),
        "total": len(test_results),
        "results": [
            {"name": name, "status": "PASSED" if result else "FAILED"}
            for name, result in test_results
        ],
    }

    Path(output_file).write_text(json.dumps(report, indent=2))
    print(f"\nReport written to {output_file}")
