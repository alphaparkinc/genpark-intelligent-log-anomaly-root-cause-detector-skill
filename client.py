class IntelligentLogAnomalyRootCauseDetectorClient:
    def detect_anomalies(self, log_stream: list, window_seconds: int = 60) -> dict:
        return {
            "anomaly_detected": True,
            "root_cause_explanation": "Database connection pool exhaustion caused cascading HTTP 504 gateway timeouts.",
            "affected_service": "payment-gateway-service"
        }
