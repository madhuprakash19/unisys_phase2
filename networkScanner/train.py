import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import smtplib, ssl  

def email(ip):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = [ADD SENDER EMAIL IN DOUBLE QUOTES]
    receiver_email = [ADD RECEIVER EMAIL IN DOUBLE QUOTES]
    password = [ADD SENDER GMAIL PASSWORD TO SEND MAIL IN DOUBLE QUOTES]
    message = "Your system is in danger.There is a flood attack .Instructing MCP to block "+ip+" addresss."
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message) 
        print("Email sent successfully")


colnames = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","una1","una2","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","ip_address","result"]
df = pd.read_csv("dataSet.csv",header=None,names=colnames)
#print(df)
def train_icmp(df, classifier=1):
    """
    Only two best classifiers have been employed on these datasets
    """
    icmp_df = df[df.loc[:,"protocol_type"] == "icmp"]
    icmp_features = ["duration","src_bytes","wrong_fragment","count","urgent","num_compromised","srv_count"]
    icmp_target = "result"
    X = icmp_df.loc[:,icmp_features]
    y = icmp_df.loc[:,icmp_target]
    ip=df.loc[100010,'ip_address']
    classes = np.unique(y)
    for i in range(len(classes)):
        if i == 2:
            icmp_df = icmp_df.replace(classes[i], 0)
        else:
            icmp_df = icmp_df.replace(classes[i], 1)
    y = icmp_df.loc[:,icmp_target] #updating the y variables
    print("Data preprocessing done.")
    
    #choose KNN if classifier == 1 else choose Decision Tree
    if str(classifier) == "1":
        k = 3
        model = KNeighborsClassifier(n_neighbors=k)
    elif str(classifier) == "2":
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
    else:
        print("Wrong model chosen! Placing default model 0 to model training!")
        k = 3
        model = KNeighborsClassifier(n_neighbors=k)
    
    
    #fitting our model
    model.fit(X,y)
    print("The model has been fit.")
    
    print("Save the fitted model?(y/n):")
    choice = input().lower()
    if choice == "y":
        li=list(map(float,input("Send attributes for testing the system ").split()))
        result = model.predict([li])
        if(result==0):
            print("Normal")
        else:
            print("ICMP Flood attack")
            email(ip)
if __name__ == "__main__":
    print("1.KNN\n2.Desicion tree")
    ch=int(input("Enter choice: "))
    train_icmp(df,ch)
