# Azure Alert Integration

Integration with Azure Alerts for Relay

## Actions

|   Type    |  Name              | Description          |
|-----------|--------------------|----------------------|
| Trigger   | [azure-alert-webhook](/triggers/azure-alert-webhook) | Triggers when an azure alert is detected |

## Contributing

### Issues

Feel free to submit issues and enhancement requests.

### Contributing

In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

### License

As indicated by the repository, this project is licensed under Apache 2.0.

# NOTES
### Crrently supported alert contexts

Alert contexts to write steps for:
- Log Analytics
- Application Insights
- Log Alerts v2
- Metric Alerts
- Activity Log - Policy
- Activity Log - Administrative
- Activity Log - AutoScale
- Service Health
- Resource Health

Custom JSON Payloads ?
https://docs.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-common-schema-definitions