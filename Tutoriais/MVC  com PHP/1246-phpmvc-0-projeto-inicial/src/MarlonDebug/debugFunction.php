<?php



class debugLog{
   
  	public function __construct(){
     $willAutoSave=false;
     $autoSave;
     // if(autoSave!=""&&autoSave!=undefined&&autoSave!=null){
     //    willAutoSave=true;
     // }
     $log = "";
     // [{'@id':0,
     // 'manualId':0
     // }];
     //log.id=0;
     //console.log("debugLog: debugLog open");
  };
  function saveThisToInput($autoSave){
     if($this->$willAutoSave){
        $input.value=$this->log;
        console.log("sys: done: saveThisToInput(autoSave)>bool this.whillAutoSave <-> True");
     }
     
  }

	function feedback(id,valor){
     this.log+="\nID task-"+id.toString()+": "+valor; //Método antigo, sem JSON
     this.saveThisToInput(this.autoSave);
  }
  // feedbackJSON=(id,valor)=>{
  //    //log+="\nID task:"+toString(id)+": "+valor; //Método antigo, sem JSON
  //    var idString = id.toString();
  //    if(!this.log[0]['manualId']==id)
  //    {
  //       this.log['@'+idString]=valor;
  //       this.log.id.countLoop=0;
  //    }
  //    if(this.log['manualId']==id)
  //       this.log.id.countLoop+=1;


  // };
  function cookiesAutoSave(){
     // period time log. 


  };
  function showLog(){
   console.log(this.log);  
  }
  function showLogJSON(){
     return JSON.parse(this.log);
  };

}  

$debug = new debugLog();

debug.feedback(1,"Debug Executado com Sucesso!");
debug.willAutoSave=true;
debug.autoSave= document.getElementById('llfield76834');
debug.feedback(2,"Ok teste 2:")
debug.showLog();


?>