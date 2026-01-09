// VECTORS

fn main()
{
    let mut v: Vec<i32> = Vec::new();

    v.push(4);
    v.push(5);

    for i in v
    {
        println!("{i}");
    }

    println!("-----------");

    let v2: Vec<char> = vec!['a', 'b', 'c'];

    // TBH having to pass a reference to the vector
    // for it not to be "consumed" by this iteration
    // looks like some real BullShit!
    for i in &v2
    {
        println!("{i}");
    }

    println!("--------------");

    // To retain a value without taking ownership
    let second: &char = &v2[1];
    println!("Second value is {second}.");

}