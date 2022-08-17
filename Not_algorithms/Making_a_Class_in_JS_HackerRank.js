// Classes
class Account{
    
  constructor(balance){
      this.balance = balance
  }
  
  debit(amount){
      if (amount > this.balance) console.log("Insufficient balance")
      else {
          this.balance -= amount
          console.log(amount + " debited")
      }
  }
  
  getBalance(){
      return console.log(this.balance)
  }
  
  credit(amount){
      this.balance += amount
      console.log(amount + " credited")
  }
}

let testing = new Account(1000)
testing.debit(112)
testing.credit(132)
testing.getBalance()
