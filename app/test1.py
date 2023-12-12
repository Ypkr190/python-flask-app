import boto3

def get_billing_amount_by_region(month):
    client = boto3.client('ce',aws_access_key_id='',aws_secret_access_key='gPTO1PuWMTSa9vqZs/nAHUHfo0v1j1dYUhDfBQUX',region_name='us-east-1')
    
    m = month.split("-")

    if m[1] in ['01','03','05','07',"08","10","12"] and int(m[0]) == 2023:
        start_date = f'{month}-01'
        end_date = f'{month}-31'
    elif m[1] in ['04',"06","09","11"] and int(m[0]) == 2023:
        start_date = f'{month}-01'
        end_date = f'{month}-30'
    else:
        start_date = f'{month}-01'
        end_date = f'{month}-28'
