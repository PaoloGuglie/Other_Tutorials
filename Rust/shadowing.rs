// In Rust, SHADOWING allows me to redeclare a variable
// with the same name, replacing the previous one.
// I can also shadow with a different type.

fn main()
{
    let x: i32 = 5;
    let x = x + 1;
    println!("x is {}", x);

    // Different type
    let str: &str = "hello";
    let str: usize = str.len();
    println!("str is {}", str);
}