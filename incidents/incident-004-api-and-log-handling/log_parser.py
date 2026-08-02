import logging

try:
    with open("app_gateway.log", "r") as log_file, open("errors_summary.log", "a") as summary_file:
            summary_file.write("\n--- Error Summary ---\n")
            for line in log_file:
                if "ERROR" in line:
                    summary_file.write(line)
    print("Log parsing complete. Errors written to errors_summary.log")
except FileNotFoundError as e:
    print(f"Log file not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred while parsing logs: {e}")