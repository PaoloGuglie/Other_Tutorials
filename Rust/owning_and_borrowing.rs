// OWNERSHIP: every value has a single owner.
// BORROWING: temporary borrow references to values.
// enables concurrent access in a safe way.

// When I borrow without using "mut", the reference
// cannot modify the original value.
// I can have 1 mutable reference or any number of
// immutable references.

fn main()
{
    let mut account: BankAccount = BankAccount {
        owner: "Alice".to_string(),
        balance: 150.55 };

    // Immutable borrow to check the balance
    account.check_balance();

    // Mutable borrow to withdraw money
    account.withdraw(60.00);

    account.check_balance();
}

struct BankAccount
{
    owner: String,
    balance: f64
}

impl BankAccount
{
    fn withdraw(&mut self, amount: f64)
    {
        println!("Withdrawing {:.2} from account owned by {}",
        amount, self.owner);
        self.balance -= amount;
    }

    fn check_balance(&self)
    {
        println!("Account owned by {} has a balance of {:.2}",
        self.owner, self.balance);
    }
}