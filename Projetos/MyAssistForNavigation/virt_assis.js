


class my_assistent_bot{
  constructor(memoria) {//height
    //prolog, scripts
    ijct_script("https://gist-it.appspot.com/https://github.com/NMarlon/tau-prolog/tree/master/modules/core.js");
    ijct_script("https://gist-it.appspot.com/https://github.com/NMarlon/tau-prolog/tree/master/modules/dom.js");
    this.memoria={};


    //talvez precise do eval("coisas aqui") mas é melhor evitar se possível. 
   //this.height = height;
  }

     bot_conversa(resposta){
        return prompt(resposta);
    }


     my_assistent_bot(){
        var fala_do_usuario= bot_conversa("Olá! Bem-vindo ao bot JS. Um assitente virtual! Digite o que procura");
        if(fala_do_usuario==""){

        }else {
          this.memoria[bot_conversa("Desculpe eu não entendi. Palavra reservada, vou assoaciar à  Você pode: \r\n 1 - Ver outras alternativas \r\n 2 - voltar pra revisar outra forma de uso \r\n 3 - Aplicar isso mesmo nisso.")]=Promisse((resposta)=>{
            
          });
            
        }

    }   

}

p =new Promise((resolve, reject)  =>{
try{

}catch(e){
  console.log
}
})

                      

var start_assistent = new my_assistent_bot();

/*
let Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
*/

