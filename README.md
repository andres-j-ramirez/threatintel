# Threat Intel Aggregator

FastAPI tool. Hits **AbuseIPDB** and **VirusTotal**. Combines data. One report. Simple.

## Features
* **Async Logic:** Fast calls. No waiting.
* **Data Cleanup:** Raw JSON made human-readable.
* **Containerized:** Runs anywhere with Docker.

## Setup
1. Create `.env` file.
2. Add keys:
```env
ABUSEIPDB_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
