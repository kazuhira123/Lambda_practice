import json #jsonモジュールをimport
def myfunc01_handler(event, context):
  x = int(event["x"]) #event引数で渡された値を整数型に変換
  y = int(event["y"])
  print("x = " + str(x)) #引数に渡された値を文字列として標準出力する
  print("y = " + str(y))
  retval = {"result" : x / y}
  return json.dumps(retval) #JSON形式で結果を返す