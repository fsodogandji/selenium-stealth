from selenium.webdriver import Chrome as Driver
from typing import Any
import json

def send(driver, cmd, params={}):
  resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
  url = driver.command_executor._url + resource
  body = json.dumps({'cmd': cmd, 'params': params})
  response = driver.command_executor._request('POST', url, body)
  return response.get('value')


def evaluationString(fun: str, *args: Any) -> str:
    """Convert function and arguments to str."""
    _args = ', '.join([
        json.dumps('undefined' if arg is None else arg) for arg in args
    ])
    expr = '(' + fun + ')(' + _args + ')'
    return expr


def evaluateOnNewDocument(driver: Driver, pagefunction: str, *args: str) -> None:

    js_code = evaluationString(pagefunction, *args)
    send(driver,'Page.addScriptToEvaluateOnNewDocument',{
        "source": js_code,
    })
    
