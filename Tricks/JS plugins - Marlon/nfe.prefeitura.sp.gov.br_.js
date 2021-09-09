//OBJETIVO colocar datalist


// RESULTADO: FAIL 
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

ijct_script('https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js');


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
function ExReg(name,dias){//Conta quantas vezes entra na página, ele conta quantas execuções se fez e salva nos cookies
    var re=getCookie(name);

    if(!re || re.length === 0 ){
        re=0;
    }else{
        re=(parseInt(re)+1).toString();
    }

    setCookie(name,re,1);
    console.info(getCookie(name));
}

function atualizar_select(id_datalist,id_select,id_input) {   
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
            //javascript:LerAtividade(document.getElementById("ctl00_body_ddlAtividade").selectedIndex,'1');setTimeout('__doPostBack(\'ctl00$body$ddlAtividade\',\'\')', 0);
            LerAtividade(document.getElementById("ctl00_body_ddlAtividade").selectedIndex,'1');setTimeout('__doPostBack(\'ctl00$body$ddlAtividade\',\'\')', 0);


      }
  }catch (e){
    console.error("Não foi possível trimar select. funcao onInput. Provavel causa: id  nao encontrado");
  }

}
function select_all_child_elements_from_element(id_element){
    var nodes = document.getElementById(id_element).childNodes;
    for(var i=0; i<nodes.length; i++) {
        if (nodes[i].nodeName.toLowerCase() == 'div') {
             nodes[i].style.background = color;
         }
    }
    return nodes;

}

window.onload = ()=>{
    ExReg("re_da_pagina_aqui",365);//salva por 1 ano desde a ultima visualizaçao

    //var campo_select_categoria_servico =  document.getElementById('ctl00_body_ddlAtividade'); //'<select name="ctl00$body$ddlAtividade" onchange="javascript:     (this.selectedIndex,"1");setTimeout("__doPostBack(\"ctl00$body$ddlAtividade\",\"\")", 0)" id="ctl00_body_ddlAtividade" class="textbox" style="font-size:10px;width:100%;"></select>';
    var campo_datalist_categoria_servico = document.createElement("datalist"); 
    campo_datalist_categoria_servico.class="textbox";
    campo_datalist_categoria_servico.style="font-size:10px;width:100%;"
    campo_datalist_categoria_servico.onchange='atualizar_select("datalist_cat_serv","ctl00_body_ddlAtividade","input_cat_serv");';
    campo_datalist_categoria_servico.appendChild(campo_select_categoria_servico);
/*
    var ancora = $('<div id="ancora_cat_serv"></div>');
    
     $('#ctl00_body_ddlAtividade').insertBefore(ancora);

    var campo_select_categoria_servico = $('#ctl00_body_ddlAtividade');
    //$('#ctl00_body_ddlAtividade').remove(); //'<select name="ctl00$body$ddlAtividade" onchange="javascript:     (this.selectedIndex,"1");setTimeout("__doPostBack(\"ctl00$body$ddlAtividade\",\"\")", 0)" id="ctl00_body_ddlAtividade" class="textbox" style="font-size:10px;width:100%;"></select>';

    //'<datalist  onchange=")" id="datalist_cat_serv" class="textbox" style="font-size:10px;width:100%;"></datalist>';
    //var renamed = document.createElement("datalist"); 
    var input_cat_serv= $('<input id="input_cat_serv" list="datalist_cat_serv" style="font-size:10px;width:100%;"></input>');
    
    $('#ancora_cat_serv').insertAfter(campo_datalist_categoria_servico);
    $('#ancora_cat_serv').insertAfter(input_cat_serv);
    //document.getElementById("ctl00_body_ddlAtividade");//AQUI O ID DO CAMPO   
    //el.insertAdjacentElement('beforebegin',input_cat_serv);
    //el.insertAdjacentElement('beforebegin',campo_datalist_categoria_servico);
    //campo_datalist_categoria_servico.appendChild(el);


    //$('#ctl00_body_ddlAtividade').insertBefore(campo_datalist_categoria_servico);  
/*
    $('ctl100_bodt').insertBefore('<input list="ctl00_body_ddlAtividade" style="width:100%">');
    var campo_datalist_categoria_servico = campo_select_categoria_servico;
    //campo_datalist_categoria_servico.replaceWith('<newTag>' + $(campo_datalist_categoria_servico).html() +'</newTag>');
    //rename_element(campo_datalist_categoria_servico,'datalist');
    //$(campo_datalist_categoria_servico).replaceWith($('<'+'datalist'+'/>').html($(campo_datalist_categoria_servico).html()));
    campo_datalist_categoria_servico.id="datalist_cat_serv";
    campo_datalist_categoria_servico.name="";
    campo_datalist_categoria_servico.list="ctl00_body_ddlAtividade";
    var input_cat_serv = '<input id="input_cat_serv" list="datalist_cat_serv"/>';


    campo_datalist_categoria_servico.onchange='atualizar_select("datalist_cat_serv","ctl00_body_ddlAtividade","input_cat_serv");';
    $('ctl100_bodt').insertBefore('<input list="ctl00_body_ddlAtividade" style="width:100%">');
    $('#datalist_cat_serv').insertBefore(input_cat_serv);

    $('#datalist_cat_serv').insertAfter(campo_select_categoria_servico);*/
};

function prettify(){

}
prettify();