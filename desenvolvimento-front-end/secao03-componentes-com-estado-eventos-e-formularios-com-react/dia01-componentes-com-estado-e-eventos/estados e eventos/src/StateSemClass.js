import React from 'react';
import logo from './logo.svg';
import './App.css';

class StateSemClass extends React.Component {
  state = {
    count: 0
  }

  makeCard = () => {
    this.setState((previusState, _count) => ({
      count: previusState.count + 1
    }))
  }
  
  render() {
    const { count } = this.state
    const styleDiv = {
      backgroundColor: 'red',
      height: '500px',
      width: '500px',
      border: 'solid black 3px'
    }

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <button onClick={this.makeCard}>BUTÃO</button>
          <div style={styleDiv}>numero de clicks:{ count }</div>
        </header>
      </div>
    );
  };
}

export default StateSemClass;
