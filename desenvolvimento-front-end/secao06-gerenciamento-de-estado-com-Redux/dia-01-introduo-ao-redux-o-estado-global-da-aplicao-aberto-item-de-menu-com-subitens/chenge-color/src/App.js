import React from "react";
import './App.css';
import Block from './components/Block';
import ChangeColorToBlack from './components/ChangeColorToBlack'
import ChangeColorToGray from './components/ChangeColorToGray'
import ChangeColorToWhit from './components/ChangeColorToWhit'

class App extends React.Component {
  // seria o estado global
  state = { color: "black" };

  // seria a peça dispatch: implementação que altera o estado global
  changerColor = (newColor) => {
    this.setState({ color: newColor });
  };

  render() {
    return(
      <div className="App App-header">
        <Block color={ this.state.color } />
        <ChangeColorToBlack 
          color={ this.state.color }
          changerColor={ this.changerColor }
        />
        <ChangeColorToGray 
          color={ this.state.color }
          changerColor={ this.changerColor }
        />
        <ChangeColorToWhit 
          color={ this.state.color }
          changerColor={ this.changerColor }
        />
      </div>
    );
  };
};

export default App;
