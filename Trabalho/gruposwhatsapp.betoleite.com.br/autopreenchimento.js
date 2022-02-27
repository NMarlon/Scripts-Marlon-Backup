// https://gruposwhatsapp.betoleite.com.br/redirecionadores/semanadaeducacao-org-8/
//https://gruposwhatsapp.betoleite.com.br/novo/


function triggerEvent( elem, event ) {
  var clickEvent = new Event( event ); // Create the event.
  elem.dispatchEvent( clickEvent );    // Dispatch the event.
};
var links = ["https://chat.whatsapp.com/umGRupoijwa0r98qj0r9q",
"https://chat.whatsapp.com/outroGRuposojeapwfj"];



function add_link(){
    try{
    setTimeout(() => {
        var i = 0 ;
        while(i < quantidade_de_grupos){
            var name= "txt_group_link_" + i.toString();
            
            console.log(name);
            document.getElementById(name).value=links[i];
            i+=1;
        }
     }, 600);
    }catch (e){
        add_links();
        console.log("erro, espaço pra links não encontrado, procurando...");
    }
}

var quantidade_de_grupos=links.length;
window.onload = function(){
    document.getElementById("txt_site_name").value="Associação Brasileira de A Igreja de Jesus Cristo dos Santos do Últimos Dias";
    document.getElementById("txt_site").value="semanadaeducacao.org";
    document.getElementById("txt_per_group_number").value="250";    
    document.getElementById("txt_group_number").value=quantidade_de_grupos;
    //document.getElementById("generate_links_btn").innerHTML="1 - Criar espaços";
    var button =  document.createElement('div');
    button.innerHTML="2 - Colocar links";
    button.setAttribute('onclick','add_link();');
    button.setAttribute('style','height:40px;background:purple;border-radius:5px;padding:8px;display: block;position: absolute;right: 10vw;cursor:pointer;'); 
    button.id="colocar_links_2";
    //button.setAttribute('class','button');
    document.getElementById("generate_links_btn").insertAdjacentElement('afterend', button);
    //document.getElementById("generate_links_btn").setAttribute('onclick','add_links()');
};

