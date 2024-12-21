import os
import csv
import sys
import importlib
from datetime import datetime

path = "."
test_prefix = "module"
test_case_file_name = "test-case.csv"
entries = os.listdir(path)
matching_dirs = sorted(
    [entry for entry in entries if os.path.isdir(os.path.join(path, entry)) and entry.startswith(test_prefix)],
    key=lambda entry: entry
)
test_case_file_path = os.path.join(path, test_case_file_name)

raise_message = ""
try:
    for directory in matching_dirs:
        test_case_file_path = os.path.join(path, directory, test_case_file_name)
        if os.path.isfile(test_case_file_path):
            with open(test_case_file_path, mode="r", encoding="utf-8") as file:
                test_cases = []
                reader = csv.DictReader(file)
                for row in reader:
                    test_cases.append(row)
                module_path = os.path.join(path, directory)
                sys.path.append(module_path)
                try:
                    input_func_module = importlib.import_module(directory)
                    input_func = getattr(input_func_module, "input_func")
                    success = 0
                    failed = 0
                    count = 0
                    print(f"Starting test cases for module: `{directory}`")
                    for test_case in test_cases:
                        count += 1
                        try:
                            start_time = datetime.now()
                            result = str(input_func(test_case["input"]))
                            end_time = datetime.now()
                            runtime_ms = (end_time - start_time).total_seconds() * 1000
                            assert result == test_case["output"], f"unexpected result result: `{result}` != expected: `{test_case['output']}` (input: {test_case['input']})"
                            success += 1

                            if test_case.keys().__contains__("time_limit"):
                                if runtime_ms > int(test_case["time_limit"]):
                                    raise Exception(f"time limit exceeded runtime: {runtime_ms}ms > {test_case['time_limit']}ms (input: {test_case['input']})")

                            print(f"module: `{directory}` test case: {count} - OK runtime: {runtime_ms}ms")
                        except AssertionError as e:
                            failed += 1
                            raise_message += f"module: `{directory}` test case: {count} - FAIL info: {e}\n"
                            print(f"module: `{directory}` test case: {count} - FAIL info: {e}")
                        except Exception as test_error:
                            failed += 1
                            raise_message += f"module: `{directory}` test case: {count} - ERROR info: {test_error}\n"
                            print(f"module: `{directory}` test case: {count} - ERROR info: {test_error}")
                    if failed > 0:
                        print(f"=== FAIL ===\n{failed} out of {count} test cases failed.")
                    else:
                        print(f"=== SUCCESS ===\n{success} out of {count} test cases passed.")
                except ModuleNotFoundError:
                    print(f"=== FAIL ===\nModule 'input_func' not found in '{directory}'.")
                finally:
                    sys.path.remove(module_path)
        else:
            print(f"=== FAIL ===\n'{test_case_file_name}' not found in '{directory}'.")
        print()
except Exception as e:
    print(f"=== FAIL ===\n{e}")

if raise_message:
    raise Exception("\n" + raise_message)