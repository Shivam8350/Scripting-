import psutil
from sys import *

def ProcessDisplay():
    print("List of running processess")
    
    Data = []
    
    for proc in psutil.process_iter():   #process_iter is ysed run honarya every process chi information dete
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    return Data
    
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])

    arr = ProcessDisplay()
    for element in arr:
        print(element)
        
if __name__ == "__main__":
    main()
    
#https://us02st1.zoom.us/web_client/sjstu3/html/externalLinkPage.html?ref=https://psutil.readthedocs.io/en/latest/#:~:text=psutil%252520(python%252520system%252520and%252520process,the%252520management%252520of%252520running%252520processes.