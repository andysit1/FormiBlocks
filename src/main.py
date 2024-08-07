from typing import Union
from fastapi import FastAPI
import subprocess
import logging

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#TODO/FEATURE
"""
    Write logic to handle project launch from base directories
    make a central class to handle directories and files.
"""

def opencmd():
    subprocess.run(['start', 'cmd'], shell=True) #automatically calls the virtual env of the subprocess, this is nice!

def runandget():
    myprocess = subprocess.run(["ls"], stdout=subprocess.PIPE)
    thoutput = myprocess.stdout.decode('utf-8')
    return thoutput

@app.post("/doit")
def dothis():
    resultfunc = runandget()
    opencmd()
    return {"result": resultfunc}
