let map = L.map('map').setView([53.551, 9.993], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a', 'b', 'c'],
}).addTo(map)


let myIcon = L.divIcon({
    html: "<div  class='marker_pin'></div>",
    iconAnchor: [9, 21],
    popupAnchor: [0, -14]
})
let myIconActive = L.divIcon({
    html: "<div  class='marker_pin_active'></div>",
    iconAnchor: [9, 21],
    popupAnchor: [0, -14]
})

let icons = [];
let s;
for (let i = 0; i < markers.length; ++i) {
    s = L.marker([markers[i].lat, markers[i].lng], { icon: myIcon })
        .bindTooltip(
            '<a href="' +
            markers[i].url +
            '" target="_blank">' +
            markers[i].name +
            '</a> <div><img src=" ' + markers[i].imgUrl + ' " style="width: 100%" /> </div>',
            {
                direction: 'top'
            }
        )
        .addTo(map)

    let obj = {
        marker: s,
        id: markers[i].id
    }
    icons.push(obj)
}
console.log(icons)
console.log(icons[1].marker)

let list = document.querySelector('.main_list')
let cards = document.querySelectorAll('.main_card');
console.log(cards)



cards.forEach(item => {
    let match = icons.find(element => element.id == item.id)
    item.addEventListener("mouseover", () => {
        console.log(match)
        console.log(item.id)
        match.marker.setIcon(myIconActive)
        // icons.forEach(i => i.setIcon(myIconActive));
        console.log(item.getAttribute("id"))
    });

    item.addEventListener("mouseout", () => {
        match.marker.setIcon(myIcon)
    })
});



