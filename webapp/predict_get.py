import pycurl

port = 'localhost:5000'
url = "predict"

data = {
"CHAS": {"0": 0},
"RM": {"0": 6.575},
"TAX": {"0": 296.0},
"PTRATIO": {"0": 15.3},
"B": {"0": 396.9},
"LSTAT": {"0": 4.98},
}

path = f"{port}/{url}?CHAS={data['CHAS']['0']}&RM={data['RM']['0']}&TAX={data['TAX']['0']}&PTRATIO={data['PTRATIO']['0']}&B={data['B']['0']}&LSTAT={data['LSTAT']['0']}"
    
c = pycurl.Curl()

c.setopt(c.URL, path)
c.perform()
c.close()