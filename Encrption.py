from cryptography.fernet import Fernet


class Encrypt:
    # global key for Encryption and decryption
    # iuFXgJButnhpWkFT4Q8PPCdAbQsfndh2XWVbMFYC164=
    
    def init(self,key):

        self.key = key
        self.fernet = Fernet(self.key)
        

    # Function for encrypt data
    def encrypy(self,saveFile=None,data=bytes):
        # if the data is not in bytes format than throw a type error
        if type(data) != bytes:
            raise TypeError("Data must be bytes")

        # encrypt the data
        encryptedData = self.fernet.encrypt(data)

        # save the encrypt text if saveFile is given
        if saveFile != None:
            try:

                with open(saveFile, 'wb') as encrypted_file:
                    encrypted_file.write(encryptedData)

            except Exception as e:
                print(e)
        
        return encryptedData
        


    def decrypt(self,saveFilePath=None,data=bytes):

        # if the data is not in bytes format than throw a type error
        if type(data) != bytes:
            raise TypeError("Data must be bytes")
            
        # decrypt the data
        decrypted = self.fernet.decrypt(data)

        # save the decrypt text if saveFile is given
        if saveFilePath != None:
            try:
                with open(saveFilePath, 'wb') as encrypted_file:
                    encrypted_file.write(decrypted)
            except Exception as e:
                print(e)


        else:
            return decrypted





if __name__ == "__main__":

    test = Encrypt()
    data = test.encrypy("text.txt",b'this is a test')
    test = Encrypt().decrypt(saveFilePath="text.txt",data=data)

# test = Encrypt().removeAll()