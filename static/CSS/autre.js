// const cli = document.querySelector('#img')
// const sort = document.querySelector('.zeyrze')


// cli.addEventListener('click', ()=> {
//     sort.classList.add('active');
//     // menu_ordi2.classList.remove('active');
    
// })
// cli.addEventListener('click', ()=> {
//     sort.classList.remove('active');

// })













const imoer1Elements = document.querySelectorAll('.imoer1');
const infosurart = document.querySelector('.infosurart');
const vetedsqs = document.querySelector('#vetedsqs');

imoer1Elements.forEach(element => {
    element.addEventListener('click', function() {
        const nom = element.querySelector(".nomzp").innerText;
        const des = element.querySelector(".despzp").innerText;
        const passwordid = element.querySelector(".pistzp").innerText;
        const imgzs = element.querySelector("#bysrd").value;

        const tab = [imgzs, nom, des, passwordid];
        console.log(tab);

        // Actions à effectuer lors du clic sur .imoer1
        infosurart.classList.add('active');

        let gdsh = `
        <div class="mslkjhy">
            <div class="anuezol" id="vetedsqs">
            <img src="static/IMAGES/crit.png
            " alt="" height="30px" width="30px" >
            </div>
            <div class="imoaeImagee">
                <img src="static/uploads/${imgzs}"  alt="">
            </div>
            <div class="imoaeInfo">
                <div class="imoaeInfomp">
                    <h1 style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;font-weight: bolder;font-size: 0.8rem;text-transform: uppercase;">${nom}</h1>
                    <p style="margin-bottom: 10px;color: rgb(146, 143, 143);font-size: 0.7rem;">${des}</p>
                    <h1 style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;font-weight: bolder;color: rgb(90, 7, 163);padding-bottom: 20px;font-size: 1rem;text-transform: uppercase;">${passwordid} FCFA</h1>
                </div>
                <div class="imoaeBoute" id="sac">
                    <form action="/new" method="post" >
                        <input style="opacity: 0;height: 0;width: 0;" type="text" name="nom" value="${nom}">
                        <input style="opacity: 0;height: 0;width: 0;"  type="text" name="desc" value="${des}">
                        <input style="opacity: 0;height: 0;width: 0;"  type="text" name="prix" value="${passwordid}">
                        <input id="bysrd" style="opacity: 0;height: 0;width: 0;"  type="text" name="image" value="${imgzs}">
                        <!-- <button type="submit" id="addpa" ><img src="{{url_for('static', filename='IMAGES/charrete.png')}}"  alt="" >
                        </button> -->
                        <button type="submit" id="addpa" ><p style="font-size: 0.7rem;">AJOUTER AU PANIER</p>
                        </button>
                        
                        
                    </form>
                    
                </div>

            </div>
            
        </div>`;

        infosurart.innerHTML = gdsh;
    });
});

// Ajoutez également l'événement de clic pour fermer .infosurart à l'extérieur de la boucle
infosurart.addEventListener('click', () => {
    infosurart.classList.remove('active');
});


// const imoer1Elements = document.querySelectorAll('.imoer1');

// imoer1Elements.forEach(element => {
//     element.addEventListener('click', function() {
//         // Code à exécuter lorsque l'élément est cliqué
//         const infosurart = document.querySelector('.infosurart')

//         console.log('Element cliqué:', element);
       
//         const imoer1 = document.querySelector('.imoer1')
//         infosurart.classList.add('active');
//             // menu_ordi2.classList.remove('active');
            
        
//         infosurart.addEventListener('click', ()=> {
//             infosurart.classList.remove('active');
        
//         })





//         let nom = document.querySelector(".nomzp").innerText;
//         let des = document.querySelector(".despzp").innerText;
//         let passwordid = document.querySelector(".pistzp").innerText;




//         let imgzs = document.querySelector("#bysrd").value;
//         let infosurartp = document.querySelector('.infosurart');
//         let tab = [imgzs, nom, des, passwordid];

//         console.log(tab);


        
//         let gdsh = `

//         <div class="mslkjhy">
//                 <div class="imoaeImage">
//                     <img src="static/uploads/${imgzs}" height="130px" width="150px" alt="">
//                 </div>
//                 <div class="imoaeInfo">
                    
//                     <h1  style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;font-weight: bolder;font-size: 0.8rem;text-transform: uppercase;"> ${nom}</h1>
                    
//                     <p style="margin-bottom: 10px;color: rgb(146, 143, 143);font-size: 0.7rem;">${des}</p>

//                     <h1 style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;font-weight: bolder;color: rgb(90, 7, 163);padding-bottom: 20px;font-size: 1rem;text-transform: uppercase;">${passwordid} FCFA</h1>
//                 </div>
//             </div>`;

//         infosurartp.innerHTML = gdsh;
//         return imoer1
//     });
// });

// const infosurart = document.querySelector('.infosurart')
// const imoer1 = document.querySelectora('.imoer1')
const commander = document.querySelector('#commander')
const codrq = document.querySelector('.zeyrze')
const autr = document.querySelector('.maile')
const vra = document.querySelector('.footer')
const vrae = document.querySelector('#vete')



// imoer1.addEventListener('click', ()=> {
//     infosurart.classList.add('active');
//     // menu_ordi2.classList.remove('active');
    
// })
// infosurart.addEventListener('click', ()=> {
//     infosurart.classList.remove('active');

// })
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



































// let nom = document.querySelector("h1#nomzp").value;
// let des = document.querySelector("#despzp").value;
// let passwordid = document.querySelector("#pistzp").value;
// let infosurartp = document.querySelector('.infosurart');
// let tab = [nom,des,passwordid];
// console.log(tab);
// tab.forEach(user => {
//     let gdsh = `  <h1>${user}</h1>
//         <p>${des}</p>
//         <p>${passwordid}</p>
//     `
//     infosurartp.innerHTML += gdsh
// });









// const imoer1Elements = document.querySelectorAll('.imoer1');

// imoer1Elements.forEach(element => {
//     element.addEventListener('click', function() {
//         // Code à exécuter lorsque l'élément est cliqué
//         const infosurart = document.querySelector('.infosurart')

//         console.log('Element cliqué:', element);
       
//         const imoer1 = document.querySelector('.imoer1')
//         infosurart.classList.add('active');
//             // menu_ordi2.classList.remove('active');
            
        
//         infosurart.addEventListener('click', ()=> {
//             infosurart.classList.remove('active');
        
//         })
//         return imoer1
//     });
// });

