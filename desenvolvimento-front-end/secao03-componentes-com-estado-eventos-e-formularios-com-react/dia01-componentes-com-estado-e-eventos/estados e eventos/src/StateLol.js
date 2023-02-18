import React from 'react';
import logo from './logo.svg';
import './App.css';

class StateLol extends React.Component {
  constructor() {
    super()
    this.makeCard = this.makeCard.bind(this);
    this.state = {
      count: 0,
      cor: '',
      tamanho: '',
      nome: '',
      imageUrl: 'https://observatoriodocinema.uol.com.br/wp-content/uploads/2021/02/homem-de-ferro-tony-divulgacao.jpg'
    }
    console.log(this)
  }

  makeCard() {
    const colors = ['#FFBF00', '#DFFF00', '#FF7F50', '#DE3163', '#9FE2BF', '#40E0D0', '#6495ED', '#CCCCFF', '#EB5002', '#EBD102'];
    const name = ['jax', 'lux', 'seraphine', 'sakarner', 'rakan', 'teemo', 'yasou', 'azir', 'gnar', 'rammus'];
    const num = (Math.random() * 9).toFixed(0);
    const string = `${num * 100}px`;
    this.setState({
      count: num,
      cor: colors[num],
      tamanho: string,
      nome: name[num]
    });
    console.log(this);
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
          <button onClick={this.makeCard}>botão</button>
          {this.state.cor}
          <div style={styleDiv}>{this.state.nome}</div>
        </header>
      </div>
    );
  };
}

export default StateLol;
