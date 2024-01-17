var updateBtn = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action 
        console.log(productId,action)
    
        updateUserOrder(productId, action)

    })
}

function updateUserOrder(productId, action){
    console.log('enviando datos')

    var url = 'update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productId':productId ,'action':action})
    })
    
    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })

}