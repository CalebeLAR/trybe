import React from 'react';
import logo from './logo.svg';
import './App.css';

// const func1 = () => { // quando a gente usa a notação de arrow function ele funciona sem o contructor!
//   document.getElementById('b1').innerText = `mudou b1 para: ${(Math.random() * 10).toFixed(0)}`
// };

class App extends React.Component {
  constructor () {
    super();
    this.func2 = this.func2.bind(this) // como não são erow functions, elas precisam do bind para ativar o this dentro do escopo da função delas.
    this.func3 = this.func3.bind(this)
  }
  state = {
    countB1: 0,
    countB2: 0,
    countB3: 0
  }


  func1 = () => { // quando a gente usa a notação de arrow function ele funciona sem o contructor!
    this.setState((previusState, _prop) =>({
      countB1: previusState.countB1 + 1
    }))    
  };

  func2 () {
    this.setState((previusState, _prop) =>({
      countB2: previusState.countB2 + 1
    }))    
  };

  func3 () {
    this.setState((previusState, _prop) =>({
      countB3: previusState.countB3 + 1
    }))    
  };
  

  render() {

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <button id="b1" onClick={this.func1}> botão 01</button>
          <div>{this.state.countB1}</div>
          <button id="b2" onClick={this.func2}> botão 02</button>
          <div>{this.state.countB2}</div>
          <button id="b3" onClick={this.func3}> botão 03</button>
          <div>{this.state.countB3}</div>
        </header>
      </div>
    );
  }
}

export default App;
