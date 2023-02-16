import './App.css';
import React from 'react';
import Dados from './components/Dados';

class App extends React.Component {
  constructor(){
    super();
    this.fetchResults = this.fetchResults.bind(this);
    this.state = {
      loading: true,
      results: undefined,
    }
  }

  async fetchResults(){
    this.setState({loading: true}, async ()=>{
      const headers = {}
      const promisse = await fetch('https://api.randomuser.me/', headers);
      const request = await promisse.json()
      this.setState({
        loading: false,
        results: request.results,
      }) 
    })
  }

  shouldComponentUpdate(nextProps, nextState){
    console.log('shouldComponentUpdate', nextState);
    // antes do PRIMEIRO setState do fetch:
    if(!nextState.results){
      return true;
    } 
    // antes do SEGUNDO setState de fetch:
    if(nextState.results[0].dob.age){
      if(nextState.results[0].dob.age <= 50){
        console.log(nextState.results[0].dob.age)
        return false;
      }
      console.log(nextState.results[0].dob.age)
      return true;
    }
  }

  render(){
    console.log('render')
    const { loading, results } = this.state;
    const loadingElement = <span>Loading...</span>;
    return (
      <div className="App-header">
        <h1>Api</h1>
        {
          loading ? loadingElement :  <Dados results={ results } />
        }
      </div>
    );
  }

  componentDidMount(){
    console.log('componentDidMount')
    this.fetchResults();
  }
}


export default App;
