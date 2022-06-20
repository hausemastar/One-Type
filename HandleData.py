import json
from Encrption import Encrypt
from random import shuffle
import string


class PassData(Encrypt):
    def __init__(self) -> None:

        self.key = "iuFXgJButnhpWkFT4Q8PPCdAbQsfndh2XWVbMFYC164="
        self.init(self.key) 
        self.data = self.loadJsonData()


    def loadJsonData(self) -> dict:
        with open("gaaaw.axx","rb") as f:
            return json.loads(self.decrypt(data=f.read()))

    def refreshData(self):
        return self.loadJsonData()

    def getData(self):
        return self.data

    def FindDataFormTitle(self,title):
        self.data = self.refreshData()
        for i in self.data["file_data"]:
            if self.data["file_data"][i]["title"].lower() == title.lower():
                return [title,self.data["file_data"][i]["decr"]]

        return [0,0]

    def getAllTitle(self) -> list:
        title_list = []
        for i in self.data["file_data"]:
            title_list.append(i)
        
        return title_list

    
    def updateMoodData(self,data):
        with open("gaaaw.axx","wb") as f:
            bytes_data = json.dumps(data, indent=2).encode('utf-8')
            encrypt_data = self.encrypy(data=bytes_data)
            f.write(encrypt_data)
    
    def updatePassWord(self,data):
        with open("gaaaw.axx","wb") as f:
            bytes_data = json.dumps(data, indent=2).encode('utf-8')
            encrypt_data = self.encrypy(data=bytes_data)
            f.write(encrypt_data)
    

    # Return False if the title is alraedy stored else True
    def checkeValidTitle(self,title):
        data = self.data["file_data"]
        for i in data:
            # removeing extra spaces
            title = " ".join(title.split())

            if data[i]["title"].lower() == title.lower():
                # print("Found it")
                return False

        return True  
class HandelData(Encrypt):
    def __init__(self) -> None:

        self.key = "iuFXgJButnhpWkFT4Q8PPCdAbQsfndh2XWVbMFYC164="
        self.init(self.key) 

        self.data = self.loadJsonData()


    def loadJsonData(self) -> dict:
        with open("gaaaw.axx","rb") as f:
            return json.loads(self.decrypt(data=f.read()))


    # Take the title and desc as a list as function arg
    def saveData(self,dataHandel):
        if self.checkeTitle(dataHandel[0]):
            
            self.data["file_data"][self.GenRandomKey()] = {"title":dataHandel[0].capitalize(),"decr":dataHandel[1].capitalize()}
            index = int(self.data["total_file"]) + 1
            self.data["total_file"] = str(index)
        
        print(self.data)


    def updateData(self,dataList):
        for i in self.data["file_data"]:
            # print(self.data["file_data"][i]["title"].lower() , dataList[0].lower())
            if self.data["file_data"][i]["title"].lower() == dataList[0].lower():
                # update the dict
                self.data["file_data"][i] = {"title":dataList[0].capitalize(),"decr":dataList[1].capitalize()}

                print(self.data)
                return
        

    # Return False if the title is alraedy stored else True
    def checkeTitle(self,title):
        data = self.data["file_data"]
        for i in data:
            # removeing extra spaces
            title = " ".join(title.split())

            if data[i]["title"].lower() == title.lower():
                # print("Found it")
                return False

        return True    


    def deleteData(self,title):
        for i in self.data["file_data"]:
            if self.data["file_data"][i]["title"].lower() == title.lower():

                del self.data["file_data"][i]
                self.data["total_file"] = int(self.data["total_file"]) - 1
                print(self.data)
                return
        # del self.data[]

    def storeData(self):
        with open("gaaaw.axx","wb") as f:
            bytes_data = json.dumps(self.data, indent=2).encode('utf-8')
            encrypt_data = self.encrypy(data=bytes_data)
            f.write(encrypt_data)
    
    def getData(self):
        return self.data


    @staticmethod
    def GenRandomKey():
        charList = []
        charList.extend(string.ascii_lowercase)
        charList.extend(string.ascii_uppercase)
        shuffle(charList)
        key = "".join(charList[:8])
        
        return key







if __name__ == "__main__":
    # HandelData().checkeTitle("This is a title")
    # a = HandelData()
    # a.saveData(["title9999","this is a title999"])
    # # a.deleteData("title112sad")
    # a.storeData()
    # # a.GenRandomKey()
    
    b = PassData()
    print(b.getData())
    # -542630838