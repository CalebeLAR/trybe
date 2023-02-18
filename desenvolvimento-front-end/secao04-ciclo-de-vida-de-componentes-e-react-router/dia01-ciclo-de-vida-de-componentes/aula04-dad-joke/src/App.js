import React from 'react';

class DadJoke extends React.Component {
  constructor() {
    super();
    this.saveJoke = this.saveJoke.bind(this);
    this.fetchJoke = this.fetchJoke.bind(this);

    this.state = {
      jokeObj: undefined,
      loading: true,
      storedJokes: [],
    }
  }

  async fetchJoke() {
    this.setState(
      {loading:true}, async () => {
            const requestHeaders = { headers: { Accept: 'application/json' } };
            const requestReturn = await fetch('https://icanhazdadjoke.com/', requestHeaders);
            const requestObject = await requestReturn.json();
            this.setState({
              loading: false,
              jokeObj: requestObject,
            });
        });
  };

  componentDidMount() {
    console.log('componentDidMount');
    this.fetchJoke();
  }

  saveJoke() {
    console.log('saveJoke');
    this.setState(({storedJokes, jokeObj})=>({
      storedJokes: [...storedJokes, jokeObj],
    }));
    this.fetchJoke();
  }

  render() {
    console.log('render');
    const { storedJokes, jokeObj, loading } = this.state;
    const loadingElement = (<span>Loading...<br/></span>);

    return (
      <div>
        <span>
          {storedJokes.map(({ id, joke }) => (<p key={id}>{joke}</p>))}
        </span>

      {
        loading ? loadingElement : <p style={{color: 'blue'}}>{jokeObj.joke}</p>
      }
      <button onClick={ this.saveJoke }>trocar + adicionar piada</button>

      </div>
    );
  }
}

export default DadJoke;