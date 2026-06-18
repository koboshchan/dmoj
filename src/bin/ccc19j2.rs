fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn read_string() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().to_string()
}

fn main() {
    let n = read_int();
    for _ in 0..n {
        let words = read_string();
        let times = words.split_whitespace().collect::<Vec<&str>>()[0].parse::<i32>().unwrap();
        let word = words.split_whitespace().collect::<Vec<&str>>()[1];
        for _ in 0..times {
            print!("{}", word);
        }
        print!("\n");
    }
}