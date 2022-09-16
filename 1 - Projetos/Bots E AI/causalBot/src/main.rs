

enum Direction{
    Up,
    Down,
    Left,
    Right
}
fn main() {
    let mut x: u64=10;
    let f: f64 = 6.7;
    let b: bool = false;
    let mut n = 0;
    let  player_direction:Direction = Direction::Up;

    match player_direction{

    }
    loop{
        n+=1;
    println!("Hello, world! n is {}",n);

        if n >10{
            break;
        }
    }
    
    while n <5{
    println!("Hello, world! n is {}",n);

        n+=1;
    }
    for n in 1..11{
    println!("Hello, world! n is {}",n);

    }

    let range = 2..7;
    for a in range{
    println!("Hello, world! a is {}",a);

    }

    let animals = vec!["dog", "cat"];

    for a in animals{
    println!("Hello, world! a is {}",a);

    }
    /*for (index, a) in animals.iter().enumerate(){
        println!("Hello, world! {} is the {} animal",index, a);

    }*/
    println!("Hello, world! x is {}",x);
    x = 60;
    if x<30{

    }else if x>30{

    }else{

    }
}


