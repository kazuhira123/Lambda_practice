import json #jsonモジュールをimport
def myfunc01_handler(event, context):
  x = int(event["x"])
  y = int(event["y"])
  print("x = " + str(x))
  print("y = " + str(y))
  retval = {"result" : x / y}
  return json.dumps(retval) #JSON形式で結果を返す