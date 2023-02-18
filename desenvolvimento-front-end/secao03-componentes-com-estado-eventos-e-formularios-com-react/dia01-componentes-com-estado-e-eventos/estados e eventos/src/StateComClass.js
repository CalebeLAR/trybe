import React from 'react';
import logo from './logo.svg';
import './App.css';

class StateComClass extends React.Component {
  constructor() {
    super()
    this.makeCard = this.makeCard.bind(this);
    this.state = {
      count: 0
    }
    console.log(this)
  }

  makeCard() {
    this.setState((previusState, _count) => ({
      count: previusState + 1
    }))
  }
  
  render() {
    const styleDiv = {
      backgroundColor: this.state.cor,
      height: '500px',
      width: '500px',
      border: 'solid black 3px',
    }

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <button style={styleDiv} onClick={this.makeCard}>BUTÃO</button>
        </header>
      </div>
    );
  };
}

export default StateComClass;
