import { legacy_createStore as createStore } from 'redux';
import { composeWithDevTools } from '@redux-devtools/extension';

//funções para o reducer
const rgb = () => {
  const R = (Math.random()*250).toFixed(0).toString()
  const G = (Math.random()*250).toFixed(0).toString()
  const B = (Math.random()*250).toFixed(0).toString()
  return `rgb(${R},${G},${B})`
};

// store
const INITIAL_STATE = {
  colors: ['white', 'black', 'red', 'green', 'blue', 'yellow'],
  index: 0,
};

const reducer = (store=INITIAL_STATE, action) => {
  switch (action.type) {
    case "NEXT_COLOR":
      return {
        colors: store.colors, 
        index: store.index < store.colors.length - 1 ? store.index + 1: store.index,
      };

    case "PREVIOUS_COLOR":
      return {
        colors: store.colors, 
        index: store.index ? store.index - 1: store.index,  // 0 é false, se store.index for 0 então retorna o store.index.
      };
      
    case "INITIAL_STATE":
    return {
      colors: store.colors, 
      index: 0, 
    };

    case "RANDON_COLOR":
      const color = rgb()
      return {
        colors: [...store.colors, color],
        index: [...store.colors, color].indexOf(color),
      }

    default:
      return store;
  };
};

const store = createStore(reducer, composeWithDevTools());


// tratando o DOM
const btnPrevius = document.getElementById('previous');
const btnNext = document.getElementById('next');
const btnRandon = document.getElementById('randon');
const btnInitial = document.getElementById('initial');
const span = document.getElementById('value');

const actionNextColor = { type: "NEXT_COLOR" };
const actionPreviousColor = { type: "PREVIOUS_COLOR" };
const actionInitalColor = { type: "INITIAL_STATE" };
const actionRandonColor = { type: "RANDON_COLOR" };

btnPrevius.addEventListener('click', ()=>{
  store.dispatch(actionPreviousColor);
});

btnNext.addEventListener('click', ()=>{
  store.dispatch(actionNextColor);
});

btnInitial.addEventListener('click', ()=>{
  store.dispatch(actionInitalColor);
});

btnRandon.addEventListener('click', ()=> {
  store.dispatch(actionRandonColor);
});

store.subscribe(()=>{
  const { colors, index } = store.getState();
  const currentColor = colors[index];
  span.innerHTML = currentColor;
  span.style.color = currentColor;
});

