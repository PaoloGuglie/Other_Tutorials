// Expression: anything that returns a value.
// Statement: anything that doesn't return a value.

fn main()
{
    // x will be equal to price * qty, the last
    // line (without semicolon).
    // I can also do:
    //     return price * qty;
    let x = {
        let price: i32 = 5;
        let qty: i32 = 10;
        price * qty
    };

    println!("Result is {}", x);
}