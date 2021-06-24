from sys import*

def main():
    print("--------Welcome----------")
    print("Script title : "+argv[0])
    
    if(len(argv)!=2):
        print("Insufficient argument to the script")
        exit()
        
    if(argv[1] == "-u"):
        print("Use the Script as Name.py parameters")
        
    if(argv[1] == "-h") or (argv[1] == "-U"):
        print("This is demo automation script")
if __name__ == "__main__":
    main()
    
    
 #SCRIPT FLAG:-
 
 1)-U(usage) : When User don't know how to use script command then Usage used(-u)...in this we can write kas use karayach
 2)-h(help) :  when user used first time script then used help...in this we can write ti sript kay karanar aahe 