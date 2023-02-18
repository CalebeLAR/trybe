import React from 'react';
import logo from './logo.svg';
import './App.css';

// const func1 = () => { // quando a gente usa a notação de arrow function ele funciona sem o contructor!
//   document.getElementById('b1').innerText = `mudou b1 para: ${(Math.random() * 10).toFixed(0)}`
// };

class App extends React.Component {
  // function App () {
  constructor() {
    super();
    // this.func1 = this.func1.bind(this);
    this.func2 = this.func2.bind(this);
    this.func3 = this.func3.bind(this);
    console.log('console.log do constructor');

  }

  func1 = () => { // quando a gente usa a notação de arrow function ele funciona sem o contructor!
    console.log(this);
    document.getElementById('b1').innerText = `mudou b1 para: ${(Math.random() * 10).toFixed(0)}`
  };

  func2 () {
    console.log(this);
    document.getElementById('b2').innerText = `mudou b2 para: ${(Math.random() * 10).toFixed(0)}`
  };

  func3 () {
    console.log(this);
    document.getElementById('b3').innerText = `mudou b3 para: ${(Math.random() * 10).toFixed(0)}`
  };

  funcPrint() {
    console.log('função print')
  }


  render() {

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <button id="b1" onClick={this.func1}> botão 01</button>
          <button id="b2" onClick={this.func2}> botão 02</button>
          <button id="b3" onClick={this.func3}> botão 03</button>
        </header>
      </div>
    );
  }
}

export default App;
