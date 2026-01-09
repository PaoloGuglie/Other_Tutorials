// Variables, by default are not allowed to change.
// Constants also aren't, but they are different:
//   - they don't allow the use of "mut"
//   - They should have capital letters
//   - I have to add the type annotation
//   - I can declare them in global scope

fn main()
{
    const Y: i8 = 20;

    println!("{}", Y);
}