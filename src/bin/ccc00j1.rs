// fn read_string() -> String {
//     let mut input = String::new();
//     std::io::stdin()
//         .read_line(&mut input)
//         .expect("Failed to read line");
//     input.trim().to_string()
// }

// fn main() {
//     let inp: String = read_string();
//     let dat = inp.split_ascii_whitespace().collect::<Vec<&str>>();
//     let start = dat[0].parse::<i32>().unwrap()-1;
//     let days = dat[1].parse::<i32>().unwrap();
//     let mut colum = start;
//     println!("Sun Mon Tue Wed Thr Fri Sat");
//     if start != 0 {
//         print!("{}", " ".repeat(((start) * 4 - 1) as usize));
//     }

//     for i in 1..=days {
//         if colum == 0 {
//             print!("{: >3}", i);
//         } else {
//             print!("{: >4}", i);
//         }
//         colum += 1;
//         if colum == 7 {
//             print!("\n");
//             colum = 0;
//         }
//     }
//     if colum != 0 {
//         print!("\n");
//     }
// }

fn read_string() -> String {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    input.trim().to_string()
}

fn main() {
    let input = read_string();
    let mut parts = input.split_whitespace();
    
    // Parse the inputs into integers
    let n: i32 = parts.next().unwrap().parse().unwrap();
    let day: i32 = parts.next().unwrap().parse().unwrap();

    println!("Sun Mon Tue Wed Thr Fri Sat");

    // 28 Days
    if n == 1 && day == 28 {
        println!("  1   2   3   4   5   6   7");
        println!("  8   9  10  11  12  13  14");
        println!(" 15  16  17  18  19  20  21");
        println!(" 22  23  24  25  26  27  28");
    }
    if n == 2 && day == 28 {
        println!("      1   2   3   4   5   6");
        println!("  7   8   9  10  11  12  13");
        println!(" 14  15  16  17  18  19  20");
        println!(" 21  22  23  24  25  26  27");
        println!(" 28");
    }
    if n == 3 && day == 28 {
        println!("          1   2   3   4   5");
        println!("  6   7   8   9  10  11  12");
        println!(" 13  14  15  16  17  18  19");
        println!(" 20  21  22  23  24  25  26");
        println!(" 27  28");
    }
    if n == 4 && day == 28 {
        println!("              1   2   3   4");
        println!("  5   6   7   8   9  10  11");
        println!(" 12  13  14  15  16  17  18");
        println!(" 19  20  21  22  23  24  25");
        println!(" 26  27  28");
    }
    if n == 5 && day == 28 {
        println!("                  1   2   3");
        println!("  4   5   6   7   8   9  10");
        println!(" 11  12  13  14  15  16  17");
        println!(" 18  19  20  21  22  23  24");
        println!(" 25  26  27  28");
    }
    if n == 6 && day == 28 {
        println!("                      1   2");
        println!("  3   4   5   6   7   8   9");
        println!(" 10  11  12  13  14  15  16");
        println!(" 17  18  19  20  21  22  23");
        println!(" 24  25  26  27  28");
    }
    if n == 7 && day == 28 {
        println!("                          1");
        println!("  2   3   4   5   6   7   8");
        println!("  9  10  11  12  13  14  15");
        println!(" 16  17  18  19  20  21  22");
        println!(" 23  24  25  26  27  28");
    }

    // 29 Days
    if n == 1 && day == 29 {
        println!("  1   2   3   4   5   6   7");
        println!("  8   9  10  11  12  13  14");
        println!(" 15  16  17  18  19  20  21");
        println!(" 22  23  24  25  26  27  28");
        println!(" 29");
    }
    if n == 2 && day == 29 {
        println!("      1   2   3   4   5   6");
        println!("  7   8   9  10  11  12  13");
        println!(" 14  15  16  17  18  19  20");
        println!(" 21  22  23  24  25  26  27");
        println!(" 28  29");
    }
    if n == 3 && day == 29 {
        println!("          1   2   3   4   5");
        println!("  6   7   8   9  10  11  12");
        println!(" 13  14  15  16  17  18  19");
        println!(" 20  21  22  23  24  25  26");
        println!(" 27  28  29");
    }
    if n == 4 && day == 29 {
        println!("              1   2   3   4");
        println!("  5   6   7   8   9  10  11");
        println!(" 12  13  14  15  16  17  18");
        println!(" 19  20  21  22  23  24  25");
        println!(" 26  27  28  29");
    }
    if n == 5 && day == 29 {
        println!("                  1   2   3");
        println!("  4   5   6   7   8   9  10");
        println!(" 11  12  13  14  15  16  17");
        println!(" 18  19  20  21  22  23  24");
        println!(" 25  26  27  28  29");
    }
    if n == 6 && day == 29 {
        println!("                      1   2");
        println!("  3   4   5   6   7   8   9");
        println!(" 10  11  12  13  14  15  16");
        println!(" 17  18  19  20  21  22  23");
        println!(" 24  25  26  27  28  29");
    }
    if n == 7 && day == 29 {
        println!("                          1");
        println!("  2   3   4   5   6   7   8");
        println!("  9  10  11  12  13  14  15");
        println!(" 16  17  18  19  20  21  22");
        println!(" 23  24  25  26  27  28  29");
    }

    // 30 Days
    if n == 1 && day == 30 {
        println!("  1   2   3   4   5   6   7");
        println!("  8   9  10  11  12  13  14");
        println!(" 15  16  17  18  19  20  21");
        println!(" 22  23  24  25  26  27  28");
        println!(" 29  30");
    }
    if n == 2 && day == 30 {
        println!("      1   2   3   4   5   6");
        println!("  7   8   9  10  11  12  13");
        println!(" 14  15  16  17  18  19  20");
        println!(" 21  22  23  24  25  26  27");
        println!(" 28  29  30");
    }
    if n == 3 && day == 30 {
        println!("          1   2   3   4   5");
        println!("  6   7   8   9  10  11  12");
        println!(" 13  14  15  16  17  18  19");
        println!(" 20  21  22  23  24  25  26");
        println!(" 27  28  29  30");
    }
    if n == 4 && day == 30 {
        println!("              1   2   3   4");
        println!("  5   6   7   8   9  10  11");
        println!(" 12  13  14  15  16  17  18");
        println!(" 19  20  21  22  23  24  25");
        println!(" 26  27  28  29  30");
    }
    if n == 5 && day == 30 {
        println!("                  1   2   3");
        println!("  4   5   6   7   8   9  10");
        println!(" 11  12  13  14  15  16  17");
        println!(" 18  19  20  21  22  23  24");
        println!(" 25  26  27  28  29  30");
    }
    if n == 6 && day == 30 {
        println!("                      1   2");
        println!("  3   4   5   6   7   8   9");
        println!(" 10  11  12  13  14  15  16");
        println!(" 17  18  19  20  21  22  23");
        println!(" 24  25  26  27  28  29  30");
    }
    if n == 7 && day == 30 {
        println!("                          1");
        println!("  2   3   4   5   6   7   8");
        println!("  9  10  11  12  13  14  15");
        println!(" 16  17  18  19  20  21  22");
        println!(" 23  24  25  26  27  28  29");
        println!(" 30");
    }

    // 31 Days
    if n == 1 && day == 31 {
        println!("  1   2   3   4   5   6   7");
        println!("  8   9  10  11  12  13  14");
        println!(" 15  16  17  18  19  20  21");
        println!(" 22  23  24  25  26  27  28");
        println!(" 29  30  31");
    }
    if n == 2 && day == 31 {
        println!("      1   2   3   4   5   6");
        println!("  7   8   9  10  11  12  13");
        println!(" 14  15  16  17  18  19  20");
        println!(" 21  22  23  24  25  26  27");
        println!(" 28  29  30  31");
    }
    if n == 3 && day == 31 {
        println!("          1   2   3   4   5");
        println!("  6   7   8   9  10  11  12");
        println!(" 13  14  15  16  17  18  19");
        println!(" 20  21  22  23  24  25  26");
        println!(" 27  28  29  30  31");
    }
    if n == 4 && day == 31 {
        println!("              1   2   3   4");
        println!("  5   6   7   8   9  10  11");
        println!(" 12  13  14  15  16  17  18");
        println!(" 19  20  21  22  23  24  25");
        println!(" 26  27  28  29  30  31");
    }
    if n == 5 && day == 31 {
        println!("                  1   2   3");
        println!("  4   5   6   7   8   9  10");
        println!(" 11  12  13  14  15  16  17");
        println!(" 18  19  20  21  22  23  24");
        println!(" 25  26  27  28  29  30  31");
    }
    if n == 6 && day == 31 {
        println!("                      1   2");
        println!("  3   4   5   6   7   8   9");
        println!(" 10  11  12  13  14  15  16");
        println!(" 17  18  19  20  21  22  23");
        println!(" 24  25  26  27  28  29  30");
        println!(" 31");
    }
    if n == 7 && day == 31 {
        println!("                          1");
        println!("  2   3   4   5   6   7   8");
        println!("  9  10  11  12  13  14  15");
        println!(" 16  17  18  19  20  21  22");
        println!(" 23  24  25  26  27  28  29");
        println!(" 30  31");
    }
}