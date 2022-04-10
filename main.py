from flask import jsonify

def hello_world(request):
    
    if request.args and 'operation' in request.args:
        operation = request.args.get('operation')
        first_operand = request.args.get('data1')
        second_operand = request.args.get('data2')

    if operation == 'add':
        result = float(first_operand) + float(second_operand)
        calculation = {
            'total': str(result)
        }
    elif operation == 'sub':
        result = float(first_operand) - float(second_operand)
        calculation = {
            'total':str(result)
        }
    elif operation == 'mul':
        result = float(first_operand) * float(second_operand)
        calculation = {
            'total': str(result)
        }
    elif operation == 'div':
        if float(second_operand) == 0:
            calculation = {
                'total': 'Div by Zero!'
            }
        else:
            result = float(first_operand) / float(second_operand)
            calculation = {
                'total': str(result)
            }
    else:
        calculation = {
            'total': 'No operation!'
        }

    response = jsonify({
        'calculation': calculation
    })

    return response
