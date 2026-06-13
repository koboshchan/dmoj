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
    let c = read_int();
    let mut c_fih: Vec<i32> = vec![];
    for _ in 0..c {
        let str_read = read_string();
        let tmp: Vec<&str> = str_read.split_whitespace().collect();
        c_fih.push(tmp[0].parse::<i32>().unwrap() * tmp[1].parse::<i32>().unwrap());
    }
    let n = read_int();
    let mut n_fih: Vec<i32> = vec![];
    for _ in 0..n {
        let str_read = read_string();
        let tmp: Vec<&str> = str_read.split_whitespace().collect();
        n_fih.push(tmp[0].parse::<i32>().unwrap() * tmp[1].parse::<i32>().unwrap());
    }
    let c_max = c_fih.iter().max().unwrap();
    let n_max = n_fih.iter().max().unwrap();
    if c_max > n_max {
        println!("Casper");
    } else if c_max < n_max {
        println!("Natalie");
    } else {
        println!("Tie");
    }
}