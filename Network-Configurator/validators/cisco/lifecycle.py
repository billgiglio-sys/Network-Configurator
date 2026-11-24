def validate(device_id, device, platform, environment):
    if platform.get('lifecycle') in {'end_of_sale','end_of_support'}:
        severity='error' if environment=='production' else 'warning'
        return [{'severity':severity,'code':'CISCO-LIFE-001','message':f'{device_id}: {device["platform"]["model"]} lifecycle is {platform["lifecycle"]}'}]
    return []
