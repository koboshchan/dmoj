fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let p = read_int();
    let c = read_int();
    let mut point = 0;

    point += p * 50;
    point -= c * 10;

    if p>c {
        point += 500;
    }

    println!("{}", point);
}