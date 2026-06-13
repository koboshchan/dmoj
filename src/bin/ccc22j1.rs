fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let regular = read_int();
    let small = read_int();
    let leftover = (regular*8 + small*3) - 28;
    println!("{}", leftover);
}