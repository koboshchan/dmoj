use std::collections::HashMap;

fn read_string() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().to_string()
}

fn main() {
    let finger_combinations = HashMap::from([
        ("1", 1),  // 1
        ("2", 2),  // 2, 1+1
        ("3", 2),  // 3, 2+1
        ("4", 3),  // 4, 3+1, 2+2
        ("5", 3),  // 5, 4+1, 3+2
        ("6", 3),  // 5+1, 4+2, 3+3
        ("7", 2),  // 5+2, 4+3
        ("8", 2),  // 5+3, 4+4
        ("9", 1),  // 5+4
        ("10", 1), // 5+5
    ]);

    let input = read_string();
    println!("{}", finger_combinations.get(input.as_str()).unwrap());
}