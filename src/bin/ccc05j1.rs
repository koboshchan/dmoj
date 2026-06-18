fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn main() {
    let daytime = read_int();
    let evening = read_int();
    let weekend = read_int();
    let mut plan_a = ((daytime - 100).max(0) as f64) * 0.25 + (evening as f64) * 0.15 + (weekend as f64) * 0.20;
    let mut plan_b = ((daytime - 250).max(0) as f64) * 0.45 + (evening as f64) * 0.35 + (weekend as f64) * 0.25;
    plan_a = (plan_a * 100.0).round() / 100.0;
    plan_b = (plan_b * 100.0).round() / 100.0;
    println!("Plan A costs {:.2}", plan_a);
    println!("Plan B costs {:.2}", plan_b);
    if plan_a < plan_b {
        println!("Plan A is cheapest.");
    } else if plan_b < plan_a {
        println!("Plan B is cheapest.")
    } else {
        println!("Plan A and B are the same price.");
    }
}