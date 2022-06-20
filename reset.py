from Encrption import Encrypt

a = Encrypt()
a.init("iuFXgJButnhpWkFT4Q8PPCdAbQsfndh2XWVbMFYC164=")

data = b'{"total_file":"0","mood":"dark","password":"meherab","file_data": {}}'
data = a.encrypy(data=data)


# with open("dist\OneType\gaaaw.axx","wb") as f:
#     f.write(data)

with open("gaaaw.axx","wb") as f:
    f.write(data)
