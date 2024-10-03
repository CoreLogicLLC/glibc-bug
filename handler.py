import json



def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    
    try:
        import lxml.etree as etree
    except Exception as e:
        return {"statusCode": 200, "body": e.message}
    

    return {"statusCode": 200, "body": json.dumps(body)}
