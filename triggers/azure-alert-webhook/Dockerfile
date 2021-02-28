FROM relaysh/core:latest-python
WORKDIR /trigger
COPY handler.py .
CMD python handler.py

LABEL "org.opencontainers.image.title"="Azure Alert Webhook Trigger"
LABEL "org.opencontainers.image.description"="Triggers a workflow in response to an Azure Alert webhook"