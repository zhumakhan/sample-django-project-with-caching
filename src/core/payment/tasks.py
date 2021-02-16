from __future__ import absolute_import, unicode_literals
import json
import requests

from celery.task import task


@task(name="send request to cloudpayments to send check to email")
def send_check_to_email(url=None,params=None,headers=None,data=None):
  try:
    response = requests.post(url=url,params=params,headers=headers,data=data)
    resp_body = json.loads(response.content)
    if resp_body.get("Success"):
      print("SEND CHECK TO EMAIL")
  except Exception as ex:
        print("ERROR IN REQUEST TO CLOUDPAYMENTS: ",ex)
  print('send request to cloudpayments to send check to email')