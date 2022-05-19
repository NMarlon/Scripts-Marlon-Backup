
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

//ijct_script('https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js');//adiciona o jQuery na página
