# Application Support Incident Lab

A small practice lab where I train myself to investigate support incidents the way I do at work: start from the symptom, read the logs, find the cause, and write it up.

This is a learning project. The logs and scenarios are simulated for practice, not taken from a real system.

## What's inside

| Folder | Practice scenario |
|---|---|
| `incidents/incident-001-payment-gap` | A payment gap, investigated from a server log, with an investigation note |
| `incidents/incident-002-gateway-timeout` | A gateway timeout, investigated from an API gateway log, with an investigation note |
| `incidents/incident-003-code-crash` | A small Python script that crashes, and a fixed version |
| `incidents/incident-004-api-and-log-handling` | Small Python scripts for checking an API response and parsing a log |

The root folder also has sample log files (`app.log`, `app_gateway.log`, `errors_summary.log`) used for practice.

## Tools

Python, reading logs, basic Linux commands, Markdown for the write-ups.

## Status

Still learning, and adding scenarios when I have time.
