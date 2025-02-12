import time
import os
import kopf
import yaml
import kubernetes

# event handling
@kopf.on.create('otus.homework','v1','mysqls')
def on_create(body, spec, logger, **kwargs):
    name=body['metadata']['name']
    image = spec.get('image')
    database = spec.get('database')
    password = spec.get('password')
    size = spec.get('storageSize')

    create_pvc(name,size)
    create_svc(name)
    create_depl(name,image,password,database)
    message = f"On create event : pvc,svc,delp {name} created"
    logger.info(message)
    return{'message':message}


@kopf.on.update('otus.homework','v1','mysqls')
def on_update(spec, fields, logger, **kwargs):
    image = spec.get('image')
    name = fields['on_create']['deployment-name']
    update_depl(ns, name, image)
    message = f"On update event : depl {name} updated"
    logger.info(message)
    return{'message':message}

@kopf.on.delete('otus.homework','v1','mysql')
def on_delete(spec,name,logger,**kwargs):
    k8s_api = kubernetes.client.CoreV1Api()
    obj =  k8s_api.delete_persistent_volume(f"{name}-pv")
    message = f"On remove event : Persistent volume {name} deleted"
    loggger.info(message)
    return{'message':message}



# api functions
def create_pvc(name,storageSize):
    tmp = open(os.path.join(os.path.dirname(__file__),'t_pvc.yaml'),'rt').read()
    pvc = tmp.format(
               name = name,
               storageSize = storageSize
               )
    pvc_body = yaml.safe_load(pvc)
    kopf.adopt(pvc_body)
    k8s_api = kubernetes.client.CoreV1Api()
    obj = k8s_api.create_namespaced_persistent_volume_claim(
               namespace='default',
               body=pvc_body
               )
    return

def create_svc(name):
    tmp = open(os.path.join(os.path.dirname(__file__),'t_svc.yaml'),'rt').read()
    svc = tmp.format(
               name = name
               )
    svc_body = yaml.safe_load(svc)
    kopf.adopt(svc_body)
    k8s_api = kubernetes.client.CoreV1Api()
    obj = k8s_api.create_namespaced_service(
               namespace='default',
               body=svc_body
               )
    return

def create_depl(name,image,password,db):
    tmp = open(os.path.join(os.path.dirname(__file__),'t_depl.yaml'),'rt').read()
    depl = tmp.format(
               name = name,
               image = image,
               password = password,
               database = db
               )
    depl_body = yaml.safe_load(depl)
    kopf.adopt(depl_body)
    k8s_api = kubernetes.client.CoreV1Api()
    obj = k8s_api.create_namespaced_service(
               namespace=ns,
               body=svc_body
               )
    return

def update_depl(ns,name,image):
    deployment_patch = {'spec': {'template': {'spec': {'containers': [{'name': 'mysql', 'image': image}]}}}}

    api = kubernetes.client.AppsV1Api()
    obj = api.patch_namespaced_deployment(
    name=deployment_name,
    namespace=namespace,
    body=deployment_patch
    )

    return
