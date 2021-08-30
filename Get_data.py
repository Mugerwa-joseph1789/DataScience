import pandas as pd
#getting data from excel files
df=pd.read_excel("G2.xlsx")

#making a copy oof the dataframe
c=df.copy
print(c["PHONE NUMBER"])

#removing fullstops from the account numbers
c["ACCOUNT NUMBER"]=[_.replace(".","") for _ in c["ACCOUNT NUMBER"]]

#creating a new column that randomly generates payment status
c["P_STATUS"]=[choice(["Paid","Not paid"]) for _ in c["STUDENT NAMES"]]

#turning our dataframe into an excel file
c.to_excel("Copy_made.xlsx",sheet_name="status")

#view all columns and rows
pd.set_option('display.max_columns',999)

#generate random Amounts of salaries
df["AMOUNT"]=[random.randint(315000,760000) for _ in df["COURSE"]]

#calculating the 95th percentile salary
p=sorted(df["AMOUNT"])
print(p[int(.95*len(p))])

#calculating percentage of of total money that wasnt paid
r=[_for _ in df["PAID"]]
g=[_ for _ in df["AMOUNT"]]
f=zip(r,g)
d=list(f)
new=[list(_) for _ in d]
percentage=(sum(_[1] for _ in g if _[0]=="NOT PAID")/sum(df["AMOUNT"]))*100

#calculating percentage number of students who recieved their money
s_r=[_ for _ in df["PAID"] if _=="PAID"]
Per_pay=(len(s_r)/len(df["PAID"]))*100



