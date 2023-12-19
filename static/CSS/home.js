const menus = [
    'hbou',
    'hbou2',
    'hbou3',
    
];
const otherMenu = document.querySelector('#hbou')
otherMenu.classList.add('active');
menus.forEach((element_actuel, index_element) => {
    const menu = document.querySelector(`#${element_actuel}`);
    menu.addEventListener('click', () => {
        for (let i = 0; i < menus.length; i++) {
            const otherMenu = document.querySelector(`#${menus[i]}`);
            if (i === index_element) {
                otherMenu.classList.add('active');
            } else {
                otherMenu.classList.remove('active');
            }
        }
    });
});


