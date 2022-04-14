from google.cloud import pubsub_v1
publisher = pubsub_v1.PublisherClient();

def calculator(request):
    request_json = request.get_json()

    topicpath=publisher.topic_path('cloud-functions-346700','food-order-topic')
    
    headers = {'Access-Control-Allow-Origin': '*'}

    if request.args:
      if 'operation' in request.args:
        opcode=request.args.get('operation')
        if 'data1' in request.args and 'data2' in request.args:
          try:
            dat1=request.args.get('data1')
            dat2=request.args.get('data2')
            if opcode == 'add':
              return (str(float(dat1) + float(dat2)),200,headers)
            elif opcode == 'sub':
              return (str(float(dat1) - float(dat2)),200,headers)
            elif opcode == 'mul':
              return (str(float(dat1) * float(dat2)),200,headers)
            elif opcode == 'div':
              if float(dat2) == 0:
                return ("Div by Zero!",500,headers)
              else:
                return (str(float(dat1) / float(dat2)),200,headers)
            else:
              return ("Operation does not exist",500,headers)
          except BaseException as e:
            return (str(e),500,headers)
        else:
          return ("No data was entered",500,headers)
      elif 'publish' in request.args:
        try:
          futurepublish=publisher.publish(topicpath,data="Sent food order".encode("utf-8"))
          futurepublish.result()
          return ("Message Published!",200,headers)
        except BaseException as e:
          return (str(e),500,headers)
      else:
        return ("No operation was entered.",500,headers)
    else:
      return ("No arguments were entered.",500,headers)
