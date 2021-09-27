import boto3

#connection
DB =boto3.resource('dynamodb')
table = DB.Table('employee') #table name

#PUT DATA
response = table.put_item(
    Item={
        'emp_id': "44",
        'name' :"Nikil",
        'age': "24"
            }
        )
print(response)

#GET DATA
response = table.get_item(
            Key={
                'emp_id':"44"
            }
        )
print(response["item"]) #Data is inside item

#DELETE DATA
response = table.delete_item(
            Key={
                'age':"24"
            }
        )
print(response)

#UPDATE DATA
table.update_item(
    Key={
        'emp_id': '44',
    },
    UpdateExpression='SET name = :values',
    ExpressionAttributeValues={
        ':values': 'Gupta'
    }
)
print(response['Item'])