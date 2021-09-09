/*//DevMode-(model.js)
to import this .js file: // Para importar esse arquivo .js :

//MODO 1 (JS):   --------------

var url_script_dev_model="https://gist.githubusercontent.com/NMarlon/befb66a92a44115e02ccecb91cd1e0e4/raw/";
verify_if_DevModel_exists=(url_script_dev_model)=>{
    var scripts = document.getElementsByTagName('script');
    for (var i = scripts.length; i--;) {
      if (scripts[i].src == url_script_dev_model) return true;
    }
  return false
}

if(!verify_if_DevModel_exists(url_script_dev_model)){
  var devModel = document.createElement('script');
  devModel.type="text/javascript";
  devModel.src=url_script_dev_model;
  devModel.id="DevModel";
  document.getElementsByTagName('head')[0].appendChild(devModel);        
}

MODO 2 (HTML):
<script type="text/javascript" src="https://gist.githubusercontent.com/NMarlon/befb66a92a44115e02ccecb91cd1e0e4/raw/">


//-------------------------

*/


//<div id="version_doc" onload="wait_for_change_version=()=>{return new Promise((resolve,reject)=>{check_if_autoreload();});}">v0.0.0</div>
console.log("Versão atual do DevMode.js: v0.17.2");

version_actual=(ver)=>{ //OPTIONAL
	var version = document.createElement('div');
	version.onload="wait_for_change_version=()=>{return new Promise((resolve,reject)=>{check_if_autoreload();});}";
	version.innerHTML=ver;
	version.id="version_doc";
	version.hidden=true;
  document.getElementsByTagName('head')[0].appendChild(version);        

}

function isMyScriptLoaded(url) {// verifica se o link (SOMENTE SCRIPT) já não existe
	if (!url) url = "http://xxx.co.uk/xxx/script.js";
	var scripts = document.getElementsByTagName('script');
	for (var i = scripts.length; i--;) {
		if (scripts[i].src == url) return true;
	}
	return false;
}
function ijct_script(script_link, funct){//Injeta scripts na página. script_link = link com .js pra injetar
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.onload = funct;
    script.src = script_link;
    if(!isMyScriptLoaded(script_link)){// pra evitar colocar repetição de script
        head.appendChild(script);        
    }else{
        console.warn("Script já existente: "+script_link);
    }
   
}
//https://html2canvas.hertzen.com/ tirar print

window.onload = (start=>{
  ijct_script('https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js', null); 
});


