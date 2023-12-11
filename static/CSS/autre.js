// const cli = document.querySelector('#img')
// const sort = document.querySelector('.zeyrze')


// cli.addEventListener('click', ()=> {
//     sort.classList.add('active');
//     // menu_ordi2.classList.remove('active');
    
// })
// cli.addEventListener('click', ()=> {
//     sort.classList.remove('active');

// })


const commander = document.querySelector('#commander')
const codrq = document.querySelector('.zeyrze')
const autr = document.querySelector('.maile')
const vra = document.querySelector('.footer')
const vrae = document.querySelector('#vete')



commander.addEventListener('click', ()=> {
    codrq.classList.add('active');
    // menu_ordi2.classList.remove('active');
    
})
codrq.addEventListener('click', ()=> {
    codrq.classList.remove('active');

})

autr.addEventListener('click', ()=> {
    vra.classList.add('active');
    window.location.replace("achat#Contactez")

    // menu_ordi2.classList.remove('active');
    
})
vrae.addEventListener('click', ()=> {
    vra.classList.remove('active');

})
