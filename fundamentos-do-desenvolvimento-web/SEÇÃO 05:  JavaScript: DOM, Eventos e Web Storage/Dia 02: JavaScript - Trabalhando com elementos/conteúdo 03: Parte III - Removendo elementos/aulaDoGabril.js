let ingredientItem = [
    '500g de feijão carioquinha cozido',
    '200g de toucinho',
    '1 concha de óleo',
    '1 cebola média picada',
    '1 colher de sopa de sal com alho',
    'Cheiro verde a gosto',
    '200g de farinha de mandioca'
    ]
    
    let ingredientList = document.querySelector('.ingredients-list');
    for (let index = 0; index < ingredientItem.length; index += 1) {
        let ingredient = ingredientItem[index];

        let ingredientListItem = document.createElement('li');
        ingredientListItem.innerText = ingredient;
        ingredientListItem.className = "ingredient-list-item"
        
        ingredientList.appendChild(ingredientListItem);
    }
    
    let ingredientListItems = document.querySelectorAll('.ingredient-list-item') 
    for (nodeElemento of ingredientListItems) {
        if (nodeElemento.innerText.includes("1"))
            ingredientList.removeChild(nodeElemento)

    }