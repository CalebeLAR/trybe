import { legacy_createStore as createStore } from "redux";
import { composeWithDevTools } from "@redux-devtools/extension";

const INITIAL_STATE = { count: 0 }; 

const reducer = (state=INITIAL_STATE, action) => {
  switch (action.type) {
    case "INCREMENT_COUNTER":
      return { count: state.count + 1}

    default:
      return state;
  }
};

const action = { type: "INCREMENT_COUNTER" };

const store = createStore(reducer, composeWithDevTools());

const btnIncrementar = document.getElementById('btn-incrementar');
const h2 = document.getElementsByTagName('h2');
btnIncrementar.addEventListener('click', () => setTimeout(()=> store.dispatch(action), 1000));

store.subscribe(()=>{
  const { count } = store.getState();
  h2[0].innerHTML = count;
  console.log('a store foi alterada!');
});
