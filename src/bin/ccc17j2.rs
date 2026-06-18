fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let start = read_int();
    let mut out = start.clone();
    let times = read_int();
    for i in 0..times {
        out += ((start.to_string() + "").clone() + &"0".repeat((i+1) as usize)).parse::<i32>().unwrap();
    }
    println!("{}", out);
}