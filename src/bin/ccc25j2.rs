fn read_string() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().to_string()
}

fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let mut donuts = read_int();
    let events = read_int();

    for i in 0..events {
        let event_type = read_string();
        let event_value = read_int();
        if event_type == "+" {
            donuts += event_value;
        } else if event_type == "-" {
            donuts -= event_value;
        }
    }
    println!("{}", donuts);
}