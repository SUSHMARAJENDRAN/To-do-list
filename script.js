let input=document.querySelector('.value');
let submit=document.querySelector('.submit');
let main=document.querySelector('.main');
let full=document.querySelector('.full');
let sub=document.querySelector('.sub');
let delet=document.querySelector(".delete");
let box=document.querySelector('.box');
delet.addEventListener('click',function(){
    main.innerHTML=''
})
submit.addEventListener('click',function(){
    let val=input.value
    input.value=''
    let div=document.createElement("div");
    div.setAttribute('class','sub');
    div.innerHTML=`<h4 class='content'>${val}</h4>,<img src="download (1).png" class='deletes' >,<div class="box">
        
    &#10003;</div>`
    main.append(div);
     
    div.querySelector(".deletes").addEventListener("click", function () {
        div.remove();
    });
    div.querySelector(".box").addEventListener("click", function (event) {
        event.target.style.backgroundColor = 'green';
    });
    
    
})

box.addEventListener('click',function(event){
    event.target.style.backgroundColor = 'green';
})