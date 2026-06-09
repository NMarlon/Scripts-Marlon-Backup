
fn main(){
	println!("Hello, World!");
}

struct Megaman {
    conhecimento: [[i32; 2]; 100],
    atuadores: [[i32; 2]; 10],
}


// Definindo a struct interna que será colocada dentro da array bidimensional
struct Ponto {
    x: i32,
    y: i32,
}

// Definindo a struct externa que contém a array bidimensional de Pontos
struct Espaco {
    space: [[Ponto; 3]; 3], // Exemplo de uma array 3x3 de Pontos
}

fn main() {
    // Criando uma instância da struct Espaco
    let mut meu_espaco = Espaco {
        space: [[Ponto { x: 0, y: 0 }; 3]; 3], // Inicializando todos os Pontos com (0, 0)
    };

    // Atribuindo valores a alguns pontos na array bidimensional
    meu_espaco.space[0][0] = Ponto { x: 1, y: 2 };
    meu_espaco.space[1][1] = Ponto { x: 3, y: 4 };
    meu_espaco.space[2][2] = Ponto { x: 5, y: 6 };

    // Imprimindo os valores dos pontos na array bidimensional
    for row in &meu_espaco.space {
        for ponto in row {
            println!("Ponto: x = {}, y = {}", ponto.x, ponto.y);
        }
    }
}


// https://www.youtube.com/watch?v=MsocPEZBd-M&ab_channel=freeCodeCamp.org