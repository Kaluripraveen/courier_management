
const primarynav =document.getElementById("primary-navigation");
 const navToggle = document.querySelector(".mobile-nav-toggle");
 navToggle.addEventListener("click",() => {
     let visibility = primarynav.getAttribute("data-visible");
     if(visibility === "false"){
         primarynav.setAttribute('data-visible',true);
         navToggle.setAttribute('aria-expanded',true);
     }else{
         primarynav.setAttribute('data-visible',false);
         navToggle.setAttribute('aria-expanded',false);
     }
    
});

var x=document.getElementById('login');
console.log(x);
var y=document.getElementById('register');
console.log(y)
var z=document.getElementById('btn');
const button2=document.getElementById("loginbutton")
const button = document.getElementById("resbutton");
button.addEventListener("click",()=>{
    x.style.left='-400px';
    y.style.left='50px';
    z.style.left='110px';

});
button2.addEventListener("click",()=>{
    x.style.left='50px';
    y.style.left='450px';
    z.style.left='0px';

})

function register()
{
    x.style.left='-400px';
    y.style.left='50px';
    z.style.left='110px';
};
function login()
{
    x.style.left='50px';
    y.style.left='450px';
    z.style.left='0px';
}
var modal = document.getElementById('login-form');
window.onclick = function(event) 
{
    if (event.target == modal) 
    {
        modal.style.display = "none";
    }
}

const forme1 = document.querySelector('.input-group-register');
const forme2 = document.querySelector('.input-group-login');
console.log(forme1);

forme1.addEventListener("submit", event=>{
    event.preventDefault();

    const registerData= new FormData(forme1);
    
    const data1 = Object.fromEntries(registerData);
    
    
    fetch('http://127.0.0.1:8000/register',{
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data1)
    }).then(res => res.json())
      .then(console.log(JSON.stringify(data1)))

    

    
});
