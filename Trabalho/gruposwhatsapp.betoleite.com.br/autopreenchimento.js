// https://gruposwhatsapp.betoleite.com.br/redirecionadores/semanadaeducacao-org-8/
//https://gruposwhatsapp.betoleite.com.br/novo/


function triggerEvent( elem, event ) {
  var clickEvent = new Event( event ); // Create the event.
  elem.dispatchEvent( clickEvent );    // Dispatch the event.
};
var links = ["https://chat.whatsapp.com/KJl0bGCbeLbCbW2mrtk7Gb",
"https://chat.whatsapp.com/D4aiz3x6K0r4JQCqaVHRD9",
"https://chat.whatsapp.com/EhLjTJdJiXXDDMLZ3WhHez",
"https://chat.whatsapp.com/KrX3P5xCUIICLR3RjWTXh6",
"https://chat.whatsapp.com/Dik8TGnsnsK1Zt7nDXx9Ln",
"https://chat.whatsapp.com/Dd0tzWPZPn07PyinhIJDem",
"https://chat.whatsapp.com/GPJQSEjcRZj3q7LlpPtAp5",
"https://chat.whatsapp.com/IZjetv7PEMZ85d7dD55OrE",
"https://chat.whatsapp.com/BCr6JzuK1ZP3jycaXcEFp2",
"https://chat.whatsapp.com/DACgK5Kv7JJ6f7hrw7yVWS",
"https://chat.whatsapp.com/FdCcatW61sOHg7mo7ofQEC",
"https://chat.whatsapp.com/Kf9gOUzKUXg1Xbgk8gbsO0",
"https://chat.whatsapp.com/J3xolQvuXFPBfYt70ZVpWm",
"https://chat.whatsapp.com/JV4llONSf6S5oFEuZTj1D5",
"https://chat.whatsapp.com/GYkH1K8ew8iBuZCtkYlLxc",
"https://chat.whatsapp.com/FTtTyhtOPFm4qzO87BUF1b",
"https://chat.whatsapp.com/JUplA2qqdxrA5SI7O2oWW0",
"https://chat.whatsapp.com/FzNZfiaoYPE7GRGqXi9L8o",
"https://chat.whatsapp.com/Ffmf5c7z6gl9NWqMFZ2rkj",
"https://chat.whatsapp.com/InJtbSP4quJ4RdNgJR3p4U",
"https://chat.whatsapp.com/KuIYR3PlHPz9ZkpMyB1CyN",
"https://chat.whatsapp.com/E5bfCPV7Dst1tIRJ8dqsS1",
"https://chat.whatsapp.com/D815C4PzRRU4SOcfSNQfKJ",
"https://chat.whatsapp.com/E2UUACzFl8VCdtgCQ0swNc",
"https://chat.whatsapp.com/KYk75I5WnDCEd5XP5JAas3",
"https://chat.whatsapp.com/HMlpz4bW0OpGynf2AqdC8G",
"https://chat.whatsapp.com/BZyR5hj0wZr1QalcjN4A6b",
"https://chat.whatsapp.com/JVUSNXKEHDT26D6a5bCxia",
"https://chat.whatsapp.com/BMBA8lbAZL8GMPLbsFDaS9",
"https://chat.whatsapp.com/D8TCmSOcN8y1PWgn3MYGae",
"https://chat.whatsapp.com/HmOCHwN2Uc10rwkyXjmij8",
"https://chat.whatsapp.com/FlbvUXvOihWAwGKpngvRXi",
"https://chat.whatsapp.com/Le7htAC7FAlLBXPNJyLQpx",
"https://chat.whatsapp.com/FNBPi9JCSg81mxoE5AiKJE",
"https://chat.whatsapp.com/FCKXK6TxFgQHq2k50HPQsD",
"https://chat.whatsapp.com/IKh0wKFMtqXBcXLewBVSEF",
"https://chat.whatsapp.com/Cmb9JlPCF7m4NO09KyYOoi",
"https://chat.whatsapp.com/Gip3LyfkGai2sb2YawdkyE",
"https://chat.whatsapp.com/HyaebstVSzWGQFx0TiWjLp",
"https://chat.whatsapp.com/HSoJ4chr7VTFNoVaAWDC0y",
"https://chat.whatsapp.com/LORfrk2Hpnl5xLceQSTJe8",
"https://chat.whatsapp.com/JsGskHYOFLzIaUTiI1MBgd",
"https://chat.whatsapp.com/JDjaUFlavUxK3ND07muv3B",
"https://chat.whatsapp.com/GoUv0rBRN5BDf3xjofKjkM",
"https://chat.whatsapp.com/HoEOKb4ktBu5OUjezpw5e3",
"https://chat.whatsapp.com/JXE3zaB6mIb7EZxJ6yN9F3",
"https://chat.whatsapp.com/IqpPYc6hiQjGdbDdVR4bMc",
"https://chat.whatsapp.com/DTqpnPDkUzRAE1JI2PVKVt",
"https://chat.whatsapp.com/CcCz9gQtl9sByN9ya1dKB4",
"https://chat.whatsapp.com/KNFLKU9EXZi21RrmjhOe0n",
"https://chat.whatsapp.com/Is201UcUvwr5MPicY4lTAA",
"https://chat.whatsapp.com/Ipk1VSgznQR9ZlaNY5AlGj",
"https://chat.whatsapp.com/GC4Bw3S3Kph3Q0QrQUQCCB",
"https://chat.whatsapp.com/JXbp7PzQMt9LQtoZebzzJN",
"https://chat.whatsapp.com/CBKJpXFpPht3Re4M3d7rwG",
"https://chat.whatsapp.com/CwVqhgyOhbq6pof2QlLzdn",
"https://chat.whatsapp.com/G5UGqOsNnsKAD4HyK1fObH",
"https://chat.whatsapp.com/Iz2bWbiiKU03KRvT6fULjv",
"https://chat.whatsapp.com/DrdauvV9LpJHoVmqPDT1DC",
"https://chat.whatsapp.com/CRxBRjz5hST5s1ZhCLoYxw",
"https://chat.whatsapp.com/CwpJzxhdJu6COMjYfNWRRI",
"https://chat.whatsapp.com/EFyzgWRpIJB8COL4InwImU",
"https://chat.whatsapp.com/Gg6Y4jerqStEBewkNKFVUB",
"https://chat.whatsapp.com/CwFpAC25e6K4sfTdCLHJbh",
"https://chat.whatsapp.com/Jas3FAfAU7X3sXp0ejfOd7",
"https://chat.whatsapp.com/Lxv7WJAlBJx6LKjOre6UGT",
"https://chat.whatsapp.com/GFo6Q1Cp2nd7hwlZH8xo7f",
"https://chat.whatsapp.com/DMOPxkhEaSN0X8U17F5M9i",
"https://chat.whatsapp.com/LPMSVneW6iC7GBZoYYUMZ3",
"https://chat.whatsapp.com/BmEIhLeTctw0otfrLUQzxo",
"https://chat.whatsapp.com/EJgyXzOjiY50Lf1DEhnv7D",
"https://chat.whatsapp.com/G5EvYnfLiFpC2Y10b0Y8Oc",
"https://chat.whatsapp.com/D3Xe12s9QYb9j38eqQwSt7",
"https://chat.whatsapp.com/Ig5cuoDZgrxBKZN8AbE8vu",
"https://chat.whatsapp.com/FOooyRdkf9o29MtRuD8YOU",
"https://chat.whatsapp.com/EeUZKV2BYNbLNbAPn4qY6h",
"https://chat.whatsapp.com/I4QbJMowNjnC6CGRMDnTkL",
"https://chat.whatsapp.com/IO1L1Dhaa9zKnH3RHA2CwE",
"https://chat.whatsapp.com/GxwAhqXCU9jAmoCuVxif7C",
"https://chat.whatsapp.com/I3vH8XDbIL38SZXE8TwQmg",
"https://chat.whatsapp.com/DRcXEV1lOzA525pKBxUeTJ",
"https://chat.whatsapp.com/H3FXSqnwQvWENcgK5PtbtL",
"https://chat.whatsapp.com/Fp14zgZTykmFKWfVQ20EYQ",
"https://chat.whatsapp.com/BoQpcjqpofY9oqYGX1uUYq",
"https://chat.whatsapp.com/GC6OHRnOKUb1KqpxqpnB5d",
"https://chat.whatsapp.com/Erug7ZprgsW043ckgdWpWg",
"https://chat.whatsapp.com/JTpUDUoHZ9k8wq2s9mdzK2",
"https://chat.whatsapp.com/Ecf0EZNsSzNAj02VpiQLKO",
"https://chat.whatsapp.com/CW6Tq6WHjNT8MKDmGbbN81",
"https://chat.whatsapp.com/HI2Z3pqORJu17N3gwJCVxi",
"https://chat.whatsapp.com/BY7hUpwvIDE8RfeAzqRPkw",
"https://chat.whatsapp.com/Hqeio8JI728E9y2fEWXyMd",
"https://chat.whatsapp.com/LWR4d1mQVG70zITzwNDSib",
"https://chat.whatsapp.com/FAlRskiKAa6DWNycoM08Fm",
"https://chat.whatsapp.com/KkPa92R3TAA2MJpmOW14Ds",
"https://chat.whatsapp.com/K0Qo9Z325sW6U61hwmBRhe",
"https://chat.whatsapp.com/FyQ7HdtTz9TAoZyn7QPw2r",
"https://chat.whatsapp.com/FhgZjNkABZ7FeFzcCsDfQR",
"https://chat.whatsapp.com/EWKfBMiwNgiDnrxnbZZLPG",
"https://chat.whatsapp.com/DVrKOPjXtL3D0HGRnaN7WS"];



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

