//http://gist-it.appspot.com/?COLOQUE AQUI O LINK DO GITHUB COM O ARQUIVO
//http://gist-it.appspot.com/https://github.com/tau-prolog/tau-prolog/tree/master/modules/core.js
//http://gist-it.appspot.com/...


/*
//Kit Básico pra jQuery 


function isMyScriptLoaded(url) {
    if (!url) url = "http://xxx.co.uk/xxx/script.js";
    var scripts = document.getElementsByTagName('script');
    for (var i = scripts.length; i--;) {
        if (scripts[i].src == url) return true;
    }
    return false;
}

function ijct_script(script_link){//Injeta scripts na página. script_link = link com .js pra injetar
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.onload = function() {
        //ACrescente a função do script aqui
    }
    script.src = script_link;
    if(!isMyScriptLoaded(script_link)){// pra evitar colocar repetição de script
        head.appendChild(script);        
    }else{
        console.warn("Script já existente: "+script_link);
    }
   
}

ijct_script('https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js');

jQuery(($)=>{


});


*///----------------------KIT PARA JQUERY TESTE

function c(content){
    return console.log(content);
}


    function setCookie(cname, cvalue, exdays) {
      var d = new Date();
      d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
      var expires = "expires="+d.toUTCString();
      document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    
    function getCookie(cname) {
      var name = cname + "=";
      var ca = document.cookie.split(';');
      for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
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
   if(e.type=="keypress"){
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
   }else if(e.type=="keydown"){
   }*/
 }

//console.log(getCookie("id_ref")+" id AQUI");
//https://stackoverflow.com/questions/424407/handling-key-press-events-f1-f12-using-javascript-and-jquery-cross-browser
function ExReg(name,dias,text){//Conta quantas vezes entra na página, ele conta quantas execuções se fez e salva nos cookies
    var re=getCookie(name);

    if(!re || re.length === 0 ){
        re=0;
    }else{
        re=(parseInt(re)+1).toString();
    }

    setCookie(name,re,1);
    console.info(text+getCookie(name));
}

function r(text){
    var re=getCookie(text);

    if(!re || re.length === 0 ){
        re=0;
    }else{
        re=(parseInt(re)+1).toString();
    }

    setCookie(text,re,1);
    console.info(text+getCookie(text));

}

ExReg("abertura_de_paginas",365,"aberturas: ");//salva por 1 ano desde a ultima visualizaçao

  function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }
  sleep(1200).then(() => {
    //fazer alguma coisa após 2 minutos;
  }

 /*try{//OLD
        jQuery(($)=>{
            if($('script[src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"]').length>0){
                return;              
            }

        });
    }catch(e){
        head.appendChild(script);
        console.error("Não há jQuery");
    }finally{
        
    }*/

/* //está com erro!
function rename_element(node,name) {//renomear um elemento
    var renamed = document.createElement(name); 
    foreach (node.attributes as a) {
        renamed.setAttribute(a.nodeName, a.nodeValue);
    }
    while (node.firstChild) {
        renamed.appendChild(node.firstChild);
    }
    return node.parentNode.replaceChild(renamed, node);
}
*/


function atualizar_select(id_datalist,id_select,id_input) {//função pra sincronizar datalist

   
    try{
      var el = document.getElementById(id_input);
      var dl = document.getElementById(id_datalist);
       if( el.value.trim() != '' ){
            var opSelected = dl.querySelector(`[value="${el.value}"]`);
            //console.log(dl+" ISSO!");
            var option = document.createElement("option");
            option.value = opSelected.value;
            option.text = opSelected.getAttribute('label');
            document.getElementById(id_select).value=el.value.trim();           
      }
  }catch (e){
    console.error("Não foi possível trimar select. funcao onInput. Provavel causa: id  nao encontrado");
  }

}


function select_all_child_elements_from_element(id_element){//seleciona todos os elementos
    var nodes = document.getElementById(id_element).childNodes;
    for(var i=0; i<nodes.length; i++) {
        if (nodes[i].nodeName.toLowerCase() == 'div') {
             nodes[i].style.background = color;
         }
    }
    return nodes;
}



function isMyScriptLoaded(url) {// verifica se o link (SOMENTE SCRIPT) já não existe
    if (!url) url = "http://xxx.co.uk/xxx/script.js";
    var scripts = document.getElementsByTagName('script');
    for (var i = scripts.length; i--;) {
        if (scripts[i].src == url) return true;
    }
    return false;
}

function ijct_script(script_link){//Injeta scripts na página. script_link = link com .js pra injetar
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.onload = function() {//abre essa função ao carregar o script
        //ACrescente a função que quiser aqui. 
    }
    script.src = script_link;
    if(!isMyScriptLoaded(script_link)){// pra evitar colocar repetição de script
        head.appendChild(script);        
    }else{
        console.warn("Script já existente: "+script_link);
    }
   
}

ijct_script('https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js');//adiciona o jQuery na página

jQuery(function($){
    $(document).click(function(event) {//mostra o innerHTML de onde clicou (VERSÃO jQuery!)
        var content = $(event.target).text();
        console.log(content);//Mostra no console o innerHTML do clique
    });

});

function i_want_the_innerHTML_of_this(){//mostra o innerHTML de onde clicou (VERSÃO JS)
    document.addEventListener('click', function(e) {
        e = e || window.event;
        var target = e.target || e.srcElement,
            text = target.textContent || target.innerText;   
    }, false);
}


