

function c(content){
    return console.log(content);
}


function t(){
    console.trace();
}
function ln() {
  var e = new Error();
  if (!e.stack) try {
    // IE requires the Error to actually be throw or else the Error's 'stack'
    // property is undefined.
    throw e;
  } catch (e) {
    if (!e.stack) {
      return 0; // IE < 10, likely
    }
  }
  var stack = e.stack.toString().split(/\r\n|\n/);
  // We want our caller's frame. It's index into |stack| depends on the
  // browser and browser version, so we need to search for the second frame:
  var frameRE = /:(\d+):(?:\d+)[^\d]*$/;
  do {
    var frame = stack.shift();
  } while (!frameRE.exec(frame) && stack.length);
  return frameRE.exec(stack.shift())[1];
}


function debug_mode(key)
{  if(key!="teste"){
        return null;
    }
            //Coloque o código aqui
}


 var t_cel,tc_ln;
 if(document.addEventListener){ //code for Moz
   document.addEventListener("keydown",keyCapt,false); 
   /*document.addEventListener("keyup",keyCapt,false);
   document.addEventListener("keypress",keyCapt,false);*/
 }else{
   document.attachEvent("onkeydown",keyCapt); //code for IE
   /*document.attachEvent("onkeyup",keyCapt); 
   document.attachEvent("onkeypress",keyCapt); */
 }
 function keyCapt(e){
   if(typeof window.event!="undefined"){
    e=window.event;//code for IE
   }
   if(e.type=="keydown"){
   // t_cel[0].innerHTML=e.keyCode;
    if(e.keyCode == 120 ){


        var debug_mode = prompt('Olá! Seja bem vindo à Semana da Educacao 2021! Deseja ver nosso site oficial?');
        if(debug_mode=="teste"){
            debug_mode(debug_mode);
        }else{
            if(confirm("Ok! Você será redirecionado para https://autossuficiencia.org")){
                window.location.href="https://autossuficiencia.org";
            }
        }
    }
   }/*else if(e.type=="keyup"){
   }else if(e.type=="keypress"){
   }*/
 }

//console.log(getCookie("id_ref")+" id AQUI");
//https://stackoverflow.com/questions/424407/handling-key-press-events-f1-f12-using-javascript-and-jquery-cross-browser