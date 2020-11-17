import boto3

TableName = "Employee"

client = boto3.client('dynamodb')

db = boto3.resource('dynamodb')

table = db.table(TableName)

table.get_item(key={Primary_Column_Name : Primary_Key})

table.put_item()