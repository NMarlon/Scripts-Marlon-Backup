
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


function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }
      

window.onload = jQuery(($)=>{//após a janela carregar


    sleep(30000).then(()=>{// depois de 2 segundos
        if($('#elementor-panel-state-loading').length>0){
            alert("Congelamento do Loading no EDITAR do Elementor.. Tentado resolver...");
            $('#elementor-panel-state-loading').remove();
        }
    });
    sleep(60000).then(()=>{// depois de 2 segundos        
        if($('#elementor-editor-wrapper').length>0){
            if(confirm("Elementor não aberto em 60 segundos... Deseja reiniciar")){
                console.warn("Elementor não aberto em 60 segundos... Reiniciando"...);
                location.reload();
            }
        }
    });
});