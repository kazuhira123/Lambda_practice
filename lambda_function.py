import json
import urllib.request

def lambda_handler(event, context):
    for message_event in json.loads(event['body'])['events']:
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + 'LINE Developersのチャネルアクセストークン'
        }
        body = {
            'replyToken': message_event['replyToken'],
            'messages': [
                {
                    "type": "text",
                    "text": message_event['message']['text'],
                }
            ]
        }
        
        req = ullib.request.Request(url, data=json.dumps(body).encode('utf-8'), method='POST', headers=headers)
        with urllib.request.urlopen(req) as res:
            logger.info(res.read().decode("utf-8"))
            
            # TODO: write code...
        # TODO: write code...
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
