fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let n = read_int();
    for i in 1..=n {
        println!("{} X {} = {}", n,i, n*i);
    }
}