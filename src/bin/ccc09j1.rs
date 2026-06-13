fn read_string() -> String {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    input.trim().to_string()
}

fn main() {
    let mut isbn = "9780921418".to_string();
    isbn.push_str(&read_string());
    isbn.push_str(&read_string());
    isbn.push_str(&read_string());
    // calculate the checksum
    let mut sum = 0;
    let mut current = 1; // 1 or 3
    for c in isbn.chars() {
        if current == 1 {
            sum += c.to_digit(10).unwrap();
            current = 3;
        } else {
            sum += 3 * c.to_digit(10).unwrap();
            current = 1;
        }
    }
    println!("The 1-3-sum is {}", sum.to_string());
}
