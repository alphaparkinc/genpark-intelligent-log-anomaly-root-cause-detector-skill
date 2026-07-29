from client import IntelligentLogAnomalyRootCauseDetectorClient

def main():
    client = IntelligentLogAnomalyRootCauseDetectorClient()
    logs = ["INFO: GET /checkout", "ERROR: ConnectionPoolTimeoutException", "FATAL: 504 Gateway Timeout"]
    res = client.detect_anomalies(logs, 60)
    print(f"Anomaly Detected: {res['anomaly_detected']}")
    print(f"Affected Service: {res['affected_service']}")
    print(f"Explanation: {res['root_cause_explanation']}")

if __name__ == "__main__":
    main()
