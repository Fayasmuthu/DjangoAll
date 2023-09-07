const wrapper =document.querySelector('.wrapper');
const loginlink =document.querySelector('.login-link')
const registerlink =document.querySelector('.register-link');
const btnpopup =document.querySelector('.btnLogin-popup');
const iconclose =document.querySelector('.icon-close');
const iconperson=document.querySelector('.person1')
const backg =document.querySelector('.backg');
let searchlogo =document.querySelector('.search');
let searchshow =document.querySelector('#Searchform');
let search =document.querySelector('.searchbox11');





registerlink.addEventListener('click',()=>{
    wrapper.classList.add('active');
});

loginlink.addEventListener('click',()=>{
    wrapper.classList.remove('active');
});
btnpopup.addEventListener('click',()=>{
    wrapper.classList.add('action-popup');
});
iconclose.addEventListener('click',()=>{
    wrapper.classList.remove('action-popup');
});
iconperson.addEventListener('click',()=>{
    wrapper.classList.add('action-popup');
});
// searchlogo.onclick = () =>{
//     searchlogo.classList.toggle('fa-times');
//     searchshow.classList.toggle('active');
// }
// window.onscroll = () =>{
//     searchlogo.classList.remove('fa-times');
//     searchshow.classList.remove('active');
// }
// document.querySelector('.search').onclick = () =>{
//     document.querySelector('#Searchform').classList.remove('active')
// }

document.querySelector('#search1').onclick = () =>{
    search.classList.toggle('active');
}


