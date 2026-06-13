fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let r = read_int();
    let g = read_int();
    let b = read_int();

    // Calculate total cost
    let total_cost = (r * 3) + (g * 4) + (b * 5);
    println!("{}", total_cost);
}
