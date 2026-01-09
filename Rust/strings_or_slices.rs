// STACK: quicker, can't have mutable data types
// HEAP: slower, can have mutable data types

fn main()
{
    // STRING: stored in the heap
    // It can grow, mute, owned type
    let mut stone: String = String::from("Hell, ");
    println!("Stone says: {}", stone);

    stone.push_str("Yeah!");
    println!("Stone says: {}", stone);

    // STRING SLICE: stored in the stack
    // It's a reference, reference type to a string
    // stored somewhere in my code. It's immutable.
    let my_string: String = String::from("Hell!");
    
    let full_string: &str = &my_string;
    println!("My string is: {}", full_string);

    let slice_string: &str = &my_string[0..2];
    println!("My slice is: {}", slice_string);
}