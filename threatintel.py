# Takes an IP and reports valuable threat intelligence
import httpx
import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load all my enviornment variables
load_dotenv()
app = FastAPI()

# Assign AbuseIPDB API & VirusTotal keys for use later 
AbuseIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")
VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
# Headers for use later

@app.get("/check/{target_ip}")
async def read_root(target_ip: str):
    abuse_result = await call_abuseipdb(target_ip)
    vt_result = await call_virustotal(target_ip)

    # Filter for what we care about, for AbuseIPDB
    a_data = abuse_result.get("data", {})
    filtered_a_data = {
        "ip": a_data.get("ipAddress", "unknown"),
        "ip_version": a_data.get("ipVersion", "unknown"),
        "score": a_data.get("abuseConfidenceScore", None),
        "country": a_data.get("countryCode", None),
        "reports": a_data.get("totalReports", 0),
        "isp": a_data.get("isp", "unknown")
        }
    
    # Now for VirusTotal which is nested data - API Standard
    v_layer1 = vt_result.get("data", {})
    v_layer2 = v_layer1.get("attributes", {})
    v_layer3 = v_layer2.get("last_analysis_stats", {})
    filtered_v_data = {
        "malicious_count": v_layer3.get("malicious", 0),
        "harmless_count": v_layer3.get("harmless", 0),
        "reputation": v_layer2.get("reputation", "undetermined")
        }

    # Combine both in to a master set we care about
    our_data = {
        "abuse_intelligence": filtered_a_data,
        "vt_intelligence": filtered_v_data
    }
    return our_data

# Use AbuseIPDB API
async def call_abuseipdb(target_ip: str):
    abuseipdb_headers = {"Accept": "application/json", "Key": AbuseIPDB_API_KEY}
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers=abuseipdb_headers,
            params = {"ipAddress": target_ip,"maxAgeInDays": 90}
        )
        return response.json()
    
# Call/Use VirusTotal API
async def call_virustotal(target_ip: str):
    vt_headers = {"x-apikey": VT_API_KEY}
    async with httpx.AsyncClient() as client:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{target_ip}"
        response = await client.get(url, headers=vt_headers)
        return response.json()
    