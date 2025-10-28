print("___________info_store_____________")
info_username={}
Sing_in=True
loan_history={}
def sing_in_process():
    global Sing_in
    if len(info_username)==0:
        enter_username=input("enter a username:")
        enter_passward=input("enter a passward:")
        if len(enter_username)<=4 and len(enter_passward)<=4:
            print("enter atlest 6 char")
        else :
            import random
            genrate=str(random.randint(100000,111111))
            user_id="M12024"+genrate
            info_username[enter_username]=(enter_passward,user_id)
            print("login sussesful")
            Enter_KYC_Document()
            return enter_username       
    else:   
        while Sing_in:
            enter_username=input("enter a username1:")
            enter_passward=input("enter a passward:")
            for key in info_username:
                if key==enter_username:
                    print("enter differet username")
                    break
            else:
                import random
                genrate=str(random.randint(100000,111111))
                            
                user_id="M12024"+genrate
                info_username[enter_username]=(enter_passward,user_id)
                print(info_username)
                print("account login susesful")                
                return enter_username
                

def login_process():
    global Sing_in
    while Sing_in:
        enter_username=input("enter a username:")
        enter_passward=input("enter a passward:")
        if enter_username in info_username:
            if info_username[enter_username][0]==enter_passward:
                print("login sussesful")
                show_Credit_limit(user)
                Sing_in=False
            else:
                print("wrong passward")
                reset=input("forgot passward:")
                if reset.lower() == "yes":
                    import random
                    OTP= random.randint(1111,9999)
                    print(OTP)
                    ENTER=int(input("enter otp"))
                    if ENTER==OTP:
                        print("login sussesful")
                        show_Credit_limit(user)                                                                        
        else:
            print("wrong username")
                       
def Enter_KYC_Document():
    details=True
    while details:
        print("ENTER YOUR KYC DETAILS")
        name=input("enter name: ")
        if name.replace(" ","").isalpha():    
            age=int(input("enter a age: "))
            Pan_card=int(input("enter pan no: "))
            adhar_card=int(input("enter adhar no: "))
            mobile_no=int(input("enter mobile no: "))
            print("kyc complete sussesful")
            details=False
        else:
            print("enter only letter not special charchater")
def show_Credit_limit(user):
        if user in loan_history:
           credit_limit=loan_history[user]
           print("your credit limit is",credit_limit)
           loan_amount=int(input("enter a amount"))
           if loan_amount >credit_limit:
                print("not credit limit avaliable")              
        else:
            loan_history[user]=1000
            print("your credit limit is","1000")
            
sing_in_process()
login_process()
Enter_KYC_Document()  
show_Credit_limit(enter_username) 
    
    
    
    
    
    




        
        
    
        
        
                       
                
        
    
                
        
    
