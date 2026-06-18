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
    let n1 = read_int();
    let n2 = read_int();
    let mut first: Vec<String> = vec![];
    let mut second: Vec<String> = vec![];
    for i in 0..n1 {
        first.push(read_string());
    }
    for i in 0..n2 {
        second.push(read_string());
    }
    for i in 0..n1 {
        for j in 0..n2 {
            println!("{} as {}", first[i as usize], second[j as usize]);
        }
    }
}