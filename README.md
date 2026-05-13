Threat Intel AggregatorFastAPI tool. Hits AbuseIPDB and VirusTotal. Combines data. One report. Simple.FeaturesAsync Logic: Fast calls. No waiting.Data Cleanup: Raw JSON made human-readable.Containerized: Runs anywhere with Docker.SetupCreate .env file.Add keys:Code snippetABUSEIPDB_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
Run with DockerBashdocker build -t threat-api .
docker run -p 8080:8000 threat-api
Go to: http://localhost:8080/docsTest IPs (Hall of Fame)CategoryIP AddressExpected ResultMalicious193.163.125.138High score. Red flags.Clean8.8.8.8Safe. Trusted.Cloud47.77.231.186Alibaba infrastructure.Crawler185.191.171.1Known SEO bot.