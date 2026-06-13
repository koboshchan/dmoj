use std::collections::HashMap;

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

fn main() {
    let ascii_digits: HashMap<i32, Vec<&str>> = HashMap::from([
        (
            0,
            vec![
                " * * * ", "*     *", "*     *", "*     *", "       ", "*     *", "*     *",
                "*     *", " * * * ",
            ],
        ),
        (
            1,
            vec![
                "       ", "      *", "      *", "      *", "       ", "      *", "      *",
                "      *", "       ",
            ],
        ),
        (
            2,
            vec![
                " * * * ", "      *", "      *", "      *", " * * * ", "*      ", "*      ",
                "*      ", " * * * ",
            ],
        ),
        (
            3,
            vec![
                " * * * ", "      *", "      *", "      *", " * * * ", "      *", "      *",
                "      *", " * * * ",
            ],
        ),
        (
            4,
            vec![
                "       ", "*     *", "*     *", "*     *", " * * * ", "      *", "      *",
                "      *", "       ",
            ],
        ),
        (
            5,
            vec![
                " * * * ", "*      ", "*      ", "*      ", " * * * ", "      *", "      *",
                "      *", " * * * ",
            ],
        ),
        (
            6,
            vec![
                " * * * ", "*      ", "*      ", "*      ", " * * * ", "*     *", "*     *",
                "*     *", " * * * ",
            ],
        ),
        (
            7,
            vec![
                " * * * ", "      *", "      *", "      *", "       ", "      *", "      *",
                "      *", "       ",
            ],
        ),
        (
            8,
            vec![
                " * * * ", "*     *", "*     *", "*     *", " * * * ", "*     *", "*     *",
                "*     *", " * * * ",
            ],
        ),
        (
            9,
            vec![
                " * * * ", "*     *", "*     *", "*     *", " * * * ", "      *", "      *",
                "      *", " * * * ",
            ],
        ),
    ]);
    let n = read_int();
    let mut input: Vec<String> = vec![];
    for _ in 0..n {
        input.push(read_string());
    }
    for (i, value) in input.iter().enumerate() {
        let mut out: Vec<String> = vec!["".to_string(); 9];
        for c in value.chars() {
            let digit = c.to_digit(10).unwrap() as i32;
            let ascii_representation = ascii_digits.get(&digit).unwrap();
            for (index, line) in ascii_representation.iter().enumerate() {
                out[index].push_str(line);
                out[index].push_str(" ");
            }
        }
        for (index, line) in out.iter().enumerate() {
            if index == out.len() - 1 {
                print!("{}", line.trim_end());
                continue;
            }
            println!("{}", line.trim_end());
        }
        if i != input.len() - 1 {
            print!("\n\n");
        }
    }
    if n != 0 {
        print!("\n")
    }
}
