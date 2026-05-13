# Threat Intelligence API

FastAPI tool, integrated with **AbuseIPDB** and **VirusTotal** to give you one clean report on any ip address.

## Features
* **Async Logic:** No waiting during multiple calls
* **Data Cleanup:** Aggregation of only relevant data
* **Containerized:** Runs anywhere with Docker

## Setup
1. Create `.env` file.
2. Add keys:
```env
ABUSEIPDB_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
```


## Run with docker
```docker build -t threat-api .
docker run -p 8080:8000 threat-api
```

## Try it out with these IPs!
1. 193.163.125.138
2. 8.8.8.8
3. 47.77.231.186
4. 185.191.171.1

## Demo
With FastAPI's Swagger UI tool, you can test out any IP! Click "Try it out", enter an IP address..


<img width="1204" height="381" alt="Screenshot 2026-05-13 at 3 34 50 PM" src="https://github.com/user-attachments/assets/2246780a-d576-4d40-8196-9d9c6d432b62" />

<br>
<br>

And you get a JSON response with eveything you could ask for :) 
<br>


<img width="559" height="446" alt="Screenshot 2026-05-13 at 3 34 23 PM" src="https://github.com/user-attachments/assets/67f55dfa-3be9-447c-ba81-62fb01f12da6" />

