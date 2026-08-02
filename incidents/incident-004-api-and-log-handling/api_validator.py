import logging
import json
logging.basicConfig(filename="app_gateway.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

raw_payload_from_api = '{"order_id": 101}'

try:
    required_fields = ["order_id", "customer_id", "amount"]
    playloadData = json.loads(raw_payload_from_api)
    flag = True
    for key in required_fields:
        if key not in playloadData:
            flag = False
    if not flag:
        logging.error("Payload missing required fields.")
        status = {"status": "BAD_REQUEST", "code": 400}
    if flag:
        if playloadData["amount"] < 0:
            logging.error("Amount cannot be negative.")
            status = {"status": "BAD_REQUEST", "code": 400}
        else:
            logging.info("Payload validation successful.")
            status = {"status": "OK", "code": 200}
except json.JSONDecodeError as e:
    logging.error(f"Error decoding JSON payload: {e}")
    status = {"status": "BAD_REQUEST", "code": 400}
print(status)


        
