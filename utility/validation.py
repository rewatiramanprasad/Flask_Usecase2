from cerberus.validator import Validator
def date_device(data):
    schema = {'date1': {'type': 'string','required':True},'date2': {'type': 'string','required':True},'device': {'type': 'string','required':True}}
    v=Validator(schema)
    if (v.validate(data)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)


def validate_duplicate(query):
    schema={'query':{'type':'string'}}
    doc={'query':query}
    v=Validator(schema)
    if(v.validate(doc)):
        return True,"successfull validation"
    
    return False,v.errors

def validate_missingtime(device):
    schema= {
               'device':{'type':'string',
               'regex':'([D]){1}([1-3]){1}'}
            }
    
    v=Validator(schema)
    doc={'device':device}
    if(v.validate(doc)):
        return True
    else:
        return False

def credential(data):
    schema={'email':{'type':'string','required':True},'password':{'type':'string','required':True}}
    v=Validator(schema)
    if(v.validate(data)):
        return True,"successful validation"
    else:
        return False,v.errors

