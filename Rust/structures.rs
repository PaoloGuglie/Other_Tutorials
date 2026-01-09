// STRUCTURES are similar to tuples, but each element
// is named.

struct User
{
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64
}

fn main()
{
    let _rect: (i32, i32) = (200, 500);

    let user1: User = User
    {
        active: true,
        username: String::from("SomeUsername"),
        email: String::from("something@m.com"),
        sign_in_count: 1
    };
    println!("The username is {}", user1.username);

    let user2: User = build_user(String::from("aa"), String::from("bb"));
    println!("The email is {}", user2.email);
}

// This is a builder function
fn build_user(username: String, email: String) -> User
{
    User {active: true, username,
        email, sign_in_count: 1}
}