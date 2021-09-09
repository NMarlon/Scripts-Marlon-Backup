
function exit_chat(){
    document.getElementsByClassName('chat-box')[0].style.display="none";
}
var button = document.createElement('button');
button.setAttribute('onclick',"exit_chat();");
button.innerHTML="X";
button.style.margin="auto";
button.style.border="none";


window.onload = function(){document.getElementsByClassName('avatar-intro')[0].appendChild(button)}