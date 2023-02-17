import { legacy_createStore as createStore, combineReducers } from 'redux';
import { composeWithDevTools } from '@redux-devtools/extension';

// primeiro redux
const THEME_INITIAL_STATE = {
  theme: 'dark',
};

const themeReducer = (state = THEME_INITIAL_STATE, action) => {
  switch (action.type) {
    case ('TOGGLE_THEME'):
      return {
        theme: state.theme === 'white' ? '#333' : 'white',
      }
    default:  
      return state;
  }
};

const actionToggleTheme = { type: "TOGGLE_THEME" }; 
const actionToggleStatus = { type: "TOGGLE_STATUS" }; 

// segundo redux
const STATUS_INITIAL_STATE = {
  status: 'offline',
};

const statusReducer = (state = STATUS_INITIAL_STATE, action) => {
  switch (action.type) {
    case ('TOGGLE_STATUS'):
      return {
        status: state.status === 'offline' ? 'online' : 'offline',
      }
    default:
      return state;
  }
};

// store
const rootReducer = Redux.combineReducers({themeReducer, statusReducer});
const store = createStore(rootReducer, composeWithDevTools());

// trabalhando o DOM
const themeButton = document.getElementById('toggle-theme');
const statusButton = document.getElementById('toggle-status');
const bodyStyle = document.querySelector('style');
const span = document.querySelector('#status');

themeButton.addEventListener('click', () => {
  store.dispatch(actionToggleTheme);
});

statusButton.addEventListener('click', () => {
  store.dispatch(actionToggleStatus);
});

store.subscribe(()=>{
  // themeReducer
  const { themeReducer: { theme } } = store.getState();
  const newStyle = `body { 
    color: ${theme === 'white' ? '#333' : 'white'}; 
    background-color: ${theme}; 
    font-family: sans-serif; 
    text-align: center; 
  }`;
  bodyStyle.innerHTML = newStyle;


  // statusReducer
  const { statusReducer: { status } } = store.getState();
  switch (status) {
    case 'offline':
      return span.innerText = 'Offline';

    case 'online':
      return span.innerText = 'Online';
  }
});