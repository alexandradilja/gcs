const app = document.getElementById('root')



const container = document.createElement('div')
container.setAttribute('class', 'container')
container.setAttribute('id', 'container')


app.appendChild(container)



var param; // initialize value for the input of user
//get input from user
function search() {
    // Make container empty and able to be filled with a new search results
    document.getElementById("container").innerHTML = "";

    // Get search term
    param = document.getElementById("searchParam").value;

    var request = new XMLHttpRequest()
    // make url with searchterm parameters
    var url = 'https://content.googleapis.com/customsearch/v1?cx=001361074102112665899%3Ap7mybnrloug&q='+param+'&searchType=image&key=AIzaSyAiUJJ3K9BomeMzvbkJ2BezPIdDc-SzmtE'

    // Make GET request to get the respons
    request.open('GET', url, true)

    request.onload = function() {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response)

    if (request.status >= 200 && request.status < 400 && data.items != undefined) {
        for (var i = 0; i < data.items.length; i++) {
            var item = data.items[i];
            console.log(item.link)
            
            // Create a div with a card class
            const card = document.createElement('div')
            card.setAttribute('class', 'card')
            

            // Create a img with the link from API
            const img = document.createElement('img')
            img.src = String(item.link)

            // Create an h1 and set the text content to the image's title
            const h1 = document.createElement('h1')
            h1.textContent = item.title

            // Create a Anchor to link the heading to the news items
            const NewAnchor = document.createElement('a')
            NewAnchor.setAttribute('target', '_blank')
            NewAnchor.href = item.image.contextLink

            // Append the cards to the container element
            container.appendChild(card)
            NewAnchor.appendChild(h1)
            card.appendChild(NewAnchor)
            card.appendChild(img)
        }

    } else {
        const errorMessage = document.createElement('h1')
        errorMessage.textContent = `Gah, it's not working!`
        app.appendChild(errorMessage)
    }
    }

    request.send()

}

