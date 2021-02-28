from nebula_sdk import Interface, WebhookServer
from quart import Quart, request

import logging
import json 

relay = Interface{}
app = Quart('alert-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    data = await request.get_json()
    logging.info("Received the following webhook payload: \n%s", json.dumps(data, indent=4))

    if data['schemaId'] != 'azureMonitorCommonAlertSchema':
        return {'message': 'not a valid azure alert using the common alert schema'}, 400, {}
    else:
        essentials = data['data']['essentials']
        context = data['data']['alertContext']
        relay.events.emit({
            'alertId': essentials['alertId'],
            'alertRule': essentials['alertRule'],
            'severity': essentials['severity'],
            'signalType': essentials['signalType'],
            'monitorCondition': essentials['monitorCondition'],
            'monitoringService': essentials['monitoringService'],
            'alertTargetIDs': essentials['alertTargetIDs'],
            'originAlertId': essentials['originAlertId'],
            'firedDateTime': essentials['firedDateTime'],
            'resolvedDateTime': essentials['resolvedDateTime'],
            'description': essentials['description'],
            'essentialsVersion': essentials['essentialsVersion'],
            'alertContextVersion': essentials['alertContextVersion'],
            'alertContext': context
        })
        return {'success': True}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()