fn read_int() -> i32 {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    input.trim().parse().expect("Input was not a valid number")
}

fn read_string() -> String {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    input.trim().to_string()
}

fn check_win(alice: String, bob: String) -> bool {
    if alice == "rock" && bob == "scissors" {
        return true;
    } else if alice == "scissors" && bob == "paper" {
        return true;
    } else if alice == "paper" && bob == "rock" {
        return true;
    }
    false
}

fn main() {
    read_int();
    let mut alice: Vec<String> = Vec::new();
    let mut bob: Vec<String> = Vec::new();
    let alice_input = read_string();
    let bob_input = read_string();
    for name in alice_input.split_whitespace() {
        alice.push(name.to_string());
    }
    for name in bob_input.split_whitespace() {
        bob.push(name.to_string());
    }

    let mut alice_wins = 0;
    let mut bob_wins = 0;

    for (index, value) in alice.iter().enumerate() {
        if check_win(value.to_string(), bob[index].to_string()) {
            alice_wins += 1;
        } else if check_win(bob[index].to_string(), value.to_string()) {
            bob_wins += 1;
        }
    }
    println!("{} {}", alice_wins, bob_wins);
}
