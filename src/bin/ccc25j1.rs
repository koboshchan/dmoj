fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let n = read_int();
    let c = read_int();
    let p = read_int();
    let total_seats = c * p;
    if n <= total_seats {
        println!("yes");
    } else {
        println!("no");
    }
}