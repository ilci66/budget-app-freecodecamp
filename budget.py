class Category:
  def __init__(self, name):
    self.name=name
    self.ledger=[]
    self.funds=0

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    self.funds+=amount

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})

      self.funds-=amount
      return True
    return False

  def get_balance(self):
    return self.funds

  def transfer(self, amount, other):
    if not self.check_funds(amount):
      return False

    self.ledger.append({'amount':-amount,'description':"Transfer to {}".format(other.name)})
    self.funds-=amount

    other.ledger.append({"amount": amount, "description":"Transfer from {}".format(self.name)})
    other.funds+=amount

    return True

  def check_funds(self, amount):
    if self.funds>=amount:
      return True
    return False

  def __str__(self):
    s=''
    s+=self.name.center(30,'*')+'\n'
    for x in self.ledger:
      if len(x['description'])>23:
        s+=x['description'][0:23]
      else:
        s+=x['description'][0:23].ljust(23)
      s+="{0:.2f}".format(x['amount']).rjust(7)
      s+='\n'
    s+='Total: {}'.format(self.funds)
    return s
            

def create_spend_chart(categories):
  s="Percentage spent by category\n"
  sum=0
  withdraws={}
  for x in categories:
    withdraws[x.name]=0
    for y in x.ledger:
      if y['amount']<0:
        withdraws[x.name]+=y['amount']
    withdraws[x.name]=-withdraws[x.name]

  for x in withdraws:
    sum+=withdraws[x]

  for x in withdraws:
    withdraws[x]=int(withdraws[x]/sum*100)
      
  for i in range(100,-10,-10):
    s+=str(i).rjust(3)+'| '
    for x in categories:
      if withdraws[x.name]>=i:
          s+='o  '
      else:
          s+='   '
    s+='\n'
  s+=' '*4+'-'*(1+len(categories)*3)+'\n'

  maxlen=0
  for x in categories:
    if len(x.name)>maxlen:
      maxlen=len(x.name)

  for i in range(maxlen):
    s+=' '*5
    for x in categories:
      if len(x.name)>i:
        s+=x.name[i]+'  '
      else:
        s+=' '*3
    s+='\n'
  return s[0:-1]