function c(content){
	return console.log(content);
}
function setCookie(cname, cvalue, exdays) {
	var d = new Date();
	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
	var expires = "expires="+d.toUTCString();	
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/;"+"SameSite=Lax; Secure;";
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

	
check_if_autoreload=()=>{
	ExReg("chegou aqui3",365,"3: ");//salva por 1 ano desde a ultima visualizaçao

	if(getCookie("version_doc_auto_reload")==document.getElementById('version_doc').innerHTML) {
		ExReg("chegou aqui4",365,"4: ");//salva por 1 ano desde a ultima visualizaçao

		window.location.reload(true);	
		return
	}else{
		ExReg("chegou aqui5",365,"5: ");//salva por 1 ano desde a ultima visualizaçao
		setCookie("version_doc_auto_reload","",-1);
		return
	}
};

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


funcoes_de_teste= (id_teste)=>{
	if(id_teste==""){
		//se não houver nada aqui...
	}else if(id_teste=="0"){
		//algo aqui
	}else{
		alert('Número de teste não encontrado!');
		chat_assist();
	}

};




name_user=()=>{

  var dev_nick = prompt('Bem-vindo, digite seu nome de usuário: ')
 	setCookie("dev_username_"+dev_nick,dev_nick,365); // 1 ano salvo	
 	alert("criado com sucesso!");
};

diaSeg=(valor)=>{
	return valor/24/60/60;
};
/*

conv=(valor,type,typeValor)=>{
	var array=[60000,3600000,86400000,31536000000];
	return 
}
*/
auto_reload_ate_version_mudar = (text,timeOut)=>{		
			ExReg("chegou aqui6",365,"6: ");//salva por 1 ano desde a ultima visualizaçao
	setCookie('version_doc_auto_reload',text,diaSeg(timeOut));
	//setCookie('version_doc_auto_reload',"true",timeOut);

};


chat_assist=(dev_nick)=>{

	console.log("Bem-vindo dev "+ dev_nick);
	var solicitacao_dev = prompt( 'Digite "/help" pra saber o que você pode fazer\n'+document.getElementById('version_doc').innerHTML);
	try{
	if(solicitacao_dev=="/help"){
		alert('/cdn (muda o nickname de dev atual))\n/v (ver versão atual)\n/test=on (habilita o modo de teste e mantém ligado)\n/test=off (desabilita modo de teste)\n/autoreload ou /autor ou /ar =0~inf [timOut: padrao 60] (recarrega a página por durante esse tempo ou até o version_doc alterar)\n');
		chat_assist(dev_nick);
	}else if(solicitacao_dev=="/cdn"){
		name_user();
	}else if(solicitacao_dev=="/v"){
		if(confirm("A versão atual em cookies é: "+getCookie("v")+"\n(cancelar pra sair)"))chat_assist(dev_nick);
	}else if(solicitacao_dev=="/r"|| solicitacao_dev=="/reload"){
		window.location.reload(true);
	}else if(solicitacao_dev=="/teste=on"|| solicitacao_dev=="/teste"){
		funcoes_de_teste(solicitacao_dev.split('=').trim());
		alert("modo de teste habilitado");
	}else if(solicitacao_dev.search("/autoreload")|| solicitacao_dev.search("/autor")|| solicitacao_dev.search("/autoR")|| solicitacao_dev.search("/ar")){
		try{
			var timeOut_ar= parseInt(solicitacao_dev.split('=')[1].trim())>0;
		}catch(e){
				auto_reload_ate_version_mudar(document.getElementById('version_doc').innerHTML,60);

		}
		/*
			ExReg("chegou aqui1",365,"1: ");//salva por 1 ano desde a ultima visualizaçao
			if(!(timeOut_ar)){

			}else{
				ExReg("chegou aqui2",365,"2: ");//salva por 1 ano desde a ultima visualizaçao
			*/
				auto_reload_ate_version_mudar(document.getElementById('version_doc').innerHTML,timeOut_ar);
			//}
			window.location.reload(true);
		
	}else if(solicitacao_dev=="/consoleClear"|| solicitacao_dev=="/consoleclear"|| solicitacao_dev=="/console_clear"|| solicitacao_dev=="/console_Clear"){
		console.clear();
		chat_assist(dev_nick);

	}else{alert("Não entendi/Ainda falta me desenvolver :| ");}

	}catch(e){
		console.error("Erro no dev_assist! (função chat_assist) Erro: "+e);
		if((!solicitacao_dev==""|| solicitacao_dev=="false")){
			alert("houve um erro! Acho que preciso de reparos :( ");
			chat_assist(dev_nick);
		}
	}finally{

	}
}
check_if_user_dev_exists=((dev_nick_input)=>{	
	dev_nick = getCookie('dev_nick_'+dev_nick_input);
	if(dev_nick_input==dev_nick){
		setCookie("last_dev",dev_nick,7); // 7 dias salvo
  	return true
	}
	return false
});

 

create_dev= (()=>{
	var dev_nick= prompt("Digite seu nome de usuário: ");
	setCookie("dev_nick_"+dev_nick,dev_nick,365);

});
remove_dev= ((dev_nick)=>{
	setCookie("dev_nick_"+dev_nick,"",-1);
});


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
        	dev_nick=getCookie("last_dev");
        	if(dev_nick!="" || document.location.href.search('dev_nick_=NMarlon')>=0){
        		chat_assist(dev_nick);
        		return
        	}  
        	var debug_mode_key = prompt('Olá! Seja bem vindo!');//qualquer bordão pra o user não estranhar o textbox.

      		if(check_if_user_dev_exists(debug_mode_key)){

      			chat_assist(debug_mode_key);
      		}else if(debug_mode_key=="/create"){
	          create_dev();
      		}else if(debug_mode_key=="/drop"){
      			remove_dev();
      		}else if(debug_mode_key==false){
      			return
	        }else{
	            if(confirm("Deseja ser redirecionado para página inicial?: https://testeapi-lojavirtual.000webhostapp.com/ ")){
	                window.location.href=" https://testeapi-lojavirtual.000webhostapp.com/";
	            }
	        }
        }
        }/*else if(e.type=="keyup"){
        }else if(e.type=="keypress"){
        }*/
      }
      


