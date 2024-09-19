import uuid 

def generateuuid(name:str):
    namespace = uuid.NAMESPACE_DNS
    uuid_v5 = uuid.uuid5(namespace,name)
    return uuid_v5