class MEOI:
    """
    Marketing Engineered Optimisation Intelligence (Inspector General Edition)
    Responsible for monitoring, diagnosing, and protecting the MEO Operating System.
    See role-card.md for full documentation.
    """

    def __init__(self):
        # Default states
        self.authority = "Proprietor"
        self.routing_active = False
        self.freeze_state = False
        self.log = []

    def receive_command(self, command: str) -> str:
        """
        Evaluate a command to control routing per Prime Directives.
        Returns a message indicating result.
        """
        allowed_commands = {"Start", "Proceed", "Begin routing", "Let's go"}
        if command in allowed_commands:
            self.routing_active = True
            return "Routing permitted"
        else:
            return "No action allowed"

    def freeze_module(self, reason: str) -> None:
        """
        Freeze a module under emergency exception (Directive 8).
        Only freezes; does not repair or correct.
        """
        self.freeze_state = True
        self.log_report("Freeze module", {"reason": reason})

    def detect_drift(self, issue: str, location: str, severity: str) -> None:
        """
        Log drift or corruption event with timestamp and severity (Directive 6).
        """
        self.log_report("Drift detected", {
            "issue": issue,
            "location": location,
            "severity": severity
        })

    def log_report(self, action: str, details: dict) -> None:
        """
        Record a report according to the transparency law (Directive 9).
        """
        from datetime import datetime, timezone
        report = {
            "action": action,
            "details": details,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        self.log.append(report)

    def get_reports(self) -> list:
        """
        Return all reports; does not clear them.
        """
        return list(self.log)

    # Additional internal methods can be added to reflect other directives;
    # all actions require explicit command from the Proprietor.
