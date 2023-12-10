const commander = document.querySelector('#commander')
const codrq = document.querySelector('.codrq')



commander.addEventListener('click', ()=> {
    codrq.classList.add('active');
    // menu_ordi2.classList.remove('active');
    
})
codrq.addEventListener('click', ()=> {
    codrq.classList.remove('active');

})


